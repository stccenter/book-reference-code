>>> class Test:
	version = 1.0

	
>>> Test.version
1.0
>>> t1 = Test()
>>> t2 = Test()
>>> t1.version
1.0
>>> t2.version
1.0
>>> Test.version = 2.0
>>> t1.version
2.0
>>> t2.version
2.0
>>> t1.version = 3.0
>>> t1.version
3.0
>>> Test.version
2.0
>>> t2.version
2.0
>>> 
