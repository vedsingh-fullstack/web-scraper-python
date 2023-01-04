import requests
from db.init_db import get_database
from bs4 import BeautifulSoup
 
BASE_URL = "https://www.urparts.com"


def get_container_list(url: str, container_class_name: str):
    list = {}

    item_page = requests.get(f'{BASE_URL}/{url}')
    item_soup = BeautifulSoup(item_page.content, "html.parser")
    container = item_soup.find('div', {"class": container_class_name})

    if container is not None:
        list = container.find_all("li")
    
    return list


def fetch_item_list(url:str, container_class_name:str):
    item_list = {}
    container_list = get_container_list(url, container_class_name)

    for l in container_list:
        link = l.find('a', href=True)
        item_list[link.text.strip()] = link['href'].replace(' ', '%20')
    
    return item_list


def get_parts(url: str, container_class_name: str):
    parts_list = {}
    container_list = get_container_list(url, container_class_name)

    for l in container_list:
        link = l.find('a', href=True)
        if link.span is not None:
            parts_list[link.text.replace('-', '').split()[0]] = link.text.replace('-', '').split()[1]

    return parts_list
     
def save_catalogue(data):
    try:
        db = get_database()
        catalogues = db.catalogues
        catalogues.insert_many(data)
    except Exception as e:
        print(f"Something went wrong{e}") # add logger error instead of print
        # add logic for max retry
        
