'''
Created on 2015年12月12日

@author: sunshyran
'''

class ErrorCode():
    '''
    Json-Rpc 2.0 error code predefined 
    code    message    meaning
    -32700    Parse error    Invalid JSON was received by the server.
    An error occurred on the server while parsing the JSON text.
    -32600    Invalid Request    The JSON sent is not a valid Request object.
    -32601    Method not found    The method does not exist / is not available.
    -32602    Invalid params    Invalid method parameter(s).
    -32603    Internal error    Internal JSON-RPC error.
    -32000 to -32099    Server error    Reserved for implementation-defined server-errors.
    '''
    
    @classmethod
    def message(cls, code):
        '''
        return human meaning message corresponding this error code
        '''
        return cls._ERROR_MESSAGE.get(code, '')
    
    
    
    PARSE_ERROR           = -32700  #Parse error
    INVALID_REQUEST       = -32600  #Invalid Request
    METHOD_NOT_FOUND      = -32601  #Method not found
    INVALID_METHOD_PARAMS = -32602  #invalid parameters
    INTERNAL_ERROR        = -32603  #"all other errors"

    #
    PROCEDURE_EXCEPTION    = -32000
    AUTHENTIFICATION_ERROR = -32001
    PERMISSION_DENIED      = -32002
    INVALID_PARAM_VALUES   = -32003
    
    # custom error code for client error
    # with form -304XX
    
    
    # custom error code for server error
    # with form -305XX
    
    
    CHANNEL_CLOSED_ERROR = -30600
    TIME_OUT             = -30601
    

    #human-readable messages
    _ERROR_MESSAGE = {
        PARSE_ERROR           : "Parse error.",
        INVALID_REQUEST       : "Invalid Request.",
        METHOD_NOT_FOUND      : "Method not found.",
        INVALID_METHOD_PARAMS : "Invalid parameters.",
        INTERNAL_ERROR        : "Internal error.",
    
        PROCEDURE_EXCEPTION   : "Procedure exception.",
        AUTHENTIFICATION_ERROR : "Authentification error.",
        PERMISSION_DENIED   : "Permission denied.",
        INVALID_PARAM_VALUES: "Invalid parameter values.",
    
        CHANNEL_CLOSED_ERROR    : 'Channel is closed',
        TIME_OUT            : 'timeout'
        }


class RpcError(Exception):
    """Base class for Rpc-errors."""
    
    def __init__(self, error_code, error_data=None):
        super().__init__()
        self.error_code   = error_code
        self.error_message = ErrorCode.message(error_code)
        self.error_data   = error_data

    def code(self):
        '''
        error code
        '''
        return self.error_code
     
    def __str__(self):
        return "Rpc Error %s : %s (%s)" %(self.code(), ErrorCode.message(self.code()), repr(self.error_data))


class RpcTransportError(RpcError):
    """Transport error."""
    
class RpcTimeoutError(RpcError):
    """Transport/reply timeout."""
    def __init__(self, error_data=None):
        RpcError.__init__(self, ErrorCode.TIME_OUT,  error_data)


class RpcParseError(RpcError):
    """Broken rpc-package. (PARSE_ERROR)"""
    def __init__(self, error_data=None):
        RpcError.__init__(self, ErrorCode.PARSE_ERROR, error_data)

class RpcInvalidRPC(RpcError):
    """Invalid rpc-package. (INVALID_REQUEST)"""
    def __init__(self, error_data=None):
        RpcError.__init__(self, ErrorCode.INVALID_REQUEST, error_data)

class RpcMethodNotFound(RpcError):
    """Method not found. (METHOD_NOT_FOUND)"""
    def __init__(self, error_data=None):
        RpcError.__init__(self, ErrorCode.METHOD_NOT_FOUND, error_data)

class RpcInvalidMethodParams(RpcError):
    """Invalid method-parameters. (INVALID_METHOD_PARAMS)"""
    def __init__(self, error_data=None):
        RpcError.__init__(self, ErrorCode.INVALID_METHOD_PARAMS, error_data)

class RpcInternalError(RpcError):
    """Internal error. (INTERNAL_ERROR)"""
    def __init__(self, error_data=None):
        RpcError.__init__(self, ErrorCode.INTERNAL_ERROR, error_data)


class RpcProcedureException(RpcError):
    """Procedure exception. (PROCEDURE_EXCEPTION)"""
    def __init__(self, error_data=None):
        RpcError.__init__(self, ErrorCode.PROCEDURE_EXCEPTION,  error_data)
class RpcAuthentificationError(RpcError):
    """AUTHENTIFICATION_ERROR"""
    def __init__(self, error_data=None):
        RpcError.__init__(self, ErrorCode.AUTHENTIFICATION_ERROR, error_data)
class RpcPermissionDenied(RpcError):
    """PERMISSION_DENIED"""
    def __init__(self, error_data=None):
        RpcError.__init__(self, ErrorCode.PERMISSION_DENIED, error_data)
class RpcInvalidParamValues(RpcError):
    """INVALID_PARAM_VALUES"""
    def __init__(self, error_data=None):
        RpcError.__init__(self, ErrorCode.INVALID_PARAM_VALUES, error_data)



if __name__ == '__main__':
    print(ErrorCode.message(ErrorCode.INVALID_REQUEST))
    error = RpcInvalidParamValues("datd")
    print(error)
    
    