from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

#@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_language(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    #ожидание на всякий случай
    browser.implicitly_wait(5)

    #кладем товар в корзину
    button_reg = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    button_reg.click()

    #Проверяем, появилась ли кнопка корзины
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="btn btn-info"]')) )
    message = browser.find_element(By.CSS_SELECTOR, '[class="alertinner "]')

    #не до конца понял зачем тут assert, так как наличие кнопки само по себе проверяет заполнение корзины, но на всякий случай вот:
    assert "Coders at Work" in message.text
if __name__ == "__main__":
   pytest.main() 