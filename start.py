import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""browser = webdriver.Chrome()
browser.get("https://selenium-python.readthedocs.io/")
print("Titulo de la pagina: ", browser.title)"""
"""
driver = webdriver.Chrome()

try:
    driver.maximize_window()
    time.sleep(4)
    driver.get("https://demoqa.com/select-menu")
    
    #Localiza el menu desplegable
    dropdown = Select(driver.find_element(By.ID, "oldSelectMenu"))
    
    #Selecciona por valor
    dropdown.select_by_value("1")
    print("Seleccionado: Azul")
    time.sleep(10)
    
    #Selecciona por texto visible
    dropdown.select_by_visible_text("Green")
    print("Seleccionado: Verde")

finally:
    time.sleep(60)
"""
"""
driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get("https://demoqa.com/alerts")
    time.sleep(3)
    #Haz clic en el boton para abrir una alerta
    driver.find_element(By.ID, "alertButton").click()
    time.sleep(3)
    #Cambia el control a la alerta y acepta
    WebDriverWait(driver,10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Texto de la alerta: ", alert.text)
    time.sleep(3)
    alert.accept()
    print("Alerta aceptada")

finally:
    time.sleep(60)
"""
"""
driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get("https://www.google.com")
    time.sleep(8)
    
    #Abre una nueva pestaña
    driver.execute_script("window.open('https://www.selenium.dev', '_blank');")
    time.sleep(8)
    
    #Cambia a la nueva pestaña
    driver.switch_to.window(driver.window_handles[1])
    print("Nuevo titulo: ", driver.title)
    time.sleep(8)
    
    #Regresa a la primer pestaña
    driver.switch_to.window(driver.window_handles[0])
    print("Titulo de regreso: ", driver.title)

finally:
    time.sleep(60)
"""
"""
driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    #Toma screenshot
    driver.save_screenshot("screenshot_google.png")
    print("Captura de pantalla guardada")

finally:
    time.sleep(60)
"""
