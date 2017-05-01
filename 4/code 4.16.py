>>> f = open ('C:/Users/Phil/Downloads/points.txt', 'r')
>>> f.readline()  # Read the 1st  line
>>> f.readline() # Read the 2nd line
>>> f.readline()  # Read the 3rd line
>>> f.readline () # end of the file
>>> f.seek(0)  #go to the begin of file
>>> f.readline() 
>>> f.readlines() # read rest lines in a list
>>> f.seek(0)
>>> f.read() # read rest lines as a string
>>> f.close()
