def get_vat(price, vat_rate):
	vat=price/100*vat_rate
	price_not_vat=price-vat
	print(price_not_vat)

price1=int(input('Введите цену '))
vat_rate1=int(input('Введите %НДС '))
get_vat(price1,vat_rate1)