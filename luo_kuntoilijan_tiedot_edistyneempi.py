# KYSYY KUNTOILIJAN PERUSTIEDOT JA LUO KUNTOILIJA-OLIOITA

# Kirjastot ja Moduulit

import kuntoilija

# Enter information about an athlete

nimi = input('Nimi: ')
while True:
    pituus_txt = input('Pitusss (cm): ')
    try:
        pituus = float(pituus_txt)
        break
    except Exception as e:
        print('Virhe pituuden arvossa, tarkista syöte', e)

while True:
    paino_txt = input('Paino (kg): ')
    try:
        paino = float(paino_txt)
        break
    except Exception as e:
        print('Virhe painon arvossa, tarkista syöte', e)    

while True:
    ika_txt = input('Ikä: ')
    try:
        ika = float(ika_txt)
        break
    except Exception as e:
        print('Virhe iän arvossa, tarkista syöte', e)

while True:
    sukupuoli_txt = input('Sukupuoli, 1 mies, 0 nainen')
    try:
        sukupuoli = float(sukupuoli_txt)
        break
    except Exception as e:
        print('Virhe syötetyssä arvossa, vain 1 ja 0 sallittu', e)


kuntoilija1 = kuntoilija.Kuntoilija(nimi, pituus, paino, ika, sukupuoli)

print(kuntoilija1.nimi, 'painoindeksi on ', kuntoilija1.bmi)