from selenium import webdriver
import os
import time
from selenium.common.exceptions import NoSuchElementException


def perform_click(url):
    path = os.path.join(os.getcwd(),'geckodriver.exe')
    driver = webdriver.Firefox(executable_path=path)
    driver.get(url)
    try:
        click = driver.find_element_by_class_name('tag-name')
        click.click()
        time.sleep(3)
    except NoSuchElementException:
        driver.quit()
        print("This URL doesn't have any offers listed")
        return
    offers = get_offer(driver)
    print_offers(offers,url)
    driver.close()
    return

def get_offer(driver):
    try:
        driver.find_element_by_class_name('discont')
        offers = driver.find_elements_by_class_name('condition')
        time.sleep(1)
        return offers
    except NoSuchElementException:
        offer = driver.find_element_by_class_name('tag-name')
        offers = []
        offers.append(offer)
        return offers

def print_offers(offers,url):
    print('Provided URL :--- ' + url + '\n' )
    print('********************** Offers ********************************')
    for offer in offers:
        print(offer.text)
    print('********************** Thank you *****************************\n')
    
if __name__ == '__main__':
    url = input('Enter the URL here : - ')
    perform_click(url)
    user_input = input("Press enter to exit ")
