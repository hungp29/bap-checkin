import logging as log
from util.file_util import load_session, load_user_info
from main.bemo_authen import BemoAuthen
from main.bemo_status import BemoStatus

# Decorator session, it will load session and user information that saved before
def session(function):
  def wrap_function(*args, **kwargs):
    # load session
    session = load_session()
    # load user information
    user_info = load_user_info()
    # if session or user information is empty then call API to get session and user_info
    if not session or not user_info:
      log.debug('Call API to get session and user information')
      session, user_info = BemoAuthen().login_and_save_session()
    elif not BemoStatus().check_status(session, user_info):
      session, user_info = BemoAuthen().login_and_save_session()
    # attend session and user information to kwargs
    kwargs['session'] = session
    kwargs['user_info'] = user_info
    # call function to continue processing
    return function(*args, **kwargs)
  return wrap_function
