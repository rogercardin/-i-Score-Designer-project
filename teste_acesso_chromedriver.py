from lib2to3.pgen2 import driver
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.med.nagoya-u.ac.jp/neurogenetics/i_Score/i_score.html')