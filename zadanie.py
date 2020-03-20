#no polando znak on klawiatura
#zeby nie bylo nie jasnosci to ten prefix czy cos 0b to binarne
#0o to oktalne a 0x to hexadecymalne

N = 11 #numer w dzienniku

math = 2**N+1 # A

binary = (bin(math))
print (math)
print (binary)


octal = (oct(math))  #na oktalne (osemkowe)
print (octal)

ectal = (math + 376) #liczba E przed zamiana

aectal = (bin(ectal)) #liczba E zamieniona na binarny
print (aectal)


hex = (hex(math)) #na hexadecymalen
print (hex)
t = 'A08'
convert = int(t, 16) #z hexa na dziesietny zeby moc dodac

dhex = (math + convert) #dodanie A08
ahex = (bin(dhex)) #zamienienie na binarny

add = (math + ectal + dhex) #dodanie wszystkiego

print(add-math) #wynik
