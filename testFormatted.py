from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


path = "/users/sevapopov/стажировка/chromedriver"
browser = webdriver.Chrome(path)
def fetchHtmlForThePage(url, delay, block_name):
    options = Options()
    options.add_argument('--headless')
    browser.get(url)
    try:
        element_present = EC.presence_of_element_located((By.ID, block_name))
        WebDriverWait(browser, delay).until(element_present)
    except TimeoutException:
        print("Loading took too much time!")
    html = browser.page_source
    return html
eventsinfo = []
def russia_running():
    page = fetchHtmlForThePage("https://russiarunning.com/events", 5, 'event-info')
    bsObj = BeautifulSoup(page, 'html.parser')
    sportevents = bsObj.find_all('div', class_='event-info')
    title = " "
    location = " "
    date = " "
    race = " "
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
        #if titles != None and locations != None and dates != None and races != None:
        eventsinfo.append(title)
        eventsinfo.append(location)
        eventsinfo.append(date)
        eventsinfo.append(race)
def reg_place():
    browser.get("https://reg.place")
    time.sleep(3)
    clickCount = 0
    try:
        while clickCount < 10:
            browser.find_element_by_link_text('ЗАГРУЗИТЬ ЕЩЕ').click()
            time.sleep(1)
    except Exception:
        print(Exception)
    sportevents = browser.find_elements_by_class_name("inner")
    title = " "
    date = " "
    for sportevent in sportevents:
        titles = sportevent.find_element_by_class_name('title')
        if titles is not None:
            title = titles.text.strip()
            print(title)
        dates = sportevent.find_element_by_class_name('date')
        if dates is not None:
            date = dates.text
            print(date)

        #if titles is not None and dates is not None:
        eventsinfo.append(title)
        eventsinfo.append(" ")
        eventsinfo.append(date)
        eventsinfo.append(" ")
def tri_life():
    page = fetchHtmlForThePage("https://www.trilife.ru/events/", 5, 'article-wrapper')
    bsObj = BeautifulSoup(page, 'html.parser')
    sportevents = bsObj.find_all('div', class_='article-wrapper')
    title = " "
    location = " "
    date = " "
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
        #if titles != None and locations != None and dates != None:
        eventsinfo.append(title)
        eventsinfo.append(location)
        eventsinfo.append(date)
        eventsinfo.append(" ")
def iron_star():
    page = fetchHtmlForThePage("https://iron-star.com", 5, 'row')
    bsObj = BeautifulSoup(page, 'html.parser')
    sportevents = bsObj.find_all('div', class_='event-item-wrap')
    title = " "
    location = " "
    date = " "
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
        #if titles != None and locations != None and dates != None:
        eventsinfo.append(title)
        eventsinfo.append(location)
        eventsinfo.append(date)
        eventsinfo.append(" ")
with open('data.csv', 'w', encoding='utf-16', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter = '\t')
    russia_running()
    reg_place()
    tri_life()
    iron_star()
    eventsinfofiltered = []
    eventsinfofilteredobjects = []
    objects_count = 0
    for i in eventsinfo:
        if i in eventsinfofiltered:
            continue
        eventsinfofiltered.append([i])
#    eventsinfo = sorted(set(eventsinfo))
    for i in eventsinfofiltered:
        eventsinfofilteredobjects.append(i)
        objects_count = objects_count + 1
        if objects_count == 4:
            replacedList = []
            for j in eventsinfofilteredobjects:
                replacedList.append(j[0].replace("\n", " "))
            #writer.writerow(eventsinfofilteredobjects)
            eventsinfofilteredobjects.clear()
            objects_count = 0
            writer.writerow(replacedList)
    browser.quit()

