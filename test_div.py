from div import dividir
def test_division_normal():
   assert dividir(10, 2) == 5

def test_division_decimal():
   assert dividir(7, 2) == 3.5

def test_division_negativa():
   assert dividir(-8, 2) == -4

def test_division_dos_negativos():
   assert dividir(-8, -2) == 4

def test_division_entre_uno():
   assert dividir(7, 1) == 7

def test_division_cero_numerador():
   assert dividir(0, 5) == 0