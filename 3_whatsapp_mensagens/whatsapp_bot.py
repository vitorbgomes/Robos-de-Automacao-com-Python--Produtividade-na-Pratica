from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

data = pd.read_excel("mensagens.xlsx")

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("Escaneie o QR Code e pressione Enter...")

for _, row in data.iterrows():
    telefone = row["Contato"]
    mensagem = row["Mensagem"]
    driver.get(f"https://web.whatsapp.com/send?phone={telefone}&text={mensagem}")
    time.sleep(10)
    try:
        botao = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        botao.click()
        print(f"Mensagem enviada para {telefone}")
    except:
        print(f"Erro ao enviar para {telefone}")

driver.quit()
