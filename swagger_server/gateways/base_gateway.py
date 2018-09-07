import datetime

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

def getMillisecondTimestamp(now_=None, today=None):
    ''' 
        Returns milliscond timestamp since midnight today,
        optional now_ & today parameters facilitate testing
    '''
    if today is None:
        tmp = datetime.datetime.utcnow()
        today = datetime.datetime(tmp.year, tmp.month, tmp.day)
    ts = datetime.datetime.utcnow() - today
    if now_:
        ts = now_ - today
    ms = 0
    ms += ts.seconds * 1000
    ms += int(ts.microseconds / 1000)
    return ms
