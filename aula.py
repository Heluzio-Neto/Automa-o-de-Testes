from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = Firefox()
browser.maximize_window()
url = 'http://automationpractice.com/'
browser.get(url)
sleep(5)

element = browser.find_element(By.ID,'search_query_top')
element.send_keys("Dress")
element.submit()

sleep(5)
find_returns = browser.find_element(By.CLASS_NAME,'product-count') 
print(find_returns.text)

# alert = browser.find_element(By.CLASS_NAME,'alert alert-warning')
# if(alert):
#     print("nenhum item encontrado")
# else:
#     print("Encontrado")
# try:
#     mensagem = browser.find_element(
#     By.XPATH, '/html/body/div/div[2]/div/div[3]/div[2]/p')
    
# except:
#     print("Sucess")


# element = browser.find_element(By.CLASS_NAME,'header_user_info')
# element.click()

# element = browser.find_element(By.ID,'email_create')
# element.send_keys("teste@gmail.com")

# element = browser.find_element(By.ID,'SubmitCreate')
# element.click()

# element = browser.find_element(By.ID,'email')
# element.send_keys("teste@gmail.com")

# element = browser.find_element(By.ID,'passwd')
# element.send_keys("123456")

# element = browser.find_element(By.ID,'SubmitLogin')
# element.click()

# element = browser.find_element(
#      By.XPATH, '//*[@id="search_query_top"]')
# element.send_keys("Teste")

# continue_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'order')
# print(continue_link.text)
# continue_link.click()

# list_links = browser.find_elements(By.PARTIAL_LINK_TEXT, 'My')
# for link in list_links:
#     print(link.text)

