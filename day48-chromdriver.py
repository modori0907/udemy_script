from selenium import webdriver
from selenium.webdriver.common.by import By

chrom_diver_path = "./chromedriver"
driver = webdriver.Chrome(executable_path=chrom_diver_path)


driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[1]/div[2]/p[2]/a')  # ”を'に変更した
# print(bug_link.texf)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")  # CSSセレクタでクラスを指定、指定したセレクタの中にタグ
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")  # CSSセレクタの中にあるliタグの中にあるaタグと範囲を狭める
events = {}

# 辞書を作成する
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)


# for name in event_names:
#     print(name.text)

# print(event_times)
# for time in event_times:
#     print(time.text)



driver.quit()