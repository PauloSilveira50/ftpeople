# 🚀 FTP DEV

## 🧭 Objetivo do Projeto
O **FTP DEV** tem como objetivo desenvolver uma ferramenta para **upload, atualização e exclusão de aplicações hospedadas em servidores via protocolo FTP**, facilitando o processo de **implementação e deploy de software em ambientes remotos**.

O sistema permitirá que o usuário:
- Selecione arquivos locais para envio;
- Configure o servidor de destino;
- Realize o **deploy automatizado** de forma prática e segura.

---

## ⚙️ Principais Funcionalidades

- 🔼 **Upload de arquivos** para o servidor via FTP;
- 🔁 **Atualização automática** de aplicações já hospedadas;
- ❌ **Exclusão remota** de arquivos obsoletos no servidor;
- 🖥️ **Interface interativa** para configuração de conexões e seleção de arquivos;
- 🔒 **Gerenciamento seguro de credenciais** de acesso FTP;
- 📊 **Feedback visual** sobre o progresso e status das operações.

---

## 🧩 Tecnologias Utilizadas

- **Linguagem:** [Python 3.13.5](https://www.python.org/)
- **Framework Web:** [Flask](https://flask.palletsprojects.com/)
- **Protocolo de Transferência:** [FTP (File Transfer Protocol)](https://datatracker.ietf.org/doc/html/rfc959)
- **Front-end:** HTML5, CSS3, JavaScript
- **Controle de Versão:** Git + GitHub

---

## 🛠️ Instruções de Instalação e Execução

### 🔹 Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:
- Python 3.13.5 
- Git  
- Pip (gerenciador de pacotes do Python)

### 🔹 Passos para rodar o projeto

```bash
# 1️⃣ Clone este repositório
git clone https://github.com/seuusuario/ftp-dev.git

# 2️⃣ Acesse a pasta do projeto
cd ftp-dev

# 3️⃣ Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv venv
venv\Scripts\activate   # No Windows
source venv/bin/activate  # No Linux/Mac

# 4️⃣ Instale as dependências
pip install -r requirements.txt

# 5️⃣ Execute a aplicação Flask
python app.py
