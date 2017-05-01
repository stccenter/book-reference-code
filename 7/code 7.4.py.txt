>>> float([1,2,3])

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float([1,2,3])
TypeError: float() argument must be a string or a number
>>> #A
>>> x = [1,2,3,4]
>>> x[4]

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x[4]
IndexError: list index out of range
>>> #C
>>> float('strv1')

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    float('strv1')
ValueError: could not convert string to float: strv1
>>> #B
>>> 1/0

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    1/0
ZeroDivisionError: integer division or modulo by zero
>>> #D
