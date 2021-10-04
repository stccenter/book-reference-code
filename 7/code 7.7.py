>>> f = None
>>> try:
        f = open('sample.txt', 'r+')
        f.readline()
        f.readlines()
        f.seek(0)
        f.read()
        f.write('This is a test!')
>>> except IOError:
        print('The file does not exist!')
>>> finally:
        if f:
            f.close()
