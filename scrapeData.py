from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import re


def startDriver(profile):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--start-maximized --headless=new")
    driver = webdriver.Chrome(chromeOptions)
    driver.get(profile)
    # sleep(0.5)
    action = ActionChains(driver)
    action.send_keys(Keys.ESCAPE)
    action.perform()
    return driver


def getHTML(driver):
    soup = BeautifulSoup(driver.page_source, features="html.parser")
    return soup


def getName(soup):
    name = soup.find("h1", attrs={'class': 'leading-open'})
    if(name):
        name = name.text.strip()
        return name
    else:
        return -1
    

def getHeadline(soup):
    headline = soup.find('h2', attrs={'class': 'leading-open'})
    if(headline):
        headline = headline.text.strip()
        return headline
    else:
        return -1
    

def getAbt(soup):
    sectionAbt = soup.find('section', attrs={'class': 'summary'})
    if(sectionAbt):
        about = sectionAbt.find('p').text.strip()
        if(len(about)>3):
            return about
        else:
            return -1
    else:
        return -1


def getExp(soup):
    sectionExp = soup.find('section', attrs={'class': 'experience'})
    if(sectionExp):
        exp = sectionExp.find('ul', attrs={'class': 'experience__list'})
        text = exp.text
        text = re.sub(' +', ' ', text)
        text = re.sub('(\n){2}+', '', text)
        text = re.sub('( \n)+', '', text)
        text = re.sub('\n ', '\n', text)
        text = text.strip()
        return text
    else:
        return -1
    

def getEdu(soup):
    sectionEdu = soup.find('section', attrs={'class': 'education'})
    if(sectionEdu):
        edu = sectionEdu.find('ul', attrs={'class': 'education__list'})
        text = edu.text
        text = re.sub(' +\n +', ' \n', text)
        text = re.sub('(\n{2})+', '', text)
        text = re.sub('\n +', '', text)
        text = text.strip()
        return text
    else:
        return -1
    

def getCerti(soup):
    sectionCerti = soup.find('section', attrs={'class': 'certifications'})
    if(sectionCerti):
        certi = soup.find('ul', attrs={'class': 'certifications__list'})
        text = certi.text
        text = re.sub(' +', ' ', text)
        text = re.sub('(\n){2}+', '', text)
        text = re.sub('( \n)+', '', text)
        text = re.sub('\n  ', '\n', text)
        text = text.strip()
        return text
    else:
        return -1
    






