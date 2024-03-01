from test_lib import test, report

month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10
def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
	brands = month_discount_brands.split(',')
	if brand in brands:
		discount_price = round(price * ((100 - MONTH_DISCOUNT_PERC) / 100), 2)
		return discount_price
	else:
		return price

price = 1500
brand = 'Kymco'
expected_price = 1350.0
price_after_discount = calc_discount(price, brand, month_discount_brands)
name = f'Prijs: {price} Prijs na korting: {price_after_discount}'
test(name, expected_price, price_after_discount)

price = 700
brand = 'Kymco'
expected_price = 630.0
price_after_discount = calc_discount(price, brand, month_discount_brands)
name = f'Prijs: {price} Prijs na korting: {price_after_discount}'
test(name, expected_price, price_after_discount)

price = 3450
brand = 'Vespa'
expected_price = 3105.0
price_after_discount = calc_discount(price, brand, month_discount_brands)
name = f'Prijs: {price} Prijs na korting: {price_after_discount}'
test(name, expected_price, price_after_discount)

price = 1199
brand = 'Yamama'
expected_price = 1079.10
price_after_discount = calc_discount(price, brand, month_discount_brands)
name = f'Prijs: {price} Prijs na korting: {price_after_discount}'
test(name, expected_price, price_after_discount)

price = 2100
brand = 'Piaggio'
expected_price = 2100
price_after_discount = calc_discount(price, brand, month_discount_brands)
name = f'Prijs: {price} Prijs na korting: {price_after_discount}'
test(name, expected_price, price_after_discount)

report()