from selenium import webdriver

type(webdriver.Safari().get('https://proglib.io/p/web-scraping').find_element(By.CLASS, 'sheet-header__logo flex valign-center'))
class Browser:
	#Взаимодействие с браузером
	def __init__(self):
		#Инициализация веб драйвера
		pass	
	
	def get_page(self):
		#Получает страничку и добавляет ее в self
		pass

	def get_element(self)->None:
		pass