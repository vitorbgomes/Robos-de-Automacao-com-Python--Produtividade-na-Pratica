from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os

url = "https://forms.gle/xxxxxx"  # Substitua por um formulário real
data = pd.read_excel("participantes.xlsx")
driver = webdriver.Chrome()

for _, row in data.iterrows():
    driver.get(url)
    time.sleep(2)

    campos = driver.find_elements(By.CLASS_NAME, "whsOnd")
    campos[0].send_keys(row["Nome"])
    campos[1].send_keys(row["Email"])
    campos[2].send_keys(row["Empresa"])

    botao = driver.find_element(By.CLASS_NAME, "NPEfkd")
    botao.click()
    time.sleep(2)

driver.quit()
