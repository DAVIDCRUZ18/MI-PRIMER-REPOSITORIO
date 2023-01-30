

from selenium import webdriver
import time
import pyautogui as pt
import pyautogui as pt 
import time ;


limit = input("cantidad de mensajes: ") 
message = input("mensaje") 
i=0

time.sleep(3) 

while i < int (limit):
    pt.typewrite(message)
    pt.press("enter")
    i += 1


# Abrir WhatsApp en el navegador
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")

# Esperar a que el usuario escanee el código QR
input("Presiona Enter una vez que hayas escaneado el código QR: ")

# Seleccionar el contacto o grupo de contactos a los que enviar el mensaje
contact = input("Ingresa el nombre del contacto o grupo: ")
user = driver.find_element_by_xpath(f"//span[@title='{contact}']")
user.click()

# Enviar el mensaje
message = input("Ingresa el mensaje a enviar: ")
msg_box = driver.find_element_by_xpath(
    "//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
for i in range(int(input("Ingresa la cantidad de veces que quieres enviar el mensaje: "))):
    msg_box.send_keys(message)
    pt.press("enter")

# Cerrar el navegador
driver.quit()
