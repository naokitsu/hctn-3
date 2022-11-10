from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import sys
import re
import string

def main():
    """
    Точка входа
    """
    driver = webdriver.Firefox()
    if len(sys.argv) != 2:
        print("Передайте страницу первым аргуметом")
        return
    driver.get(sys.argv[1])

    clean = re.compile('<.*?>')
    remove_spaces = re.compile('[ ,\n,\t]+')

    text = driver.page_source   # Скачаем страницу
    text = re.sub(remove_spaces, ' ', re.sub(clean, ' ', text)) # Уберем теги и лишние пробелы
    text = text.translate(str.maketrans('', '', string.punctuation)).lower().split() # убираем пунктуацию, переводим в строчные, делим на слова

    difference = 0
    left = ['я', 'меня', 'мне', 'мной', 'мною', 'мы', 'нас', 'нам', 'нами']
    right = ['ты', 'тебя', 'тебе', 'тобой', 'тобою',  'вы', 'вас', 'вам', 'вами', 'вас', 'он', 'ему', 'нём', 'его', 'она', 'её', 'ней', 'ей,', 'ею', 'оно', 'они', 'нас', 'них', 'их', 'им', 'ими']

    for i in text:
        if i in left:
            difference -= 1
        elif i in right:
            difference += 1

    if i < 0:
        print("Личных местоимений 1-го лица больше")
    elif i > 0:
        print("Личных местоимений 1-го лица меньше")
    else:
        print("Количество местоимений 1-го лица равно кол-ву местоимений других лиц")

    driver.quit()

if __name__ == '__main__':
    main()
