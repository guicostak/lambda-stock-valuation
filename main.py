import yfinance as yf
import numpy as np

def get_total_assets(ticker):
    stock = yf.Ticker(ticker)

    # Pegando o balanço patrimonial
    balance_sheet = stock.balance_sheet

    if 'Total Assets' in balance_sheet:
        total_assets = balance_sheet.loc['Total Assets'][0]  # Último valor disponível
        return total_assets
    else:
        print("Total Assets não disponível para este ticker.")
        return None

def get_wacc(ticker):
    # Baixando os dados financeiros da empresa
    stock = yf.Ticker(ticker)

    # Obter a capitalização de mercado (Market Cap)
    market_cap = stock.info.get('marketCap', 0)
    
    # Obter o custo da dívida (Debt) e o total de ativos (Total Assets)
    debt = stock.info.get('totalDebt', 0)
    total_assets = get_total_assets(ticker)

    # Verificando se os dados são válidos
    if total_assets <= 0:
        print("Total Assets não pode ser zero ou negativo.")
        return None

    # Cálculo do custo do capital próprio e da dívida
    equity = market_cap

    # A fórmula WACC: WACC = (E/V) * Re + (D/V) * Rd * (1 - T)
    # Onde:
    # E = Valor de mercado do capital (equity)
    # D = Valor de mercado da dívida (debt)
    # V = E + D (Valor total da firma)
    # Re = Custo do capital próprio (pode ser estimado pelo forward PE)
    # Rd = Custo da dívida (pode ser estimado pelo debt-to-equity)
    
    # Obtendo os custos
    forward_pe = stock.info.get('forwardPE', 0)
    debt_to_equity = stock.info.get('debtToEquity', 0)

    if forward_pe == 0 or debt_to_equity == 0:
        print("Os valores de forward PE ou debt to equity não estão disponíveis.")
        return None

    # Cálculo do WACC
    wacc = (equity / total_assets) * forward_pe + (debt / total_assets) * debt_to_equity
    return wacc

ticker = "BBAS3.SA"

acao = yf.Ticker(ticker)
dados_financeiros = acao.financials

# 🔹 Extrair o fluxo de caixa livre (FCF) dos últimos anos
fluxo_de_caixa_livre = acao.cashflow.loc["Free Cash Flow"]
print(f"Fluxo de caixa livre atual:  { fluxo_de_caixa_livre.iloc[0]}")

# Obter a taxa de crescimento de 1 ano usando .iloc
taxa_crescimento_1y = acao.growth_estimates.loc['+1y'].iloc[0]
print(f"Taxa de crescimento de 1 ano: {taxa_crescimento_1y}")

wacc = get_wacc(ticker)
print(f"Wacc: {wacc}")
