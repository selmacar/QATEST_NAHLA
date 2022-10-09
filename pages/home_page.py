from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)

    def go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def login(self, username, password):
        username_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_polje.clear()
        username_polje.click()
        username_polje.send_keys(username)
        password_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_polje.clear()
        password_polje.click()
        password_polje.send_keys(password)
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    def get_text(self):
        text_element=self.wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='title']")))
        return text_element.text

    def add_to_cart(self, ButtonID):
        self.wait.until(EC.element_to_be_clickable((By.ID, ButtonID))).click()

    def click(self, ElementID):
        self.wait.until(EC.element_to_be_clickable((By.ID, ElementID))).click()

    def get_text_item(self, itemID):
        item = self.driver.find_element(By.ID, itemID)
        return item.text

    def checkout(self, name, surname, postalCode):
        Ime = self.driver.find_element(By.ID, "first-name")
        Ime.click()
        Ime.send_keys(name)
        Prezime = self.driver.find_element(By.ID,"last-name")
        Prezime.click()
        Prezime.send_keys(surname)
        Postanski_broj = self.driver.find_element(By.ID, "postal-code")
        Postanski_broj.click()
        Postanski_broj.send_keys(postalCode)
   
    def check_login(self):
        assert self.wait.until(EC.visibility_of_element_located((By.ID, "root")))