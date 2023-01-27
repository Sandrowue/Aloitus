# OHJELMA, JOKA KYSYY BMI-TIETOJA USEASTA KUNTOILIJASTA

# Kirjastot ja Moduulit

import fitness

pituus_teksti = input('Pituus (cm): ')
paino_teksti = input('Paino (kg): ')

pituus = float(pituus_teksti)
paino = float(paino_teksti)

bmi = fitness.laske_bmi(paino, pituus)

print('Painoindeksi on', bmi)