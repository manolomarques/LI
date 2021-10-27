import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test_LI_teste_2():
    def setup_method(self, method):
        self.driver = webdriver.Chrome('drivers/chrome/94/chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.vars = {}

    #def teardown_method(self, method):
     #   self.driver.quit()


    def test_23(self):
        self.driver.get("https://qastoredesafio.lojaintegrada.com.br")
        self.driver.find_element(By.LINK_TEXT, "Ver mais").click()
        self.driver.find_element(By.LINK_TEXT, "Comprar").click()
        self.driver.find_element(By.ID, "usarCupom").click()
        self.driver.find_element(By.ID, "usarCupom").send_keys("10OFF")
        self.driver.find_element(By.ID, "usarCupom").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, ".total").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".valor-total").text == "R$ 135,70"
        self.driver.find_element(By.CSS_SELECTOR, ".grande").click()
        self.driver.find_element(By.ID, "id_email_login").click()
        self.driver.find_element(By.ID, "id_email_login").send_keys("mfmfel@gmail.com")
        self.driver.find_element(By.LINK_TEXT, "Continuar").click()

    def test_24(self):
        self.driver.get("https://qastoredesafio.lojaintegrada.com.br/")
        self.driver.find_element(By.LINK_TEXT, "Ver mais").click()
        self.driver.find_element(By.LINK_TEXT, "Comprar").click()
        self.driver.find_element(By.ID, "usarCupom").click()
        self.driver.find_element(By.ID, "usarCupom").send_keys("30REAIS")
        self.driver.find_element(By.ID, "usarCupom").send_keys(Keys.ENTER)
        assert self.driver.find_element(By.CSS_SELECTOR, ".valor-total").text == "R$ 105,60"
        self.driver.find_element(By.CSS_SELECTOR, ".grande").click()
        self.driver.find_element(By.ID, "id_email_login").click()
        self.driver.find_element(By.ID, "id_email_login").send_keys("mfmfel@gmail.com")
        self.driver.find_element(By.LINK_TEXT, "Continuar").click()

     def test_25(self):
        self.driver.get("https://qastoredesafio.lojaintegrada.com.br")
        self.driver.find_element(By.LINK_TEXT, "Ver mais").click()
        self.driver.find_element(By.LINK_TEXT, "Comprar").click()
        self.driver.find_element(By.CSS_SELECTOR, "#formCalcularFrete .cor-secundaria").click()
        self.driver.find_element(By.ID, "calcularFrete").send_keys("85817-210")
        self.driver.find_element(By.ID, "calcularFrete").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".bg-dark:nth-child(4) .cor-secundaria").click()
        self.driver.find_element(By.ID, "usarCupom").send_keys("30REAIS")
        self.driver.find_element(By.ID, "usarCupom").send_keys(Keys.ENTER)
        assert self.driver.find_element(By.CSS_SELECTOR, ".valor-total").text == "R$ 105,60"
        self.driver.find_element(By.CSS_SELECTOR, ".grande").click()
        self.driver.find_element(By.ID, "id_email_login").click()
        self.driver.find_element(By.ID, "id_email_login").send_keys("mfmfel@gmail.com")
        self.driver.find_element(By.LINK_TEXT, "Continuar").click()
        element = self.driver.find_element(By.LINK_TEXT, "Continuar")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()