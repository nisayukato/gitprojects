from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.instagram.com/')
time.sleep(10)
#signing in
browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys()
browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys()
browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
time.sleep(30)
#passing the insta messages
browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
time.sleep(10)
#searching for users
users = [....]

for user in users :

    try :

        browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input').clear()
        browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(user)
        time.sleep(6)
        browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/a/div').click()
        time.sleep(15)
    except Exception :
        print('there is a problem in searching for {}'.format(user))
    try :
        browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input').clear()
        browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/button').click()
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]').click()
        time.sleep(2)
    except Exception :
        print('could not unfollow {}'.format(user))
for account in users :
    try :
        time.sleep(5)
        browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/button').click()
        browser.back()
    except Exception :
        print("couldn't follow {}".format(account))
        browser.back()
