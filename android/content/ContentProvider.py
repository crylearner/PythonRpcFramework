'''
Created on 2018年7月7日

@author: sunshyran
'''
from android.database.Cursor import Cursor


class ContentProviderQueryError(Exception):
    
    def __init__(self, uri, projection, selection, selectionArgs, sortOrder, error):
        super().__init__("query failed: uri=%s, selection=%s, selectionArgs=%s\n%s" %(uri, selection, selectionArgs,error))

class ContentProvider(object):
    
    def __init__(self, client):
        self.client = client
    
    
    def query(self, uri, projection, selection, selectionArgs, sortOrder):
        '''
        @param uri: Uri
        @param projection: columns to query. a list type
        @param selection: where  
        @return Cursor
        '''
        rsp = self.client.call('ContentProvider.query', {
            'uri':uri,
            'projection':projection,
            'selection':selection,
            'selectionArgs':selectionArgs,
            'sortOrder':sortOrder})
        if rsp.error is not None:
            raise ContentProviderQueryError(uri, projection, selection, selectionArgs, sortOrder, rsp.error)
        return Cursor(self.client, rsp.result['Cursor']['token'])
    
    def insert(self, uri, content_values):
        '''
        @return Uri
        '''
        rsp = self.client.call('ContentProvider.insert', {"uri":uri, "values":content_values.toJson()})
        if rsp.error is not None:
            raise Exception(rsp.error)
        return rsp.result['Uri']
    
    def update(self, uri, content_values, selection, selectionArgs):
        '''
        '''
        rsp = self.client.call('ContentProvider.update', {"uri":uri, 
                                                          "values":content_values.toJson(),
                                                          'selection':selection,
                                                          'selectionArgs':selectionArgs})
        if rsp.error is not None:
            raise Exception(rsp.error)
        return rsp.result
    
    def delete(self, uri, selection, selectionArgs):
        '''
        '''
        rsp = self.client.call('ContentProvider.delete', {"uri":uri, 
                                                          'selection':selection,
                                                          'selectionArgs':selectionArgs})
        if rsp.error is not None:
            raise Exception(rsp.error)
        return rsp.result
    
    def call(self, method, arg, extras):
        '''
        @param arg: str type
        @param extras: Bundle type
        '''
        rsp = self.client.call('ContentProvider.call', {"method":method, 
                                                        'arg':arg,
                                                          'extras':extras.toJson() if extras else None})
        if rsp.error is not None:
            raise Exception(rsp.error)
        

if __name__ == '__main__':
    pass