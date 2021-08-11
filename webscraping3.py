from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')
time.sleep(10)
#signing in
browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys('your user name or email')
browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys('your password')
time.sleep(3)
browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()
time.sleep(10)
#passing the insta messages
browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
time.sleep(10)
browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
time .sleep(3)
#the list of the celebrities users you want
users = ['kimkardashian','leomessi','cristiano','psg','fcbarcelona','neymarjr']
#unfollowig the users
for user in users :
#searching for users from the list
    try :
        browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(user)
        time.sleep(4.5)
        browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()
        time.sleep(20)
    except Exception :
        print('there is a problem in searching for '+ user)
#unfollowing the users 
    try :
        browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button/div/span').click()
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
        time.sleep(2)
    except Exception :
        print('could not unfollow {}'.format(user))
#following the users
for account in users :
    try :
        time.sleep(20)
        browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button').click()
        browser.back()
    except Exception :
        print("couldn't follow {}".format(account))
        browser.back()

