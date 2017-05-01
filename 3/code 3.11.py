>>> s = set(['A','B','C','D'])
>>> t = set(['A','B','E','F'])
>>> s-t
set(['C', 'D'])
>>> s&t
set(['A', 'B'])
>>> s^t
set(['C', 'E', 'D', 'F'])
>>> s|t
set(['A', 'C', 'B', 'E', 'D', 'F'])
>>> s.difference(t)
set(['C', 'D'])
