import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# DANE TESTOWE
email = "abrakadabra@wp.pl"
firstname = "Kasia"
lastname = "Kowalska"
password = "abrakadabrA3?"
password2 = "abrakadabra"
street = "Konwaliowa"
number_street = "23"
number_house = "3"
city = "Bydgoszcz"
postcode = "85-005"
phone_number = "885678777"

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.aptekaolmed.pl")
        self.driver.implicitly_wait(3)

    def test1(self):

    # Kliknij "Zaloz Konto"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="base-btn btn-olmed-black"]'))).click()

    # Zaakceptuj polityke prywatnosci
        self.driver.find_element(By.XPATH, '//button[@class="cookie_box_close btn-orange w-100-mobile h-100 d-block mx-auto"]').click()

    # Wprowadz email
        email_input = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'username')))
        email_input.send_keys(email)

    # Wprowadz haslo
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.send_keys(password)

   # Potwierdz haslo
        password_confirm_input = self.driver.find_element(By.ID, 'password_confirmationation')
        password_confirm_input.send_keys(password2)
        password_confirm_input.location_once_scrolled_into_view

    # Wprowadz imie
        first_name_input = self.driver.find_element(By.ID, 'imie')
        first_name_input.send_keys(firstname)

    # Wprowadz nazwisko
        last_name_input = self.driver.find_element(By.ID, 'nazwisko')
        last_name_input.send_keys(lastname)

    # Wprowadz numer telefonu
        phone_number_input = self.driver.find_element(By.ID, 'telefon')
        phone_number_input.send_keys(phone_number)

    # Wprowadz ulice
        street_input = self.driver.find_element(By.ID, 'ulica')
        street_input.send_keys(street)

    # Wprowadz nr domu
        number_street_input = self.driver.find_element(By.ID, 'nrdomu')
        number_street_input.send_keys(number_street)

    # Wprowadz nr mieszkania
        number_house_input = self.driver.find_element(By.ID, 'nrmieszk')
        number_house_input.send_keys(number_street)

    # Wprowadz kod pocztowy
        post_code_input = self.driver.find_element(By.ID, 'kodpoczt')
        post_code_input.send_keys(postcode)

    # Wprowadz miejscowosc
        city_input = self.driver.find_element(By.ID, 'miejscowosc')
        city_input.send_keys(city)

    # Zaznacz wymagane zgody
        self.driver.find_element(By.ID, 'terms').click()
        self.driver.find_element(By.ID, 'terms1').click()

    # KLiknij 'Zarejestruj sie'
        self.driver.find_element(By.XPATH, '//button[@class="btn-no-style wide-orange mt-3"]').click()

        sleep(3)

        scroll_for_error = self.driver.find_element(By.XPATH, '//h2[@class="custom-header mb-4"]')
        scroll_for_error.location_once_scrolled_into_view

        sleep(10)

    # Sprawdz, czy jest tylko jedna informacja o bledzie
        error_messages = self.driver.find_elements(By.XPATH, '//div[@class="error mb-2 text-center text-danger"]')
        self.assertEqual(1, len(error_messages))

    # Sprawdz tresc informacji o bledzie
        error_info = self.driver.find_element(By.XPATH, '//div[@class="error mb-2 text-center text-danger"]').text
        print(error_info)

        self.assertEqual("Powtórzone hasło musi być identyczne!", error_info)



    def tearDown(self):
        self.driver.quit()