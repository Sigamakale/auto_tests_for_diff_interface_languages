from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_basket_button_exists(browser):
    browser.get(link)
    #time.sleep(10)
    btn = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert btn, 'Страница не содержит кнопку добавления в корзину'
