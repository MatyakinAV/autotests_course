# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

sbis_site = 'https://sbis.ru/'
driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get(sbis_site)
    assert driver.current_url == sbis_site, 'Не верно открыт сайт'  # проверяем что тот сайт который надо открылся
    assert driver.title == 'СБИС — экосистема для бизнеса: учет, управление и коммуникации', 'Не верный заголовок'  # Проверяем тайтл
    contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-link[href = "/contacts"]')
    assert contacts.text =='Контакты', 'Текст кнопки изменился'
    assert contacts.is_displayed(), 'Не отображается кнопка'
    assert contacts.get_attribute('title') == '', 'Тайтл изменился : был "" '
    contacts.click()
    sleep(2)
    logo_tensor = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__border-left--border-xm '
                                                       '.sbisru-Contacts__logo-tensor')
    assert logo_tensor.get_attribute('href') == 'https://tensor.ru/', 'Не верная ссылка на сайт, должно быть https://tensor.ru/'
    #  Нужно ли проверять что сменилась картинка? адрес хранения картинки
    # Переход на страницу Тензор.ру
    logo_tensor.click()
    sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    block_svl = driver.find_element(By.CSS_SELECTOR, '[class = "tensor_ru-Index__block4-content tensor_ru-Index__card"] '
                                                     '[class = "tensor_ru-Index__card-title tensor_ru-pb-16"]')  # Нашли блок Сила в людях
    assert block_svl.text == 'Сила в людях', ' Неправильный текст блока'
    assert block_svl.is_displayed(), ' Не видно блок'
    ssylka_podrobnee = driver.find_element(By.CSS_SELECTOR, '[class = "tensor_ru-Index__block4-content tensor_ru-Index__card"] [href="/about"]')
    ssylka_podrobnee.location_once_scrolled_into_view
    assert ssylka_podrobnee.get_attribute('href') == 'https://tensor.ru/about', 'Не верная ссылка на сайт'
    assert ssylka_podrobnee.text == 'Подробнее', 'Не верный текст'
    ssylka_podrobnee.click()
    sleep(5)
finally:
    driver.quit()
