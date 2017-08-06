from utils.Singleton import singleton
import inspect
import logging
import os.path
import sys

class Logger(object):
    '''
    classdocs
    '''

    #logformat = logging.Formatter("[%(name)s] [%(levelname)s] %(message)s")
    logformat = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s")
    def __init__(self, name, logpath):
        '''
        Constructor
        '''
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # 建立一个filehandler来把日志记录在文件里，级别为debug以上
        fh = logging.FileHandler(os.path.join(r'D:\\', logpath))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.logformat)
        self.logger.addHandler(fh)
        self.filehandler = fh
        
        # 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        ch.setFormatter(self.logformat)
        self.logger.addHandler(ch)
        self.screenhandler = ch
    
    
    def setLevel(self, file_level=logging.DEBUG, stdout_level=logging.ERROR):
        self.filehandler.setLevel(file_level)
        self.screenhandler.setLevel(stdout_level)

    
    def setFormatter(self, formatter):
        '''
        %(name)s Logger的名字
        %(levelname)s 文本形式的日志级别
        %(message)s 用户输出的消息
        %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
        %(levelno)s 数字形式的日志级别
        %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
        %(filename)s 调用日志输出函数的模块的文件名
        %(module)s  调用日志输出函数的模块名
        %(funcName)s 调用日志输出函数的函数名
        %(lineno)d 调用日志输出函数的语句所在的代码行
        %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
        %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
        %(thread)d 线程ID。可能没有
        %(threadName)s 线程名。可能没有
        %(process)d 进程ID。可能没有
        '''
        self.filehandler.setFormatter(formatter)
        self.screenhandler.setFormatter(formatter)
    
    def debug(self, tag, message, *args, **kwargs):
        self.logger.getChild(tag).debug(message, *args, **kwargs)
    
    def info(self, tag, message, *args, **kwargs):
        self.logger.getChild(tag).info(message, *args, **kwargs)
        
    def warning(self, tag, message, *args, **kwargs):
        self.logger.getChild(tag).warning(message, *args, **kwargs)
    
    def error(self, tag, message, *args, **kwargs):
        self.logger.getChild(tag).error(message, *args, **kwargs)
        
    def critical(self, tag, message, *args, **kwargs):
        self.logger.getChild(tag).critical(message, *args, **kwargs)
    
    def exception(self, tag, msg, *args, **kwargs):
        self.logger.getChild(tag).exception(msg, *args, **kwargs)
    
    @classmethod    
    def __LINE__(cls):
        f = inspect.currentframe()
        return inspect.getframeinfo(f).lineno
    

