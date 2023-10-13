from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests, json


def scrape_data_from_web_page(url, fields_data) -> {}:
    options = Options()
    options.headless = True
    options.add_argument('--headless=new')

    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)
    driver.implicitly_wait(60)

    soup = BeautifulSoup(driver.page_source, 'html5lib')
    # soup.find('p', attrs={"class": "text-lg font-bold text-black"})

    response = {}
    for field_id, tags_array in fields_data.items():
        tag = soup
        for tag_query_data in tags_array:
            if not tag:
                break

            attrs = {}
            if "class" in tag_query_data:
                attrs["class"] = tag_query_data.get("class")
            if "id" in tag_query_data:
                attrs["id"] = tag_query_data.get("id")
            tag = tag.find(tag_query_data.get("tag"), attrs=attrs)

        if tag:
            response[field_id] = tag.text.strip()

    return response


def get_json_data(url) -> (str, bool, str):
    try:
        response = requests.request("GET", url, timeout=2)
        if response.status_code != 200:
            return None, False, "Got non 2xx response: {}".format(response.status_code)

        return json.loads(response.text), False, response.status_code
    except Exception as e:
        print("Get data failed for {}, error: {}".format(url, e))
        return None, True, 500
