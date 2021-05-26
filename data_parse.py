"""
python file to parse data to send
"""

from selenium import webdriver

driver = webdriver.Chrome('/Users/yk/PycharmProjects/inpyeon bot/chromedriver')

driver.get('https://trends.google.com/trends/trendingsearches/daily?geo=KR')
