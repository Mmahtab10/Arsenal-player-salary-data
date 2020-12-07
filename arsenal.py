from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import pandas as pd

print('\nWelcome to Arsenal FC players payroll page\n')
page_num = input('Enter the year for payroll data (2011-2020): ')

df = pd.DataFrame(columns = ['Player', 'Salary', 'Year']) #creates a master dataframe


driver = webdriver.Chrome('/Users/mahtabkhan/Documents/chromedriver')

if(page_num != 2020):
	url = 'https://www.spotrac.com/epl/arsenal-fc/payroll/' + page_num + '/'
else:
	url = 'https://www.spotrac.com/epl/arsenal-fc/payroll/'	

driver.get(url)

players = driver.find_elements_by_xpath('//td[@class="player"]')
salaries = driver.find_elements_by_xpath('//td[@class="cap info"]')

#to get the text of each player into a list
players_list = []
for p in range(len(players)):
	players_list.append(players[p].text)
#to get the salaries into a list
salaries_list = []
for s in range(len(salaries)):
	salaries_list.append(salaries[s].text)	

data_tuples = list(zip(players_list[1:],salaries_list[1:])) # list of each players name and salary paired together
temp_df = pd.DataFrame(data_tuples, columns=['Player','Salary']) # creates dataframe of each tuple in list
temp_df['Year'] = page_num   # adds season beginning year to each dataframe
df = df.append(temp_df)  #appends to master dataframe


driver.close()