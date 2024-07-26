from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://www.italika.mx/modelos"

class Driver:
    # WEB DRIVER CONFIG
    def __init__(self):
        self.options = self.configure_browser_options()
        self.driver = self.start_browser()
        self.wait = WebDriverWait(self.driver, 9)

    def configure_browser_options(self):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--enable-logging")
        options.add_argument("--log-level=3")  # DISABLE LOGS
        options.add_argument("--incognito")
        options.add_argument("--disable-cache")
        options.add_argument("--disable-cookies")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        options.add_argument("--use-fake-ui-for-media-stream")
        options.add_argument("--disable-dev-shm-usage")

        return options

    def start_browser(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get(BASE_URL)
        return driver

    def get_data(self):
        try:
            
            XPATH = "/html/body/div[3]/div/div[1]/div/div[6]/div/div"

            data = []

            gen = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, XPATH))
            )

            soup = BeautifulSoup(gen.get_attribute("innerHTML"), 'html.parser')

            sections = soup.find_all(
                'div', class_='elektra-elektra-components-0-x-flexrow-mobile')

            for section in sections:

                title = section.find(
                    'h1', class_='elektra-elektra-components-0-x-section__content--title').text.strip()

                description = section.find(
                    'p', class_='elektra-elektra-components-0-x-section__content--text').text.strip()

                img_url = section.find(
                    'div', class_='elektra-elektra-components-0-x-section__image').find('img')['src']

                data.append({
                    'title': title,
                    'description': description,
                    'img_url': img_url
                })

            self.driver.quit()

            return data

        except Exception as e:
            self.driver.quit()
            print(f"Error: {e}")
            return None
