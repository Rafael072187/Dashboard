📈 Dashboard de Ações – IBOVESPA

Aplicação interativa desenvolvida em Streamlit para visualizar a evolução de preços de ações da B3 (IBOVESPA), calcular performance individual e da carteira, e filtrar por períodos personalizados.

🚀 Funcionalidades

Carrega automaticamente a lista de ações do IBOV a partir de um arquivo CSV (IBOV.csv).

Obtém cotações históricas via yfinance.

Permite selecionar uma ou mais ações para exibição.

Filtro de intervalo de datas com slider.

Gera gráficos de linha interativos.

Calcula e exibe:

Performance individual de cada ativo no período selecionado.

Performance total da carteira (supondo R$ 1000 investidos em cada ativo).

Interface com tema escuro (config.toml).

🛠️ Pré-requisitos

Python 3.8+

Pacotes:

pip install streamlit pandas yfinance

📂 Estrutura de Arquivos
📦 dashboard-acoes
 ┣ 📜 DashboardAcoes.py   # Código principal da aplicação
 ┣ 📜 IBOV.csv            # Lista de ações do IBOV
 ┣ 📜 config.toml         # Configuração do tema (modo dark)

▶️ Como executar

Coloque o arquivo IBOV.csv no mesmo diretório, no formato:

Código
PETR4
VALE3
ITUB4
...


Execute no terminal:

streamlit run DashboardAcoes.py


O navegador abrirá com a aplicação interativa.

📊 Uso

No menu lateral, selecione as ações e o intervalo de datas.

Veja o gráfico de evolução de preços.

Abaixo do gráfico, visualize:

Performance de cada ativo (verde para ganhos, vermelho para perdas).

Performance total da carteira no período.

🎨 Tema

O tema escuro é configurado via config.toml:

[theme]
base = "dark"

⚠️ Observações

É necessário acesso à internet para obter as cotações via yfinance.

As datas de início e fim no carregamento estão fixadas de 01/01/2020 até 01/08/2025 — ajuste no código se necessário.