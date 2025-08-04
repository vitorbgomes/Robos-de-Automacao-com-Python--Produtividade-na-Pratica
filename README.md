# Python Automation Suite com Selenium

Bem-vindo à **Python Automation Suite**! Este é um conjunto de scripts de automação desenvolvidos em Python, utilizando a biblioteca Selenium e outras, para executar tarefas rotineiras de forma eficiente. Cada script é projetado para ser uma solução prática e real para desafios comuns, desde o preenchimento de formulários até a organização de arquivos.

## Features

A suíte inclui os seguintes módulos de automação:

1.  🤖 **Bot de Inscrição em Evento:** Preenche automaticamente um formulário do Google Forms com dados de múltiplos participantes listados em uma planilha Excel.
2.  📄 **Bot de Consulta de Status de NF-e:** Acessa o portal da Nota Fiscal Eletrônica da Receita Federal para verificar a disponibilidade e o status dos serviços em tempo real.
3.  📱 **Bot de Envio de Mensagens via WhatsApp:** Envia mensagens personalizadas em massa para contatos listados em uma planilha Excel, utilizando o WhatsApp Web.
4.  🔄 **Conversor de XML para Excel:** Converte múltiplos arquivos XML de NF-e em planilhas Excel organizadas, extraindo informações chave como emitente, destinatário e valor total.
5.  🗂️ **Organizador de Arquivos:** Move e organiza arquivos de um diretório de origem (ex: Downloads) para pastas de destino, categorizadas pela extensão do arquivo.

## 🛠️ Pré-requisitos

Antes de começar, garanta que você tenha os seguintes softwares instalados:

* [Python 3.8+](https://www.python.org/downloads/)
* [Google Chrome](https://www.google.com/chrome/)
* [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) (A versão deve ser compatível com a do seu Google Chrome)

## ⚙️ Instalação e Configuração

1.  **Clone o repositório:**
    ```sh
    git clone [https://github.com/seu-usuario/python-automation-suite.git](https://github.com/seu-usuario/python-automation-suite.git)
    cd python-automation-suite
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```sh
    # Para Windows
    python -m venv venv
    venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure o ChromeDriver:**
    Baixe o ChromeDriver compatível com sua versão do Google Chrome e adicione o executável ao `PATH` do seu sistema ou coloque-o na raiz do projeto.

## 🚀 Como Usar

Cada script pode ser executado individualmente. Siga as instruções abaixo para cada módulo.

### 1. Bot de Inscrição em Evento

Este bot lê os dados da planilha `participantes.xlsx` e os insere em um formulário do Google.

1.  **Crie seu próprio formulário** no [Google Forms](https://forms.google.com/) com os campos "Nome", "Email" e "Empresa".
2.  Abra o arquivo `1_inscricao_evento/evento_inscricao_bot.py` e **substitua o valor da variável `url`** pela URL do seu formulário.
3.  Edite a planilha `1_inscricao_evento/participantes.xlsx` com os dados que deseja cadastrar.
4.  Execute o script:
    ```sh
    cd 1_inscricao_evento
    python evento_inscricao_bot.py
    ```

### 2. Bot de Consulta de Status de NF-e

Verifica a disponibilidade dos serviços da Sefaz no portal da Receita Federal.

1.  Navegue até a pasta do projeto.
2.  Execute o script:
    ```sh
    cd 2_download_nfe
    python baixar_nfe_bot.py
    ```
    O status dos serviços será exibido no terminal.

### 3. Bot de Envio de Mensagens via WhatsApp

Envia mensagens automatizadas pelo WhatsApp Web.

1.  Edite a planilha `3_whatsapp_mensagens/mensagens.xlsx` com os números de telefone (incluindo o código do país, ex: **5511999999999**) e as mensagens.
2.  Execute o script:
    ```sh
    cd 3_whatsapp_mensagens
    python whatsapp_bot.py
    ```
3.  O script abrirá o WhatsApp Web. **Escaneie o QR Code** com seu celular e, em seguida, **pressione Enter** no terminal para iniciar os envios.

### 4. Conversor de XML para Excel

Converte arquivos XML de NF-e para o formato `.xlsx`.

1.  Coloque todos os seus arquivos `.xml` na pasta `4_xml_to_excel_converter/input_xml/`.
2.  Navegue até a pasta do projeto e execute o script:
    ```sh
    cd 4_xml_to_excel_converter
    python xml_to_excel.py
    ```
3.  Os arquivos convertidos serão salvos na pasta `output_excel/`.

### 5. Organizador de Arquivos

Organiza os arquivos de uma pasta de origem em subpastas baseadas na extensão.

1.  Por padrão, o script organiza a pasta `Downloads` do usuário. Se desejar, altere as variáveis `origem` e `destino` no arquivo `5_file_organizer/file_organizer.py`.
2.  Execute o script:
    ```sh
    cd 5_file_organizer
    python file_organizer.py
    ```
    Os arquivos serão movidos e organizados na pasta de destino (`~/Arquivos_Organizados` por padrão).

## 📦 Dependências

Este projeto utiliza as seguintes bibliotecas Python:

* `selenium`: Para automação de navegadores web.
* `pandas`: Para manipulação e análise de dados, especialmente com arquivos Excel.
* `openpyxl`: Necessário para o Pandas ler e escrever arquivos `.xlsx`.

## 🤝 Contribuições

Contribuições são bem-vindas! Se você tem ideias para novos bots ou melhorias nos existentes, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.
