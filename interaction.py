from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrom_diver_path = "./chromedriver"
driver = webdriver.Chrome(executable_path=chrom_diver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Atsuyuki")

Last_name = driver.find_element(By.NAME, "lName")
Last_name.send_keys("Suzuki")

Email_address = driver.find_element(By.NAME, "email")
Email_address.send_keys("test@test.co.jp")

SignUP_Button = driver.find_element(By.CLASS_NAME, "btn-block")
SignUP_Button.click()


# driver.get("https://ja.wikipedia.org/wiki/Main_Page")
# # article_count = driver.find_element(By.CSS_SELECTOR, "#number a")
# # # print(article_count.text)
# # all_portals = driver.find_element(By.LINK_TEXT, "記事")
# # all_portals.click()
#
# # search_click = driver.find_element(By.CLASS_NAME, "mw-ui-button mw-ui-quiet mw-ui-icon mw-ui-icon-element mw-ui-icon-wikimedia-search search-toggle")
# # search_click.click()
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
#
