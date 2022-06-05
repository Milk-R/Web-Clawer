import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #move_to_element

#設定driver
path = 'C:\\Users\\zxc88\\Desktop\\Desktop\\Python\\chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get('https://shopee.tw/') #到蝦皮網址

time.sleep(1)

#輸入要搜尋的商品
print('輸入商品名稱：')
item = str(input())

#關閉廣告
ads_btn = driver.find_element_by_css_selector('div.shopee-popup__close-btn')
ads_btn.click()

#搜尋商品
t_field = driver.find_element_by_css_selector('input.shopee-searchbar-input__input') #搜尋欄
t_field.send_keys(item)
time.sleep(1)
t_btn = driver.find_element_by_css_selector('button.btn.btn-solid-primary.btn--s.btn--inline') #搜尋按鈕
t_btn.click()

#抓資料
time.sleep(3)
index = 0 #第幾個商品

while(1):
    try:
        product = driver.find_elements_by_css_selector('div.fBhek2._2xt0JJ')[index] #視窗內的第index個商品
        ActionChains(driver).move_to_element(product).perform() #移動到元素位置
        
        product_name = product.find_element_by_css_selector('div.yQmmFK._1POlWt._36CEnF').text
        product_price = product.find_element_by_css_selector('div._32hnQt').text
        product_price_r = product_price.split('\n')

        print(product_name)
        if(len(product_price_r) == 1):
            print(product_price_r[0], end='\n\n')
        else:
            print(product_price_r[0] + '-' + product_price_r[1], end='\n\n')

        time.sleep(0.1)
        index += 1
    except IndexError:
        break