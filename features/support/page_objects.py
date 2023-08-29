from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException


LANDING_PAGE = "https://www.ornikar.com/assurance-auto"
MAX_WAIT_TIME = 10

class LandingPage:
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get(LANDING_PAGE)
        self.driver.maximize_window()
        cookie_banner = CookieBannerPage(self.driver)
        if cookie_banner.is_banner_visible():
            cookie_banner.click_accept_button()

    def clicks_main_cta(self):
        self.driver.find_element(By.XPATH, "//a[@text='CTA' and @class='button is-heroe w-button']").click()

    def clicks_secondary_cta(self):
        self.driver.find_element(By.XPATH, "//a[@text='CTA' and @class='button is-secondary-heroe key-exists w-button']").click()

class EstimationPage:
    def __init__(self, driver):
        self.driver = driver

    def clicks_yes_to_first_question(self):
        wait = WebDriverWait(self.driver, MAX_WAIT_TIME)
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Oui')]")))
        element.click()

    def checks_for_email_input(self):
        wait = WebDriverWait(self.driver, MAX_WAIT_TIME)
        input_email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))
        assert input_email.is_displayed(), "The email input is not visible on the page."
    
    def checks_for_search_by_plate(self):
        wait = WebDriverWait(self.driver, MAX_WAIT_TIME)
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Rechercher par plaque')]")))
        assert element.is_displayed(), "The search by plate field is not visible on the page."

class CookieBannerPage:
    def __init__(self, driver):
        self.driver = driver

    def is_banner_visible(self):
        try:
            banner = WebDriverWait(self.driver, MAX_WAIT_TIME).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Gestion des cookies')]"))
            )
            return True
        except:
            return False

    def click_accept_button(self):
        wait = WebDriverWait(self.driver, MAX_WAIT_TIME)
        accept_button = wait.until(EC.presence_of_element_located((By.ID, "axeptio_btn_acceptAll")))
        accept_button.click()