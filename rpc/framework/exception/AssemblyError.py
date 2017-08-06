'''
Created on 2016年4月9日

@author: sunshyran
'''
from rpc.framework.exception.RpcError import RpcError


class AssemblyError(RpcError):
    pass

if __name__ == '__main__':
    print(AssemblyError("fsdfsf"))