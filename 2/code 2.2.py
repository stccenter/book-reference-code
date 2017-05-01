>>> class Test:
	def __init__(self):
		self.__foobar = "private attr"
		self.foobar = "public attr"

		
>>> test = Test()
>>> test.foobar
'public attr'
>>> test.__foobar

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    test.__foobar
AttributeError: Test instance has no attribute '__foobar'
>>> test._Test__foobar
'private attr'
>>> 
