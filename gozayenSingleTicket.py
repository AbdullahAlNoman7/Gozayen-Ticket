import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BimanTicket:

    def demo_ticket(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('https://www.gozayaan.com/')
        # one way select
        # driver.find_element(By.CSS_SELECTOR, '.flight-type-wrapper .radio:nth-of-type(1)').click()
        # confirm ticket
        click_input_from = driver.find_element(By.CSS_SELECTOR, '.box.from.location > .value')
        click_input_from.click()
        input_box_from = driver.find_elements(By.XPATH, "//div[@class='airport-suggestion']//div[@class='airport-list']//div//div[@class='airport-location']//div")
        print(len(input_box_from))
        for result in input_box_from:
            if result.text == "Cox's Bazar, Bangladesh":
                result.click()
                break
        click_input_to = driver.find_element(By.CSS_SELECTOR, '.box.has-swapper.location.to > .value')
        click_input_to.click()
        input_box_to = driver.find_elements(By.XPATH, "/html//div[@id='searchbar']//div["
                                                      "@class='airport-suggestion']//div[1]/div")
        print(len(input_box_to))
        for results in input_box_to:
            if results.text == "Dhaka, Bangladesh":
                results.click()
                break
        journy_date = driver.find_element(By.CSS_SELECTOR, '.flight-search div:nth-of-type(3) .value')
        journy_date.click()
        selct_date = driver.find_element(By.CSS_SELECTOR, '.calendar.left > .month > span:nth-of-type(16)')
        selct_date.click()
        travel_cls = driver.find_element(By.CSS_SELECTOR, '.box.traveler')
        travel_cls.click()
        # Economic class
        driver.find_element(By.CSS_SELECTOR, '.radio-container .brand-radio:nth-of-type(1) .text').click()
        driver.find_element(By.CSS_SELECTOR, '.btn.btn-secondary.picker-mb-btn').click()
        # search
        driver.find_element(By.XPATH, "//div[@id='searchbar']//button[@type='button']").click()
        # select ticekt

        wait = WebDriverWait(driver, 80)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@id='flight-list']/div[@class='container']/div[@class='row']/div["
                       "@class='col-lg-9']/div[2]/div[@class='flight-card']//button["
                       "@type='button']"))).click()
        # send user info
        scroll = driver.find_element(By.CSS_SELECTOR,".collapse.show > div > div:nth-of-type(1) > .col-12.mb-1 > "
                                                     ".font-weight-bolder.text-primary")
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        # driver.find_element(By.XPATH,'//*[@id="__BVID__521"]/div/span/div/div[1]/label/div/span').click()
        # mr.click
        driver.find_element(By.XPATH, "//span[normalize-space()='MR.']").click()
        # first name
        first_name = driver.find_element(By.ID, "first-name-0")
        first_name.send_keys("Mr")
        # last name
        last_name = driver.find_element(By.ID, "last-name-0")
        last_name.send_keys("Sagor")
        # email
        driver.find_element(By.ID, "email-0").send_keys('sagor@gmail.com')
        # phone number
        driver.find_element(By.ID, "phone-number-0").send_keys('01928595758')
        time.sleep(3)
        driver.find_element(By.ID, "bookButton").click()  # continue
        print("Test passed......")


tickt_obj = BimanTicket()
tickt_obj.demo_ticket()

