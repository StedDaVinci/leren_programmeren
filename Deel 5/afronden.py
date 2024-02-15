from test_lib import test, report

def afronden(nr: float) -> float:
	DECIMAAL = 5
	return round(nr * 100 / DECIMAAL) * DECIMAAL / 100

Bedrag = 4.23
Expected_bedrag = 4.25
Afgeronde_bedrag = afronden(Bedrag)
name = f'test bedrag: {Bedrag} afgerond bedrag: {Afgeronde_bedrag}'
print(type(name))
test(name, Expected_bedrag, Afgeronde_bedrag)

Bedrag = 22.21
Expected_bedrag = 22.20
Afgeronde_bedrag = afronden(Bedrag)
name = f'test bedrag: {Bedrag} afgerond bedrag: {Afgeronde_bedrag}'
print(type(name))
test(name, Expected_bedrag, Afgeronde_bedrag)

Bedrag = 52.54
Expected_bedrag = 52.55
Afgeronde_bedrag = afronden(Bedrag)
name = f'test bedrag: {Bedrag} afgerond bedrag: {Afgeronde_bedrag}'
print(type(name))
test(name, Expected_bedrag, Afgeronde_bedrag)

Bedrag = 91.37
Expected_bedrag = 91.35
Afgeronde_bedrag = afronden(Bedrag)
name = f'test bedrag: {Bedrag} afgerond bedrag: {Afgeronde_bedrag}'
print(type(name))
test(name, Expected_bedrag, Afgeronde_bedrag)

Bedrag = 35.69
Expected_bedrag = 35.7
Afgeronde_bedrag = afronden(Bedrag)
name = f'test bedrag: {Bedrag} afgerond bedrag: {Afgeronde_bedrag}'
print(type(name))
test(name, Expected_bedrag, Afgeronde_bedrag)

report()