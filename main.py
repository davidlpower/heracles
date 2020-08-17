from app.money_format import MoneyFormat

local_format = 'de_DE'
formater = MoneyFormat(local_format)

converted_value = formater.format(13232313.023230)

print(converted_value)