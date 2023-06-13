# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

sbis_site = 'https://sbis.ru/'
sbis_tensor = 'https://tensor.ru/'
driver = webdriver.Chrome()
try:
    #  Заходим на сайт 'https://sbis.ru/'
    driver.get(sbis_site)
    driver.maximize_window()
    assert driver.current_url == sbis_site, 'Не верно открыт сайт'

    #  Переходим по кнопке Контакты
    contact_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href = "/contacts"]')
    assert contact_btn.text == 'Контакты', 'Неправильный текст кнопки'
    assert contact_btn.is_displayed(), 'Кнопка не отображается'
    contact_btn.click()
    time.sleep(3)

    #  Смотрим логотип Тензор и переходим по нему
    tensor_btn = driver.find_element(By.CSS_SELECTOR, '[class="sbisru-Contacts__logo-tensor mb-8"]')
    assert tensor_btn.is_displayed(), 'Кнопка не отображается'
    time.sleep(3)
    tensor_btn.click()

    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == sbis_tensor, 'Не верно открыт сайт'

    #  Смотрим блок Сила в людях и переходим по нему
    time.sleep(3)
    news_btn = driver.find_element(By.CSS_SELECTOR, '[class="s-Grid-col s-Grid-col--6 s-Grid-col--sm12"] ' 
                                                    '[class="tensor_ru-Index__card-title tensor_ru-pb-16"]')
    assert news_btn.text == 'Сила в людях', 'Нет заголовка "Сила в людях"'
    assert news_btn.is_displayed(), 'Новость не отображается'

    news_btn_about = driver.find_element(By.CSS_SELECTOR, '[class="s-Grid-col s-Grid-col--6 s-Grid-col--sm12"] '
                                                          '[class="tensor_ru-link tensor_ru-Index__link"]')
    news_btn_about.location_once_scrolled_into_view
    assert news_btn_about.text == 'Подробнее', 'Не правильный текст, нужно чтобы был :  "Подробнее"'
    news_btn_about.click()
    time.sleep(3)
    assert driver.current_url == "https://tensor.ru/about", 'не тот сайт открыт'
finally:
    driver.quit()
