# script 1
# 0 to 5
0 = __name__.__class__().__len__()
1 = __name__.__getnewargs__().__len__()
2 = __name__.__class__().__repr__().__len__()
3 = __name__.__class__.__name__.__len__()
4 = __name__.__class__.__class__.__name__.__len__()
5 = __name__.__getnewargs__().__class__.__name__.__len__()
# 6 to 17
6 = __name__.__lt__.__name__.__len__()
7 = __name__.__dir__.__name__.__len__()
8 = __name__.__hash__.__name__.__len__() # do you see the pattern?
17 = __name__.__init_subclass__.__name__.__len__()
# for 18 and above, just use __add__, __mul__, and other magic methods

# script 2
c = __name__.__contains__.__name__.__getitem__(__name__.__class__().__repr__().__len__())
e = __name__.__ne__.__name__.__getitem__(__name__.__class__.__name__.__len__())
h = __name__.__hash__.__name__.__getitem__(__name__.__class__().__repr__().__len__())
r = __name__.__dir__.__name__.__getitem__(__name__.__class__.__class__.__name__.__len__())
x = __name__.__reduce_ex__.__name__.__getitem__(__name__.__format__.__name__.__len__())
