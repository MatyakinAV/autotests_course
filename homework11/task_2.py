# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

sbis_site = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()
try:
    # Открываем и авторизуемся
    driver.get(sbis_site)
    driver.maximize_window()
    time.sleep(3)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.is_displayed(), 'не отображается ввод логина'

    login.send_keys('кабинет600', Keys.ENTER)
    assert login.get_attribute('value') == 'кабинет600', 'не получился ввод'

    time.sleep(3)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    login.is_displayed(), 'не отображается ввод пароля'

    password.send_keys('кабинет6000', Keys.ENTER)
    assert password.get_attribute('value') == 'кабинет6000', 'не получился ввод'

    #  Открываем контакты и диалог выбора сотрудника
    time.sleep(8)
    contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]')
    contacts.click()

    time.sleep(3)
    contacts_sub = driver.find_element(By.CSS_SELECTOR, '[name="headTitle"]')
    contacts_sub.click()

    time.sleep(3)
    message = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]')
    message.click()

    time.sleep(3)

    #  Выбираем сотрудника и отправем сообщение
    message_person = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-Render__field"] .controls-Field')
    message_person.send_keys('Василенко Вячеслав', Keys.ENTER)
    time.sleep(2)
    my_person = driver.find_element(By.CSS_SELECTOR, '[class="msg-addressee-selector__addressee"][tabindex="0"]')
    my_person.click()

    time.sleep(2)
    send_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"] ')
    text_message = 'Спам Автотест!'
    send_message.send_keys(text_message)

    send_message_btn = driver.find_element(By.CSS_SELECTOR, '.controls-BaseButton[title="Отправить"]')
    send_message_btn.click()

    #  Проверяем сообщение и удаляем его , потом заново проверяем
    time.sleep(3)
    message_sended = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-detail__layout-content '
                                                          '.controls-ListView__item_default .msg-entity-text')
    assert message_sended.text == text_message, 'Сообщения не такое'

    msg = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-detail__layout-content .controls-ListView__item_default')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(msg)
    action_chains.perform()

    mes_del = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    mes_del.click()
    time.sleep(1)

    check_message_del = driver.find_elements(By.CSS_SELECTOR,
                                             '.msg-dialogs-detail__layout-content '
                                             '.controls-ListView__item_default .msg-entity-text')
    assert check_message_del[0].text != text_message, 'Первое сообщение осталось'


finally:
    driver.quit()
