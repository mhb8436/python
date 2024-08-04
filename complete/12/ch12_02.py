import module02.currency_converter

print('환율 변환기 입니다')

amount = float(input('변환할 금액을 입력하세요'))
from_currency = input('변환할 금액 통화를 입력하세요(예: USD, EUR, JYP, KRW):')
to_currency = input('변환할 대상 통화를 입력하세요(예: USD, EUR, JYP, KRW):')

converted_amount = module02.currency_converter.convert(amount, from_currency, to_currency)
print(f"{amount} {from_currency}는 {converted_amount:.2f} {to_currency} 입니다. ")


