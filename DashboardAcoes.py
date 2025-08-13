import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import timedelta


@st.cache_data
def carregar_dados(empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers)
    
    cotacoes_acao = pd.DataFrame()  # Cria um DataFrame vazio para armazenar dados válidos
   
    for ticker in empresas:
        try:
            # Tenta obter os dados históricos para cada ticker
            cotacao = dados_acao.tickers[ticker].history(start="2020-01-01", end="2025-08-01")
            if not cotacao.empty:
                # Se conseguiu dados, adicione ao DataFrame
                cotacoes_acao[ticker] = cotacao['Close']
        except Exception as e:
            st.warning(f"Não foi possível carregar dados para {ticker}: {e}")


    return cotacoes_acao


@st.cache_data
def carregar_tickers_acoes():
    base_tickers = pd.read_csv("IBOV.csv", sep=";")
    tickers = list(base_tickers["Código"])
    tickers = [item + ".SA" for item in tickers]
    return tickers


acoes = carregar_tickers_acoes()
dados = carregar_dados(acoes)
dados.index = pd.to_datetime(dados.index)


st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações ao longo dos anos.
""")


st.sidebar.header("Filtros")


if not dados.empty:
    lista_acoes = st.sidebar.multiselect("Escolha as ações para visualizar", dados.columns)
    
    if lista_acoes:
        dados_selecionados = dados[lista_acoes]


        if len(lista_acoes) == 1:
            acao_unica = lista_acoes[0]
            dados_selecionados = dados_selecionados.rename(columns={acao_unica: "Close"})


        data_inicial = dados_selecionados.index.min().to_pydatetime()
        data_final = dados_selecionados.index.max().to_pydatetime()
        
        intervalo_data = st.sidebar.slider("Selecione o período",
                                        min_value=data_inicial,
                                        max_value=data_final,
                                        value=(data_inicial, data_final),
                                        step=timedelta(days=1))


        dados_filtrados = dados_selecionados.loc[intervalo_data[0]:intervalo_data[1]]


        # Exibir o gráfico - funciona igual para 1 ou vários ativos
        st.line_chart(dados_filtrados)


        # Calcular a performance dos ativos
        texto_performance_ativos = ""


        if len(lista_acoes)==0:
            lista_acoes = list(dados_filtrados.columns)
        elif len(lista_acoes)==1:
            dados_filtrados = dados_filtrados.rename(columns={"Close": acao_unica})


        carteira = [1000 for acao in lista_acoes]
        total_inicial_carteira = sum(carteira)


        for i, acao in enumerate(lista_acoes):
            performance_ativo = dados_filtrados[acao].iloc[-1] / dados_filtrados[acao].iloc[0] - 1
            performance_ativo = float(performance_ativo)


            carteira[i] = carteira[i] * (1 + performance_ativo)


            if performance_ativo > 0:
                # :cor[texto]
                texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: :green[{performance_ativo:.1%}]"
            elif performance_ativo < 0:
                texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: :red[{performance_ativo:.1%}]"
            else:
                texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: {performance_ativo:.1%}"


        total_final_carteira = sum(carteira)
        performance_carteira = total_final_carteira / total_inicial_carteira - 1


        if performance_carteira > 0:
            texto_performance_carteira = f"Performance da carteira com todos os ativos: :green[{performance_carteira:.1%}]"
        elif performance_carteira < 0:
            texto_performance_carteira = f"Performance da carteira com todos os ativos: :red[{performance_carteira:.1%}]"
        else:
            texto_performance_carteira = f"Performance da carteira com todos os ativos: {performance_carteira:.1%}"


        st.markdown(f"""
        ### Performance dos Ativos
        Essa foi a perfomance de cada ativo no período selecionado:

        {texto_performance_ativos}

        """)

        st.markdown(texto_performance_carteira, unsafe_allow_html=True)

else:
    st.warning("Nenhum dado de ações disponível.")