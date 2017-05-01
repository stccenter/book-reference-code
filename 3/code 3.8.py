>>> a = [1,2,3,4]
>>> a
[1, 2, 3, 4]
>>> a[0]=5
>>> a
[5, 2, 3, 4]
>>> x = (1,2,3,4)
>>> x
(1, 2, 3, 4)
>>> x[0]=5

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    x[0]=5
TypeError: 'tuple' object does not support item assignment
>>> 
