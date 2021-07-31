import random

#------------------------
# Request Payload class
#------------------------
class RequestPayload:
  
  def __init__(self):
    self.__model_data = None
    self.__domain_data = None
    self.__fields_data = None
    self.__limit_data = None
    self.__user_info_data = None
    self.__partner_ids_data = None

  # Set model
  def model(self, model_data:str):
    self.__model_data = model_data
    return self

  # Set domain
  def domain(self, domain_data:list):
    self.__domain_data = domain_data
    return self

  # Set fields
  def fields(self, fields_data:list):
    self.__fields_data = fields_data
    return self

  # Set limit
  def limit(self, limit_data:int):
    self.__limit_data = limit_data
    return self

  # Set user information
  def user_info(self, user_info_data):
    self.__user_info_data = user_info_data
    return self

  # Set Partner ids
  def partner_ids(self, partner_ids_data):
    self.__partner_ids_data = partner_ids_data
    return self

  # Build Request payload
  def build(self):
    id = random.randint(0, 999999999)
    context = {}
    if self.__user_info_data:
      context = self.__user_info_data['user_context'] | {'bin_size': True, 'allowed_company_ids': [self.__user_info_data['user_companies']['allowed_companies'][0][0]]}
    payload = {}
    payload['jsonrpc'] = '2.0'
    payload['jsonrpc'] = 'call'
    payload['params'] = {}
    if self.__model_data:
      payload['params']['model'] = self.__model_data
    if self.__domain_data:
      payload['params']['domain'] = self.__domain_data
    if self.__fields_data:
      payload['params']['fields'] = self.__fields_data
    if self.__limit_data:
      payload['params']['limit'] = self.__limit_data
    if context:
      payload['params']['context'] = context
    if self.__partner_ids_data:
      payload['params']['partner_ids'] = self.__partner_ids_data


    #   "jsonrpc": "2.0",
    #   "method": "call",
    #   "params": {
    #       "model": self.__model_data,
    #       "domain": self.__domain_data,
    #       "fields": self.__fields_data,
    #       "limit": self.__limit_data,
    #       "sort": "",
    #       "context": context
    #   },
    #   "id": id
    # }
    return payload, id
