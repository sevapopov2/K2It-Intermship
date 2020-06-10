from urllib.request import urlopen

from bs4 import BeautifulSoup

import csv

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options


def fetchHtmlForThePage(url, delay, block_name):

    options = Options()
    options.add_argument('--headless')

    path = "/users/sevapopov/стажировка/chromedriver"

    browser = webdriver.Chrome(path)

    browser.get(url)

    try:

        element_present = EC.presence_of_element_located((By.ID, block_name))

        WebDriverWait(browser, delay).until(element_present)

    except TimeoutException:

        print("Loading took too much time!")

    html = browser.page_source

    browser.quit()

    return html


def russia_running():

    page = fetchHtmlForThePage("https://russiarunning.com/events", 5,
                               'event-info')

    bsObj = BeautifulSoup(page, 'html.parser')

    sportevents = bsObj.find_all('div', class_='event-info')

    title = ''

    location = ''

    date = ''

    race = ''
    for sportevent in sportevents:

        titles = sportevent.find('a', class_='ellipsis')

        if titles != None:

            title = titles.text.strip()

            print(title)

        locations = sportevent.find('span', class_='place')

        if locations != None:

            location = locations.text

            print(location)

        dates = sportevent.find('div', class_='date')

        if dates != None:

            date = dates.text

            print(date)
        races = sportevent.find('span', class_='race-event-item')

        if races != None:
            race = races.text

            print(race)

        writer.writerow([title, location, date, race])


def reg_place():
    page = fetchHtmlForThePage("https://reg.place", 5, 'inner')

    bsObj = BeautifulSoup(page, 'html.parser')

    sportevents = bsObj.find_all('div', class_='inner')

    title = ''

    location = ''

    date = ''

    race = ''

    for sportevent in sportevents:

        titles = sportevent.find('div', class_='title')

        if titles != None:

            title = titles.text.strip()

            print(title)

        dates = sportevent.find('div', class_='date')

        if dates != None:

            date = dates.text

            print(date)
        writer.writerow([title, date])


def tri_life():
    page = fetchHtmlForThePage("https://www.trilife.ru/events/", 5,
                               'article-wrapper')

    bsObj = BeautifulSoup(page, 'html.parser')

    sportevents = bsObj.find_all('div', class_='article-wrapper')

    title = ''

    location = ''

    date = ''

    race = ''

    for sportevent in sportevents:

        titles = sportevent.find('span', class_='summary hide')

        if titles != None:

            title = titles.text.strip()

            print(title)

        locations = sportevent.find('span', class_='location')

        if locations != None:

            location = locations.text

            print(location)

        dates = sportevent.find('div', class_='pseudo-td')

        if dates != None:

            date = dates.text

            print(date)
        writer.writerow([title, location, date])


def iron_star():
    page = fetchHtmlForThePage("https://iron-star.com", 5, 'row')

    bsObj = BeautifulSoup(page, 'html.parser')

    sportevents = bsObj.find_all('div', class_='event-item-wrap')

    title = ''

    location = ''

    date = ''

    for sportevent in sportevents:

        titles = sportevent.find('div', class_='title')

        if titles != None:

            title = titles.text.strip()

            print(title)

        locations = sportevent.find('div', class_='place')

        if locations != None:

            location = locations.text

            print(location)

        dates = sportevent.find('div', class_='date')

        if dates != None:

            date = dates.text

            print(date)
        writer.writerow([title, location, date])


with open('data.csv', 'w', newline='', encoding='utf-16') as csvfile:

    writer = csv.writer(csvfile, delimiter='	', quotechar='|')
    russia_running()

    reg_place()
    tri_life()
    iron_star()
