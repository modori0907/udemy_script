from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# ------- クロームドライバーを用意 ------ #
chrom_diver_path = "./chromedriver"
driver = webdriver.Chrome(executable_path=chrom_diver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# クリックする対象を取得
cookie = driver.find_element(By.ID, "cookie")

# 購入するとstoreが更新されるので、された後のストアの情報をに入手するしょり
# CSSセレクターで一覧を取得する
items = driver.find_elements(By.CSS_SELECTOR, "#store div")

# 内包処理　取得したオブジェクトをループで回す、取得したアイテムのidタグの中身をget_attibuteを利用して取得する
# idには各種アイテムを識別するための名称がついている
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5  # time.time() 現在の時刻に5秒を追加した物
five_min = time.time() + 60*5  # 5minutes

print("start")
while True:
    # まずは5秒間ボタンを押しまくる
    cookie.click()
    if time.time() > timeout:  # ボタンをおしまくる時間が5秒より長くなったら次の処理に進める

        # ID Storeの下にあるbタグの情報を取得する
        # そこには値段情報が入っている
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        # 値段を入れるリストを用意する
        item_prices = []

        # 値段を入れる処理
        for price in all_prices:
            # タグなどの情報を取り除きインナーテキストのみを取得する
            element_text = price.text
            if element_text != "":
                # 取り出す値は例えば、Cursor - 15なので編集が必要
                # split('-')でリストに変換　['Cursor ', ' 15']
                # strip()で余白( 15)を削除 15
                # replace(",","")は,があれば削除する処理
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # keyを値段、valueをアイテムにする辞書を作成
        cookie_upgrades = {}

        # ストアにある一覧の数を取り出す。range関数を利用して数分だけ繰り返し処理、nに引き渡すのは数字

        for n in range(len(item_prices)):
            # 値段とアイテム名を追加する
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # どれくらい稼いでいるチェックする処理
        money_element = driver.find_element(By.ID, "money").text
        # 取得する値例は217
        if "," in money_element:
            money_element = money_element.replace(",", "")
        # お金の処理
        cookie_count = int(money_element)

        # Find upgrades
        affortable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affortable_upgrades[cost] = id  # もし、クッキーの値段が商品の値段より大きかったら、値段と商品名の辞書

        # Purchase the most expensive affotable upgrade
        highest_price_affortable_upgrade = max(affortable_upgrades) # keyで一番値が大きいものを取り出す処理。つまり値段
        # print(highest_price_affortable_upgrade)
        to_purchase_id = affortable_upgrades[highest_price_affortable_upgrade]
        print(to_purchase_id) # idの値はうまく取得できてる　Grandmaで止まる

        """
        <selenium.webdriver.remote.webelement.WebElement (session="fd32ca9c3399c5160526714c9a621a0b", element="4d7a904e-9ae8-47c7-ab5a-20da01db0c85")>
        buyCursor
        <selenium.webdriver.remote.webelement.WebElement (session="fd32ca9c3399c5160526714c9a621a0b", element="9a8f2577-af4e-4b29-a199-015864d5a869")>
        buyGrandma
        """

        driver.find_element(By.ID, to_purchase_id).click()
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
