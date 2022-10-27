from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from urllib.request import urlopen


def test_count_selenium():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("http://selenium.dev")

    assert driver.title == 'Selenium'

    response = urlopen("http://selenium.dev")
    html = response.read().decode('utf-8')
    subs = 'Selenium'
    cnt = html.count(subs)
    print("Количество упоминаний 'Selenium':", cnt)

    driver.quit()

"""
def test_count_word_selenium():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("http://selenium.dev")

    count = driver.find_elements(By.XPATH, "//*[contains(text(), 'selenuim')]")
    count1 = driver.find_elements(By.XPATH, "//*[contains(text(), 'Selenium')]")
    count2 = len(count) + len(count1)

    assert count2 != 0, "Вхождений искомого слова не найдено."
    print('Успешно! Число вхождений "Selenium" -', count2)

    driver.quit()
"""