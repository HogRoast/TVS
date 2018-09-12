import time

'''''
Gateway Errors...
'''''
'''''
Gateway not connected or session invalidated in some form
'''''
class InvalidSessionError(Exception):
    def __init__(self, msg):
        self.msg = msg

'''''
Account does not exist for this gateway
'''''
class InvalidAccountError(Exception):
    def __init__(self, msg):
        self.msg = msg

'''''
Account exists but is not permissioned for this action
'''''
class AccountPermissionError(Exception):
    def __init__(self, msg):
        self.msg = msg

'''''
Order paramters are not valid
'''''
class OrderValidationError(Exception):
    def __init__(self, msg):
        self.msg = msg

'''''
Server request failure
'''''
class ServerRequestError(Exception):
    def __init__(self, errorCode, msg):
        self.errorCode = errorCode
        self.msg = msg

'''''
Gateway Ops...
'''''
def established(fn):
    '''
        Decorator to ensure applicable methods have a valid session when called
    '''    
    def wrapper(*args, **kwargs):
        if args[0].session:
            return fn(*args, **kwargs)
        raise InvalidSessionError('Session not established')
    return wrapper

def getMillisecondTimestamp():
    return int(time.time() * 1000)
