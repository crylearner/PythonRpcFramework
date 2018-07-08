'''
Created on 2018年7月7日

@author: sunshyran
'''
from urlobject.urlobject import URLObject


class Uri(object):
    
    def isHierarchical(self):
        raise NotImplementedError
    
    def isOpaque(self):
        '''
        Returns true if this URI is opaque like "mailto:nobody@google.com". The
        scheme-specific part of an opaque URI cannot start with a '/'.
        '''
        return not self.isHierarchical();

    def isRelative(self):
        raise NotImplementedError
    
    def isAbsolute(self):
        return not self.isRelative()
    
    def getScheme(self):
        raise NotImplementedError
    
    def getSchemeSpecificPart(self):
        raise NotImplementedError
    
    def getAuthority(self):
        raise NotImplementedError
    
    def getUserInfo(self):
        raise NotImplementedError
    
    def getHost(self):
        raise NotImplementedError
    
    def getPort(self):
        raise NotImplementedError
    
    def getPath(self):
        raise NotImplementedError
    
    def getQuery(self):
        raise NotImplementedError
    
    def getFragment(self):
        raise NotImplementedError
    
    def getPathSegments(self):
        raise NotImplementedError
    
    @classmethod
    def parse(cls, uri_string):
        return StringUri(uri_string)
    

class AbstractHierarchicalUri(Uri):

    def isHierarchical(self):
        return True
    
    
    
class HierarchicalUri(AbstractHierarchicalUri):
    
    def __init__(self, scheme, authority, path, query, fragment):
        super().__init__()
        self._scheme = scheme
        self._netloc = authority
        self._path   = path
        self._query  = query
        self._fragment=fragment
        self._uri    = URLObject()
        self._uri.with_scheme(scheme)
        self._uri.with_auth(authority)
        self._uri.with_path(path)
        self._uri.with_query(query)
        self._uri.with_fragment(fragment)
        
    def isHierarchical(self):
        return True
        
    def isRelative(self):
        return self._scheme is None 

    def getScheme(self):
        return self._uri.scheme

    def getSchemeSpecificPart(self):
        uriString = str(self._uri)
        return uriString.replace("%s:" % self.getScheme()).replace('#%s' %self.getFragment())


    def getAuthority(self):
        return self._uri.auth

    def getPath(self):
        return self._uri.path

    def getQuery(self):
        return self._uri.query

    def getFragment(self):
        return self._uri.fragment


    def getPathSegments(self):
        return self._uri.path.segments
    

    def getUserInfo(self):
        return self._uri.auth

    def getHost(self):
        return self._uri.hostname
    
    def getPort(self):
        return self._uri.port

class OpaqueUri(Uri):
    '''like as "mailto:nobody@google.com"
    '''
    def __init__(self, scheme, schemeSpecific, fragment):
        self._scheme = scheme
        self._schemeSpecific = schemeSpecific
        self._fragment=fragment
    
    def isHierarchical(self):
        return False
        
    def isRelative(self):
        return self._scheme is None 

    def getScheme(self):
        return self._scheme

    def getSchemeSpecificPart(self):
        return self._schemeSpecific

    def getAuthority(self):
        return None

    def getPath(self):
        return None

    def getQuery(self):
        return None

    def getFragment(self):
        return self._fragment


    def getPathSegments(self):
        return ()
    

    def getUserInfo(self):
        return None

    def getHost(self):
        return None
    
    def getPort(self):
        return -1
    
class StringUri(AbstractHierarchicalUri):
    
    def __init__(self, uri_string):
        self._uriString = uri_string
        self._uri = URLObject(self._uriString)
        
    def isHierarchical(self):
        if ':' not in self._uriString: return True
        return self._uriString.statswith(self._uri.scheme + ':/')
    
    def isRelative(self):
        return  ':' not in self._uriString
    
    def getScheme(self):
        return self._uri.scheme
        
    def getSchemeSpecific(self):
        return self._uriString.replace("%s:" % self.getScheme()).replace('#%s' %self.getFragment())
    
    def getAuthority(self):
        return self._uri.auth
    
    def getPath(self):
        return self._uri.path
    
    def getPathSegments(self):
        return self._uri.path.segments
    
    def getQuery(self):
        return self._uri.query
    
    def getFragment(self):
        return self._uri.fragment
    

if __name__ == '__main__':
    quat = URLObject("mailto:nobody@google.com")
    print(quat.scheme)
    print(quat.auth)
    print(quat.path)