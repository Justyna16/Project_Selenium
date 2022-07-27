import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

# DANE TESTOWE
produkt_1 = "vigantol"
produkt_2 = "ceviforte"


class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.aptekaolmed.pl")
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//button[@class="cookie_box_close btn-orange w-100-mobile h-100 d-block mx-auto"]').click()

    def test1(self):

    # Wyszukaj produkt
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'sample2'))).send_keys(produkt_1)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'sample2'))).send_keys(Keys.ENTER)

    # Znajdz odpowiedni produkt
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//img[@src="https://www.aptekaolmed.pl/produkty_zdjecia/vigantol-krople-20-000-jmmg-10-ml.jpg?ver=1622114944"]'))).location_once_scrolled_into_view

        sleep(3)

    # Zmien ilosc produktu
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@field="qty55535"][@class="qtyplus btn-no-style"]'))).click()

    # Dodaj produkt do koszyka
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product-listing-blade"]/div[1]/div[3]/div/div[2]/button'))).click()

        sleep(5)

    # Wyszukaj kolejny produkt
        self.driver.find_element(By.ID, 'sample2').send_keys(produkt_2)
        self.driver.find_element(By.ID, 'sample2').send_keys(Keys.ENTER)

    # Znajdz odpowiedni produkt
        self.driver.find_element(By.XPATH, '//img[@src="https://www.aptekaolmed.pl/produkty_zdjecia/ceviforte-max-30kaps.jpg?ver=1634380833"]').location_once_scrolled_into_view

        sleep(3)

    # Dodaj produkt do koszyka
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product-listing-blade"]/div[1]/div[3]/div/div[2]/button'))).click()

        sleep(5)

    # Otworz koszyk
        self.driver.find_element(By.ID, 'dropdown-cart-click').click()

        sleep(5)

    # Sprawdz czy ilosc produktow zgadza sie
        sprawdzam_koszyk = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//span[@style="font-weight: normal;"]'))).get_attribute("innerText")
        self.assertEqual(str(3), sprawdzam_koszyk[1])

        print("Ilość produktów w koszyku: ", sprawdzam_koszyk)

        sleep(5)



    def tearDown(self):
        self.driver.quit()


