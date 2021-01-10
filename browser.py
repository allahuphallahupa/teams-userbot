'''Работа с браузером'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement 


# TODO: шобы многа браузеров могло изспользовать. пока тока сафаре
class Browser:
	#Взаимодействие с браузером
	def __init__(self):
		#Инициализация веб драйвера
		self.driver = webdriver.Safari()

	def click_element(element:WebElement):
		element.click_element()

	def get_page(page:str, self):
		#Получает страничку. 
		self.driver.get(page)

	def get_element(self, xpath:str)->WebElement:
		#Ждет пока элемент подгрузится и выводит его
		WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
		element = self.driver.find_element_by_xpath(xpath)
		return element 
	def close(self)
		self.driver.close()