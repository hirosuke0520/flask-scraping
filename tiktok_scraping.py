from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def get_tiktok_profile_by_selenium(user_id):

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    # options.add_argument('--disable-dev-shm-usage')
    # service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome(options=options)

    url = f"https://www.tiktok.com/@{user_id}"
    driver.get(url)
    driver.implicitly_wait(30)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    profile_info = {
        "userId": user_id,
        "userSubtitle": get_text_from_elements(soup, "data-e2e", "user-subtitle"),
        "followersCount": get_text_from_elements(soup, "data-e2e", "followers-count"),
        "likesCount": get_text_from_elements(soup, "data-e2e", "likes-count"),
    }

    driver.quit()  
    return profile_info

def get_text_from_elements(soup:BeautifulSoup, attr_name, attr_value):
    elements = soup.find_all(attrs={attr_name: attr_value})
    if isinstance(elements, list) and elements:
        return elements[0].text
    else:
        return ""
