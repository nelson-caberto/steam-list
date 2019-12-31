from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from time import sleep
import csv

#fails with headless option
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

driver.get('https://store.steampowered.com/login/')
driver.find_element_by_name('username').send_keys(input('Steam account name: '))
driver.find_element_by_name('password').send_keys(getpass())
driver.find_element_by_xpath('//*[@id="login_btn_signin"]/button/span').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="authcode"]').send_keys(input('Steam Guard code:'))
driver.find_element_by_xpath('//*[@id="auth_buttonset_entercode"]/div[1]/div[1]').click()
sleep(3)
driver.find_element_by_xpath('//*[@id="success_continue_btn"]/div[1]').click()
sleep(1)
name = driver.find_element_by_xpath('//*[@id="global_header"]/div/div[2]/a[3]').text
driver.get(f'https://steamcommunity.com/id/{name}/games/?tab=all')
sleep(7)
rgGames = driver.execute_script('return rgGames')

keys = []
for game in rgGames:
    for key in game:
        if key not in keys:
            keys.append(key)

with open('games.csv','w',newline='') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=keys)
    writer.writeheader()
    for game in rgGames:
        try:
            writer.writerow(game)
        except:
            pass