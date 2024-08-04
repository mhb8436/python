exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'JPY': 110.0,
    'KRW': 1150.0
}

def convert(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print('지원하지 않는 통화입니다.')
        return
    
    # USD 기준으로 변환 
    amount_in_usd = amount / exchange_rates[from_currency]
    # 목적 통화로 변환
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    return converted_amount


