'''
Created on 2018年7月8日

@author: sunshyran
'''
from android.content.ContentProvider import ContentProvider
from android.content.Context import Context
from android.content.Intent import Intent
from android.os.Bundle import Bundle


if __name__ == '__main__':
    from client.json.ClientProxy import ClientProxy
    client = ClientProxy('127.0.0.1', 12346)
    context = Context(client)
    context.sendBroadcast(Intent(action='abc'), '')
    
    provider = ContentProvider(client)
    provider.call('any', 'arg', None)
    
    print('over')