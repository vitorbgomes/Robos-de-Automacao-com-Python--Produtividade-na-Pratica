from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx"
driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)
status = driver.find_elements(By.XPATH, '//table[@id="ctl00_ContentPlaceHolder1_gdvDisponibilidade"]/tbody/tr')
for linha in status[1:]:
    colunas = linha.find_elements(By.TAG_NAME, "td")
    print(f"{colunas[0].text}: Sefaz Virtual - {colunas[1].text}")

driver.quit()
