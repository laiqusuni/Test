import time

class MyDateUtils:

	def showDate(self):
		currentDate = time.localtime()
		formatDate = time.strftime('%Y-%m-%d', currentDate)
		print('current date:', formatDate)

if __name__ == '__main__':
	obj = MyDateUtils()
	obj.showDate()