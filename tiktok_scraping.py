from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

def get_tiktok_profile_by_selenium(user_id):
    options = Options()
    options.add_argument('--headless')
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
