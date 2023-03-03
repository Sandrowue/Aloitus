# KYSYY KUNTOILIJAN PERUSTIEDOT JA LUO KUNTOILIJA-OLIOITA

# Kirjastot ja Moduulit

import kuntoilija

# Functions

# Ask a question and covert the answer to float
def kysy_tiedo(kysymys):
    """Asks a question from the user and converts answer to a floating point number

    Args:
        kysymys (str): The question to ask

    Returns:
        tuple: answer as float, Error message, Error Code and a detailed error message
    """
    while True:
        answer_txt = input(kysymys)
        try:
            answer = float(answer_txt)
            result = (answer, 'OK', 0, 'Conversion successful')
            break
        except Exception as e:
            print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
            result = (0, 'Error', 1, str(e))
    return result

# Enter information about an athlete
nimi = input('Nimi: ')

# Use ask_user function to get height and convert it into float
answer = kysy_tiedo('Pituus (cm): ')
# Read the 1st element of the tuple containing height value
pituus = answer[0]

answer = kysy_tiedo('Paino (kg): ')
paino = answer[0]
answer = kysy_tiedo('Ikä: ')
ika = answer[0]
answer = kysy_tiedo('Sukupuoli, 1 mies, 0 nainen')
sukupuoli = answer[0]



'''
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
        print('Virhe syötetyssä arvossa, vain 1 ja 0 sallittu', e)'''


kuntoilija1 = kuntoilija.Kuntoilija(nimi, pituus, paino, ika, sukupuoli)

print(kuntoilija1.nimi, 'painoindeksi on ', kuntoilija1.bmi)

print('Viimeisen kysymyksen virheilmoitus', answer[1], 'koodi', answer[2], 'engl. ilmoitus', answer[3])