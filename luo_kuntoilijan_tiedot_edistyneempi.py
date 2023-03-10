# KYSYY KUNTOILIJAN PERUSTIEDOT JA LUO KUNTOILIJA-OLIOITA

# Kirjastot ja Moduulit

import kuntoilija
import questions
# Enter information about an athlete
name = input('Nimi: ')

# Ask details about her/him

question1 = questions.Question('Kuinka paljon painat (kg)? ')
weight = question1.kysy_tiedo_float(True)

question2 = questions.Question('Kuinka pitkä olet (cm)? ')
height = question2.kysy_tiedo_float(True)

question3 = questions.Question('Kuinka vanha olet? ')
age = question3.kysy_tiedo_integer(True)

question4 = questions.Question('Sukupuoli: 1 = mies, 0 = nainen: ')
gender = question4.kysy_tiedo_integer(True)

question5 = questions.Question('Mikä on kaulanympäryksesi (cm)? ')
neck = question5.kysy_tiedo_float(True)

question6 = questions.Question('Mikä on vyötärön mittasi (cm)? ')
waist = question6.kysy_tiedo_float
if gender == 0: 
    question7 = questions.Question('Mikä on lantionympäryksesi (cm) ?')
    hip = question7.kysy_tiedo_float(True)

# Create an athlet object from Kuntoilija class
athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender)