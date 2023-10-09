# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import string
import random
sbis_site = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()
#driver.maximize_window()
try:
    driver.get(sbis_site)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys('Игра', Keys.ENTER)
    assert login.get_attribute('Value') == 'Игра', 'Логин не отобразился в поле логин'
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys('Игра123', Keys.ENTER)
    assert password.get_attribute('Value') == 'Игра123', 'Пароль не отобразился в поле пароль'
    sleep(7)
    button_sms = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"] '
                                                     '[class="NavigationPanels-Accordion__title '
                                                      'NavigationPanels-Accordion__title_level-1"]')
    assert button_sms.text == 'Контакты', 'Не правильное наименование пункта Аккордеона'
    button_sms.click()
    sleep(1)
    button_sms = driver.find_element(By.CSS_SELECTOR, '[class="NavigationPanels-SubMenu__lvl-1 '
                                                      'NavigationPanels-SubMenu__item  '
                                                      'NavigationPanels-Accordion__prevent-default '
                                                      'NavigationPanels-SubMenu__item-withIcon  '
                                                      'NavigationPanels-SubMenu__item_hasAction ws-flex-grow-1"]')
    button_sms.click()
    sleep(3)
    # Открываем окно выбора сотрудника для отправки сообщения по кнопке +
    plus_but = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    assert plus_but.is_displayed(), 'Кнопка не отображается'
    plus_but.click()
    sleep(3)
    #  Ищем и выбираем сотрудника кому отправить
    okno_poiska = driver.find_element(By.CSS_SELECTOR, '[class="controls-Field js-controls-Field '
                                                       'controls-InputBase__nativeField '
                                                       'controls-Search__nativeField_caretEmpty '
                                                       'controls-Search__nativeField_caretEmpty_theme_default   '
                                                       'controls-InputBase__nativeField_hideCustomPlaceholder"]')
    okno_poiska.send_keys('Игрова Аня')
    sleep(2)
    #  Выбор сотрудника
    sotrudnik = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]')
    sotrudnik.click()
    #  Пишем сообщение и отправляем
    sleep(2)
    text_sms = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    S = 50
    text_message = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    text_sms.send_keys(text_message, Keys.CONTROL + Keys.ENTER)
    sleep(2)
    # разобрать какой класс правильно брать
    sms_open = driver.find_element(By.CSS_SELECTOR, '[class="msg-dialogs-item ws-flexbox ws-flex-column '
                                                    'msg-dialogs-item_unread msg-dialogs-item_unviewed"]')
    mes_split = sms_open.text.split('\n')[4]
    assert text_message == mes_split, 'Не отобразилось сообщение на первом месте'
    action_chains = ActionChains(driver)
    action_chains.move_to_element(sms_open).perform()
    del_sms = driver.find_element(By.CSS_SELECTOR, '[class="controls-Button__icon controls-BaseButton__icon '
                                                   'controls-icon_size-m controls-icon_style-danger controls-icon '
                                                   'icon-Erase"]')
    del_sms.click()
    # нужно ли проверять выпадашку что перемещено в корзину и если да , то тут надо вылавливатьк ак то ее?
    check_message_del = driver.find_elements(By.CSS_SELECTOR,
                                             '.msg-dialogs-detail__layout-content '
                                             '.controls-ListView__item_default .msg-entity-text')
    assert check_message_del[0].text != text_message, 'Первое сообщение осталось'
    sleep(2)
finally:
    driver.quit()