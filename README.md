<center><h1>📊 Dashboard de Ações - IBOVESPA</h1></center>

<p align="center">
  Aplicação interativa desenvolvida em <b>Streamlit</b> para analisar e visualizar a evolução de preços das ações da <b>B3</b>, calcular performance individual e da carteira, e aplicar filtros personalizados de data.
</p>

---

## 🧭 Tabela de Conteúdos
- [Descrição](#-descrição)
- [Instalação](#-instalação)
- [Uso](#-uso)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Como Contribuir](#-como-contribuir)
- [Autor](#-autor)

---

## 💡 Descrição
O **Dashboard de Ações** permite acompanhar o desempenho histórico de ativos listados no **IBOVESPA**, exibindo gráficos interativos e estatísticas de performance.  
Ideal para investidores e analistas que desejam entender a evolução dos preços e comparar resultados de carteiras simuladas.

---

## ⚙️ Instalação

<details>
<summary><b>Passos para configurar o ambiente</b></summary>

1. Clone o repositório:
   ```bash
   git clone https://github.com/Rafael072187/Dashboard.git
   cd Dashboard
Crie e ative um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Verifique se o arquivo IBOV.csv está no mesmo diretório do script DashboardAcoes.py.
Ele deve conter os códigos das ações, por exemplo:

Copiar código
PETR4, VALE3, ITUB4, ...
</details>

---

▶️ Uso
Execute o comando abaixo no terminal:

bash
Copiar código
streamlit run DashboardAcoes.py
A aplicação abrirá automaticamente no navegador.
Utilize o menu lateral para:

Selecionar uma ou mais ações do IBOV

Definir o período de análise

Visualizar o desempenho individual e total da carteira

---

🧩 Tecnologias Utilizadas
Python 3.8+

Streamlit – Interface web interativa

Pandas – Manipulação de dados

yfinance – Obtenção de cotações históricas

config.toml – Personalização do tema (modo escuro)

---

🤝 Como Contribuir
<details> <summary><b>Passos para contribuir</b></summary>
Faça um fork do projeto

Crie uma branch para sua modificação:

bash
Copiar código
git checkout -b minha-nova-feature
Faça as alterações e commit:

bash
Copiar código
git commit -m "Adicionei nova funcionalidade"
Envie a branch:

bash
Copiar código
git push origin minha-nova-feature
Abra um Pull Request 🚀

</details>

---

👤 Autor
<center>
Rafael Bittencourt de Araújo
💼 Desenvolvedor Python e entusiasta de dados
🌐 GitHub

</center>
<p align="center"> <a href="https://github.com/Rafael072187/Dashboard" style="background-color:#0366d6;color:white;padding:10px 20px;border-radius:5px;text-decoration:none;"> 🔗 Ver Repositório no GitHub </a> </p> ```
