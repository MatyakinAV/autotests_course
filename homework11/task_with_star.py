# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
import urllib.request

driver = webdriver.Chrome()
site_sbis = 'https://sbis.ru/'
try:
    driver.get(site_sbis)
    link_download = driver.find_element(By.CSS_SELECTOR, '[class="sbisru-Footer__link"]['
                                                         'href="/download?tab=ereport&innerTab=ereport25"]')
    link_download.location_once_scrolled_into_view
    link_download.click()
    sbis_plugin = driver.find_elements(By.CSS_SELECTOR, '.controls-TabButton__wrapper')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(sbis_plugin[1])
    action_chains.click().perform()
    sleep(2)
    # Проверяем что вкладка Windows, и что она открыта
    os_system = driver.find_elements(By.CSS_SELECTOR, '[class="js-innerTabPlugin sbis_ru-DownloadNew-innerTabs__title '
                                                      'sbis_ru-DownloadNew-innerTabs__title--default"]')
    assert os_system[0].text == 'Windows', 'Не верная вкладка'
    assert os_system[0].is_displayed(), 'Вкладка не отображается'
    href_plugin = driver.find_element(By.CSS_SELECTOR, '[href="https://update.sbis.ru/Sbis3Plugin/master/win32'
                                                       '/sbisplugin-setup-web.exe"]')
    assert href_plugin.is_displayed(), 'Не отображается ссылка'

    url = href_plugin.get_attribute('href')
    file_name = 'sbis_plugin_setup.exe'
    urllib.request.urlretrieve(url, file_name)
    size_file = (os.path.getsize(file_name)) / (1024 * 1024)
    print(f' Размер установочного файла  {file_name} {round(size_file, 2)} mb')
finally:
    driver.quit()


