from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import lxml
import requests

obmen = int(input("Введите количество гривен, которые нужно конвертировать, после нажмите Enter: "))
counter = 0
counter3 = 1

def run(playwright):
    page = playwright.chromium.launch(headless=False).new_page()
    page.goto('https://bank.gov.ua')

    soup = BeautifulSoup(page.content(), 'lxml')


    for dollar in soup.select('.value-full '):
        global counter3
        counter2 = counter
        counter2 += 1
        if counter2 == 1:
            print("Количество Евро")
        if counter3 == 2:
            print("Количество Долларов США")
        value = dollar.select_one('small').text
        value = value.replace(",", ".")
        value2 = float(value)
        result = (obmen / value2)
        print(round(result, 2))
        counter3 += 1

'''print("Количество Евро")
print("Количество Долларов США")'''

with sync_playwright() as playwright:
    run(playwright)



'''counter = 2
        if counter == 2:
            print("Количество Долларов США")

counter = 1
    if counter == 1:
        print("Количество Евро")'''



'''for dollar in soup.select('value-full '):
    value = dollar.select_one('small').float
    #value = dollar.select_one('value-full ').get('small')
    print (value)'''
#value = dollar.select_one('value-full ').get('small')