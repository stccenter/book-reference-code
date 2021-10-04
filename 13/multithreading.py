import threading
import time
class SummingThread(threading.Thread):
     def __init__(self,low,high):
         threading.Thread.__init__(self)
         self.low=low
         self.high=high
         self.total=0

     def run(self):
         for i in range(self.low,self.high):
             time.sleep(0.01)               
             self.total+=i
threads = []
for i in range(10):
     threads.append(SummingThread(i*100,(i+1)*100))

starttime = time.clock()

for i in range(10):
     threads[i].start() # This actually causes the thread to run
     
for i in range(10):
     threads[i].join() # This waits until the thread has completed
# At this point, both threads have completed
result = 0
for i in range(10):
     result+=threads[i].total
     
print('10 threads ')
print(result)
print(str(time.clock()-starttime) + ' seconds\n')

thread = SummingThread(0,1000)
starttime = time.clock()
thread.start()
thread.join()
print('single thread')
print(thread.total)
print(str(time.clock()-starttime) + ' seconds\n')
