Dados financeiros da ação (acao.financials)

Tax Effect Of Unusual Items
Tax Rate For Calcs
Total Unusual Items
Total Unusual Items Excluding Goodwill
Net Income From Continuing Operation Net Minority Interest
Reconciled Depreciation
Net Interest Income
Interest Expense
Interest Income
Normalized Income
Net Income From Continuing And Discontinued Operations
Diluted Average Shares
Basic Average Shares
Diluted EPS
Basic EPS
Diluted NI Available to Common Stockholders
Net Income Common Stockholders
Other under Preferred Stock Dividend
Net Income
Minority Interests
Net Income Including Noncontrolling Interests
Net Income Extraordinary
Net Income Continuous Operations
Tax Provision
Pretax Income
Other Non-Operating Income Expenses
Special Income Charges
Write Off
Operating Expense
Other Operating Expenses
Depreciation And Amortization In Income Statement
Amortization
Depreciation Income Statement
Selling General And Administration
Selling And Marketing Expense
General And Administrative Expense
Insurance And Claims
Rent And Landing Fees
Total Revenue
Operating Revenue

Fluxo de caixa da ação (acao.cashflow)

Free Cash Flow  
Capital Expenditure  (CapEx)
End Cash Position  
Beginning Cash Position  
Effect Of Exchange Rate Changes  
Changes In Cash  
Financing Cash Flow  
Net Other Financing Charges  
Interest Paid Cff  
Cash Dividends Paid  
Common Stock Dividend Paid  
Net Common Stock Issuance  
Net Issuance Payments Of Debt  
Net Long Term Debt Issuance  
Investing Cash Flow  
Dividends Received Cfi  
Net Investment Purchase And Sale  
Sale Of Investment  
Purchase Of Investment  
Net Business Purchase And Sale  
Sale Of Business  
Purchase Of Business  
Net Intangibles Purchase And Sale  
Purchase Of Intangibles  
Net PPE Purchase And Sale  
Sale Of PPE  
Purchase Of PPE  
Operating Cash Flow  
Taxes Refund Paid  
Change In Working Capital  
Change In Other Current Liabilities  
Change In Other Current Assets  
Other Non Cash Items  
Provisionand Write Offof Assets  
Deferred Tax  
Depreciation And Amortization  
Amortization Cash Flow  
Depreciation  
Pension And Employee Benefit Expense  
Net Foreign Currency Exchange Gain Loss  
Gain Loss On Sale Of PPE  
Net Income From Continuing Operations  






wacc = 0.10  # Custo médio ponderado de capital (10%)
anos = 10  # Período da projeção

# 🔹 Calcular o valor presente dos fluxos de caixa futuros
fcf_futuro = [fcf_atual * (1 + taxa_crescimento) ** i for i in range(1, anos + 1)]
valores_presentes = [fcf / (1 + wacc) ** i for i, fcf in enumerate(fcf_futuro, 1)]

# 🔹 Calcular o valor residual (perpetuidade)
valor_residual = (fcf_futuro[-1] * (1 + taxa_crescimento)) / (wacc - taxa_crescimento)
valor_residual_presente = valor_residual / (1 + wacc) ** anos

# 🔹 Somar todos os valores para obter o valor total da empresa
valor_justo_empresa = sum(valores_presentes) + valor_residual_presente

# 🔹 Obter o número de ações para calcular o preço justo por ação
num_acoes = acao.info["sharesOutstanding"]
fair_price = valor_justo_empresa / num_acoes

# 🔹 Exibir o resultado
print(f"Valor Justo (Fair Price) por ação de {ticker}: R$ {fair_price:.2f}")




Informações da ação (acao.info)

Stock Info: {
    'address1': '',
    'address2': '',
    'city': '',
    'state': '',
    'country': '',
    'phone': '',
    'website': '',
    'industry': '',
    'industryKey': '',
    'industryDisp': '',
    'sector': '',
    'sectorKey': '',
    'sectorDisp': '',
    'longBusinessSummary': '',
    'fullTimeEmployees': '',
    'companyOfficers': [],
    'auditRisk': '',
    'boardRisk': '',
    'compensationRisk': '',
    'shareHolderRightsRisk': '',
    'overallRisk': '',
    'governanceEpochDate': '',
    'executiveTeam': [],
    'maxAge': '',
    'priceHint': '',
    'previousClose': '',
    'open': '',
    'dayLow': '',
    'dayHigh': '',
    'regularMarketPreviousClose': '',
    'regularMarketOpen': '',
    'regularMarketDayLow': '',
    'regularMarketDayHigh': '',
    'dividendRate': '',
    'dividendYield': '',
    'exDividendDate': '',
    'payoutRatio': '',
    'fiveYearAvgDividendYield': '',
    'beta': '',
    'trailingPE': '',
    'forwardPE': '',
    'volume': '',
    'regularMarketVolume': '',
    'averageVolume': '',
    'averageVolume10days': '',
    'averageDailyVolume10Day': '',
    'bid': '',
    'ask': '',
    'bidSize': '',
    'askSize': '',
    'marketCap': '',
    'fiftyTwoWeekLow': '',
    'fiftyTwoWeekHigh': '',
    'priceToSalesTrailing12Months': '',
    'fiftyDayAverage': '',
    'twoHundredDayAverage': '',
    'trailingAnnualDividendRate': '',
    'trailingAnnualDividendYield': '',
    'currency': '',
    'tradeable': '',
    'enterpriseValue': '',
    'profitMargins': '',
    'floatShares': '',
    'sharesOutstanding': '',
    'heldPercentInsiders': '',
    'heldPercentInstitutions': '',
    'impliedSharesOutstanding': '',
    'bookValue': '',
    'priceToBook': '',
    'lastFiscalYearEnd': '',
    'nextFiscalYearEnd': '',
    'mostRecentQuarter': '',
    'earningsQuarterlyGrowth': '',
    'netIncomeToCommon': '',
    'trailingEps': '',
    'forwardEps': '',
    'lastSplitFactor': '',
    'lastSplitDate': '',
    'enterpriseToRevenue': '',
    '52WeekChange': '',
    'SandP52WeekChange': '',
    'lastDividendValue': '',
    'lastDividendDate': '',
    'quoteType': '',
    'currentPrice': '',
    'targetHighPrice': '',
    'targetLowPrice': '',
    'targetMeanPrice': '',
    'targetMedianPrice': '',
    'recommendationMean': '',
    'recommendationKey': '',
    'numberOfAnalystOpinions': '',
    'totalCash': '',
    'totalCashPerShare': '',
    'totalDebt': '',
    'totalRevenue': '',
    'revenuePerShare': '',
    'returnOnAssets': '',
    'returnOnEquity': '',
    'grossProfits': '',
    'operatingCashflow': '',
    'earningsGrowth': '',
    'revenueGrowth': '',
    'grossMargins': '',
    'ebitdaMargins': '',
    'operatingMargins': '',
    'financialCurrency': '',
    'symbol': '',
    'language': '',
    'region': '',
    'typeDisp': '',
    'quoteSourceName': '',
    'triggerable': '',
    'customPriceAlertConfidence': '',
    'regularMarketChangePercent': '',
    'regularMarketPrice': '',
    'corporateActions': [],
    'regularMarketTime': '',
    'exchange': '',
    'messageBoardId': '',
    'exchangeTimezoneName': '',
    'exchangeTimezoneShortName': '',
    'gmtOffSetMilliseconds': '',
    'market': '',
    'esgPopulated': '',
    'shortName': '',
    'marketState': '',
    'hasPrePostMarketData': '',
    'firstTradeDateMilliseconds': '',
    'regularMarketChange': '',
    'regularMarketDayRange': '',
    'fullExchangeName': '',
    'averageDailyVolume3Month': '',
    'fiftyTwoWeekLowChange': '',
    'fiftyTwoWeekLowChangePercent': '',
    'fiftyTwoWeekRange': '',
    'fiftyTwoWeekHighChange': '',
    'fiftyTwoWeekHighChangePercent': '',
    'fiftyTwoWeekChangePercent': '',
    'earningsTimestamp': '',
    'earningsTimestampStart': '',
    'earningsTimestampEnd': '',
    'earningsCallTimestampStart': '',
    'earningsCallTimestampEnd': '',
    'isEarningsDateEstimate': '',
    'epsTrailingTwelveMonths': '',
    'epsForward': '',
    'epsCurrentYear': '',
    'priceEpsCurrentYear': '',
    'fiftyDayAverageChange': '',
    'fiftyDayAverageChangePercent': '',
    'twoHundredDayAverageChange': '',
    'twoHundredDayAverageChangePercent': '',
    'sourceInterval': '',
    'exchangeDataDelayedBy': '',
    'averageAnalystRating': '',
    'cryptoTradeable': '',
    'longName': '',
    'trailingPegRatio': ''
}
