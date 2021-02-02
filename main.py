from selenium import webdriver
import time
import random
from config import username, password


class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self, email, password):
        self.driver.get('https://instagram.com/')
        time.sleep(7)

        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(email)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(password)

        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()

        time.sleep(5)

        # Deny save credentials and notifications
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div/div/button').click()

        time.sleep(3)

        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]').click()

        time.sleep(1)

        # Navigate to profile
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
        time.sleep(.5)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div').click()
        time.sleep(3)

        # Get following
        following_button = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
        time.sleep(.5)

        self.following = self.get_names()
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
        time.sleep(.5)

        # Get followers
        followers_button = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(.5)

        self.followers = self.get_names()
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
        time.sleep(.5)

        # Find not following back
        self.not_following_back = [
            user for user in self.following if user not in self.followers]

        print("unfollowing:")
        for uname in self.not_following_back:
            print('>\t', uname)
            self.unfollow(uname)

        print("DONE")
        self.driver.get('https://instagram.com')

    def unfollow(self, uname):
        # Open search bar, input uname and click first
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div/span[2]').click()
        time.sleep(.5)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(uname)
        time.sleep(1)
        results = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[4]/div')
        results.find_elements_by_tag_name('a')[0].click()
        time.sleep(5)

        # Click unfollow and confirm
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[1]').click()

    def get_names(self):
        unames = []
        SCROLL_PAUSE_TIME = .7
        xpath = "/html/body/div[4]/div/div/div[2]"
        scrollbox = self.driver.find_element_by_xpath(xpath)

        # Get scroll height
        last_height = self.driver.execute_script(
            "return arguments[0].scrollHeight", scrollbox)

        while True:
            # Scroll down to bottom
            self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scrollbox)

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script(
                "return arguments[0].scrollHeight", scrollbox)
            if new_height == last_height:
                break
            last_height = new_height

        results = bot.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[2]')
        unames = [a.text for a in results.find_elements_by_tag_name(
            'a') if a.text != '']

        return unames


bot = Bot()
bot.login(username, password)
