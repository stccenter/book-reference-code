>>> a = [1,2,3,4]
>>> a
[1, 2, 3, 4]
>>> b = [x*3 for x in a]
>>> b
[3, 6, 9, 12]
>>> a[0]
1
>>> a[3]
4
>>> a[4]

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a[4]
IndexError: list index out of range
>>> len(a)
4
>>> a[1:3]
[2, 3]
>>> del a[0]
>>> a
[2, 3, 4]
>>> a*3
[2, 3, 4, 2, 3, 4, 2, 3, 4]
>>> a+b
[2, 3, 4, 3, 6, 9, 12]
>>> a = [1,4,7,9]
>>> sum = 0
>>> for i in a:
	sum+=i

	
>>> sum
21
>>> 
