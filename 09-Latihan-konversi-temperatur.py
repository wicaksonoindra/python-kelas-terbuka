# Konversi Temperatur

## Celcius
print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius=float(input("Masukkan suhu dalam celcius: "))
print("Suhu adalah",celcius,"Celcius")
## Reamur
reamur = (4/5) * celcius
print("Suhu dalam Reamur adalah",reamur,"Reamur")

## Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah",fahrenheit,"Fahrenheit")

## Kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah",kelvin,"Kelvin")

## ====================PR========================
print("\n===PR===\nFahrenheit ke Kelvin\n")
fahrenheitpr = float(input("Masukkan suhu Fahrenheit: "))
kelvinpr = (5/9) * (fahrenheitpr-32) + 273
print("Suhu dalam Kelvin adalah",kelvinpr,"Kelvin")

print("\nKelvin ke Fahrenheit\n")
kelvinpr2 = float(input("Masukkan Suhu Kelvin: "))
fahrenheitpr2 = (kelvinpr2 - 273) * (9/5) + 32
print("Suhu dalam Fahrenheit adalah",fahrenheitpr2,"Fahrenheit")
