from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username;
        self.password = password;
        self.bot = webdriver.Chrome();


    def login(self):
        bot = self.bot;
        bot.get('https://twitter.com');
        time.sleep(3);
        login = bot.find_element_by_class_name('StaticLoggedOutHomePage-buttonLogin');
        login.click();
        email = bot.find_element_by_name('session[username_or_email]');
        password = bot.find_element_by_name('session[password]');
        email.clear();
        password.clear();
        email.send_keys(self.username);
        password.send_keys(self.password);
        password.send_keys(Keys.RETURN);
        time.sleep(3);

    def LikeTweets(self, hashtag):
        bot = self.bot;
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd');
        time.sleep(3);
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2);
            tweets = bot.find_element_by_class_name('tweet');
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:
                bot.get("https://twitter.com" + link);
                try:
                    bot.find_element_by_class_name("HeartAnimation");
                    time.sleep(10);
                except Exception as x:
                    time.sleep(1);




hussein = TwitterBot('email@hotmail.com', "password123");
hussein.login();
hussein.LikeTweets('webdevelopment');
