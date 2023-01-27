# OHJELMA, JOKA KYSYY BMI-TIETOJA USEASTA KUNTOILIJASTA

# Kirjastot ja Moduulit

# Tuodaan fitness.py:n sisältämät toiminnot tähän ohjelmaan.
import fitness

# Kysytään tiedot ja tulostetaan painoindeksi kunnes halutaan lopettaa

'''pituus_teksti = '0'
while pituus_teksti != '':

    pituus_teksti = input('Pituus (cm), (stop = tyhjä): ')
    if pituus_teksti == '':
        break
    paino_teksti = input('Paino (kg): ')

    pituus = float(pituus_teksti)
    paino = float(paino_teksti)
    # lasketaan painoindeksin fitness-modulin laske_bmi funktiolla
    bmi = fitness.laske_bmi(paino, pituus)

    print('Painoindeksi on', bmi)'''

bmi_lista = []

while True:
    
    pituus_teksti = input('Pituus (cm), (stop = tyhjä): ')
    if pituus_teksti == '':
        break
    paino_teksti = input('Paino (kg): ')
   
    # yritetään muuttaa syötetyt tekstit luvuksi
    try:
        pituus = float(pituus_teksti)
        paino = float(paino_teksti)
        bmi = fitness.laske_bmi(paino, pituus)
        # Lisätään BMI listaan
        bmi_lista.append(bmi)
        print('Painoindeksi on', bmi)
    # Jos tapathtuu virhe, ilmoitetaan käyttäjälle
    except Exception as e:
        print('Syötteessä oli virhe, pelkkä numero sallittu!', e)
    # lasketaan painoindeksin fitness-modulin laske_bmi funktiolla
print('Painoindeksit olivat:', bmi_lista)
