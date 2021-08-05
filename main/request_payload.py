import random

#------------------------
# Request Payload class
#------------------------
class RequestPayload:
  
  def __init__(self):
    self.__model = None
    self.__domain = None
    self.__fields = None
    self.__limit = None
    self.__user_info = None
    self.__partner_ids = None
    # self.__ip_client = None
    self.__args = None
    self.__method = None
    self.__context = {}

  # Set model
  def model(self, model:str):
    self.__model = model
    return self

  # Set domain
  def domain(self, domain:list):
    self.__domain = domain
    return self

  # Set fields
  def fields(self, fields:list):
    self.__fields = fields
    return self

  # Set limit
  def limit(self, limit:int):
    self.__limit = limit
    return self

  # Set user information
  def user_info(self, user_info):
    self.__user_info = user_info
    return self

  # Set Partner ids
  def partner_ids(self, partner_ids):
    self.__partner_ids = partner_ids
    return self
  
  # Set ip client
  # def ip_client(self, ip_client):
  #   self.__ip_client = ip_client
  #   return self

  # Set args
  def args(self, args):
    self.__args = args
    return self

  # Set method
  def method(self, method):
    self.__method = method
    return self

  # Add context
  def add_context(self, context_value:dict):
    self.__context = self.__context | context_value
    return self

  # Build Request payload
  def build(self, context_kwargs=False):
    id = random.randint(0, 999999999)
    context = {}
    if self.__user_info:
      context = self.__user_info['user_context'] | {'bin_size': True, 'allowed_company_ids': [self.__user_info['user_companies']['allowed_companies'][0][0]]}

    # if self.__ip_client:
    #   context['ip_client'] = self.__ip_client
    context = context | self.__context

    payload = {}
    payload['jsonrpc'] = '2.0'
    payload['method'] = 'call'
    payload['params'] = {}
    if self.__model:
      payload['params']['model'] = self.__model
    if self.__domain:
      payload['params']['domain'] = self.__domain
    if self.__fields:
      payload['params']['fields'] = self.__fields
    if self.__limit:
      payload['params']['limit'] = self.__limit
    if context:
      if not context_kwargs:
        payload['params']['context'] = context
      else:
        payload['params']['kwargs'] = {'context': context}
    if self.__partner_ids:
      payload['params']['partner_ids'] = self.__partner_ids
    if self.__args != None:
      payload['params']['args'] = self.__args
    if self.__method:
      payload['params']['method'] = self.__method
    payload['id'] = id
    return payload, id
