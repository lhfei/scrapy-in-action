#Simple assignment
from selenium.webdriver import Chrome

driver = Chrome()

#Or use the context manager
from selenium.webdriver import Chrome

with Chrome(executable_path='D:\\DevProfile\\ChromeDriver\\chromedriver_91.exe') as driver:
    #your code inside this indent