# import threading
# import time
# exitflag=0

# class my_thread(threading.Thread):
	# def __init__(self,name,threadid):
		# #threading.Thread.__init__(self)
		# super(my_thread,self).__init__()
		# self.name=name
		# self.threadid=threadid
	# def run(self):
		# print('strating'+self.name)
		# threadlock.acquire()
		# Print_time(self.name,3,6)
		# threadlock.release()
		# #print('exiting'+self.threadid)
		
# def Print_time(threadname,delay,counter):
	# while counter:
		# #if exitflag:
		# #	threading.Thread.exit()
		# time.sleep(delay)
		# print('%s,%s'%(threadname,time.ctime(time.time())))
		# counter =counter- 1
# threads=[]
# threadlock=threading.Lock()		
		
# thread1=my_thread('thread--11','1')
# thread2=my_thread('thread--22','2')
# thread=threading.Thread()
# print('获取线程名称',thread.getName())

# thread1.start()
# thread2.start()

# threads.append(thread1)
# threads.append(thread2)

# #print('exiting main thread')

# for t in threads:
	# t.join()
# print('Exit Main threads')

# #python3 queue模块Queue类的用法
# import queue

# q=queue.Queue()
# for i in range(5):
	# q.put(i)
	# print(q)
	
# while not q.empty():
	# print(q.get(i))
	
	
	
# #学习多线程编程threading.Thread
# import threading,time

# def loop():
	# print('thread%s is running'%(threading.current_thread().name))
	# n=0
	# while n<5:
		# n+=1
		# print('thread %s >>%s'%(threading.current_thread().name,n))
		# time.sleep(1)
	# print('thread%s is ended'%(threading.current_thread().name))
# print('thread%s is now running'%(threading.current_thread().name))

	
# t=threading.Thread(target=loop，name='LoopThread')  #name参数不填写，则程序自动命名为thread1,thread2....
# t.start()
# t.join()
# print('thread %s is ended'%(threading.current_thread().name))
	
	
#threading.Thread.lock()

import threading,time

balance=0
lock=threading.Lock()
def change_it(n):
	global balance
	balance=balance+n
	balance=balance-n 

def run(n):
	for i in range(10000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()
thread1=threading.Thread(target=run,args=(15,))
thread2=threading.Thread(target=run,args=(8,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(balance)
		
		