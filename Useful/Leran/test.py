from sys import argv


class Song(object):
	def __init__(self,lyrics):
		self.lyrics=lyrics
	def sing_me_song(self):
		for line in self.lyrics:
			print(line)

happy_song=Song(['hatty birthday to you ','i dont want to get sued','So i will stop right here'])

bulls_on_parade=Song(['They really around the famlity','Whih pockets full of shells'])


happy_song.sing_me_song()
bulls_on_parade.sing_me_song()	


class X(Y):  #创建一个类X，它是Y的一种

class X(object):#创建一个
	def __init__(self,J):  #__init__是类X的一个函数，接收self和J作为参数
	print(J)
	
foo=x() #foo作为类X的一个实例

foo.M(J)  #调用函数M，并使用self 和J进行传值

foo.K=Q  #从foo中获取K属性，并将它赋值为Q