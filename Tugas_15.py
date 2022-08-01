import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self):    
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    
    def test_a_failed_login_with_empty_username_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol log in
        time.sleep(3)

        # validasi
        response_message = browser.find_element(By.XPATH,"//*/div/form/div[3]").text
        self.assertEqual(response_message, 'Epic sadface: Username is required')    
  
    def test_b_failed_login_with_empty_username(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol log in
        time.sleep(3)

        # validasi
        response_message = browser.find_element(By.XPATH,"//*/div/form/div[3]").text
        self.assertEqual(response_message, 'Epic sadface: Username is required')    

    def test_c_failed_login_with_empty_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("problem_user") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol log in
        time.sleep(3)

        # validasi
        response_message = browser.find_element(By.XPATH,"//*/div/form/div[3]").text
        self.assertEqual(response_message, 'Epic sadface: Password is required')

    def test_d_failed_login_with_wrong_username(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("septiana") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol log in
        time.sleep(3)

        # validasi
        response_message = browser.find_element(By.XPATH,"//*/div/form/div[3]").text
        self.assertEqual(response_message, 'Epic sadface: Username and password do not match any user in this service')

    def test_e_failed_login_with_wrong_username_and_wrong_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("septiana") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("123456") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol log in
        time.sleep(3)

        # validasi
        response_message = browser.find_element(By.XPATH,"//*/div/form/div[3]").text
        self.assertEqual(response_message, 'Epic sadface: Username and password do not match any user in this service')
  
    def test_f_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("problem_user") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol log in
        time.sleep(3)
 
        # validasi
        response_data = browser.get("https://www.saucedemo.com/inventory.html")

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()