#!/usr/local/bin python3

"""Persional string module


""" 

__author__ = "Clar kAaron"
__version__ = "v0.0"
__email__ = "clarkaaron@163.com"

from collections import Iterable as iter_able

class Iterator:
    value = None
    index = 0

    def __init__(self,iterable,count=1 ):
        '''
        描述:该函数用于实现类实例化时的属性值初始化
        '''
        if isinstance(iterable,iter_able):
            length = len(iterable)
            if length == 1:
                self.__iterable = [ chr( ord(iterable) + index ) for index in range(0,count) ]
            else:
                self.__iterable = [ char for char in iterable ]
        else:
            raise TypeError("iterable:{} object is not iterable".format( type(iterable).__name__ ) )
        self.Iter = iter( self.__iterable )

    def __next__(self):
        '''
        描述:该函数用于next()函数迭代下一个值;
        '''
        if( self.index < len(self.__iterable) ):
            self.index += 1
        else:
            self.Iter = iter(self.__iterable)
            self.index = 1
        self.value = next(self.Iter)
        return self.value

    def __iter__(self):
        '''
        描述:该函数用于实现类的实例化的迭代功能;
        '''
        for i in range( 0, len(self.__iterable) ):
            yield self.__next__()
    
    def __len__(self):
        return len(self.__iterable)
'''
Iterators: 使用Iterator组成列表,并将迭代值组成字符串返回
'''
class Iterators:

    def __init__(self,count,iterable,length=1):
        self.__list_iter = [ Iterator(iterable,length) for index in range(0,count) ]
        self.__status = [ True for index in range(0,count) ]

    def __next__(self):
        count = len( self.__list_iter )
        length = len( self.__list_iter[0] )
        strings = ''
        #-------------------------------------------------
        for index in range(0,count):
            if self.__status[index]:
                next(self.__list_iter[index])
            #----------------------------------------------
            FLAG = True
            for i in range(0,index):
                if self.__list_iter[i].index != length:
                    FLAG = False
                    break
            self.__status[index] = FLAG
            #print(self.__list_iter[index].index,end=' ')
        #--------------------------------------------------
        # 
        for index in range(0, len(self.__list_iter) ):
            if not self.__list_iter[index].value:
                strings = None
                break
            strings += str(self.__list_iter[index].value)
        #---------------------------------------------------
        return strings
        
    def __iter__(self):
        count = len(self.__list_iter)
        length = len( self.__list_iter[0] )
        for index in range(0,length**count):
            yield next(self)
        
    def __len__(self):
        count = len( self.__list_iter )
        length = len( self.__list_iter[0] )
        return length**count     


if __name__ == '__main__':

    '''
    Iter = getChar_iter('a',26)
    print("迭代对象Iter,迭代数量{}".format(Iter.length))
    for index in range(0,Iter.length):
        char = Iter.iterNext()
        print("第{}个迭代值:{}".format(Iter.index,Iter.value))
    '''
    Tuple0 = ('!','@','#','$','%','^','&','*','(',')')
    char = ('1','2','3','4','5','6','7','8','9','0')
    iterable0 = Iterator(Tuple0)
    iterable1 = Iterator(char)
    for each in iterable0:
        print( "{} --> {}".format(next(iterable1), each ) )
