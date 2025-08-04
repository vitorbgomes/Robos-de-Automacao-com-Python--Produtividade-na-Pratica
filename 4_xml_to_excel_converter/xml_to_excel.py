import os
import xml.etree.ElementTree as ET
import pandas as pd

entrada = "input_xml"
saida = "output_excel"
os.makedirs(saida, exist_ok=True)

for arquivo in os.listdir(entrada):
    if arquivo.endswith(".xml"):
        caminho = os.path.join(entrada, arquivo)
        tree = ET.parse(caminho)
        root = tree.getroot()

        ns = {'ns': 'http://www.portalfiscal.inf.br/nfe'}
        dados = []

        for inf in root.findall(".//ns:infNFe", ns):
            emit = inf.find(".//ns:emit/ns:xNome", ns).text
            dest = inf.find(".//ns:dest/ns:xNome", ns).text
            total = inf.find(".//ns:ICMSTot/ns:vNF", ns).text
            dados.append({
                "Emitente": emit,
                "Destinatário": dest,
                "Valor Total": total
            })

        df = pd.DataFrame(dados)
        df.to_excel(os.path.join(saida, arquivo.replace(".xml", ".xlsx")), index=False)

print("Conversão concluída!")
