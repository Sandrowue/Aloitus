# KYSYY KUNTOILIJAN PERUSTIEDOT JA LUO KUNTOILIJA-OLIOITA

# Kirjastot ja Moduulit

import kuntoilija
import questions
# Enter information about an athlete
name = input('Nimi: ')

# Ask details about her/him

question1 = questions.Question('Kuinka paljon painat (kg)? ')
weight = question1.kysy_tiedo_float(True)[0]

question2 = questions.Question('Kuinka pitkä olet (cm)? ')
height = question2.kysy_tiedo_float(True)[0]

question3 = questions.Question('Kuinka vanha olet? ')
age = question3.kysy_tiedo_integer(True)[0]

question4 = questions.Question('Sukupuoli: 1 = mies, 0 = nainen: ')
gender = question4.kysy_tiedo_integer(True)[0]

question5 = questions.Question('Mikä on kaulanympäryksesi (cm)? ')
neck = question5.kysy_tiedo_float(True)[0]

question6 = questions.Question('Mikä on vyötärön mittasi (cm)? ')
waist = question6.kysy_tiedo_float(True)[0]
if gender == 0: 
    question7 = questions.Question('Mikä on lantionympäryksesi (cm) ?')
    hips = question7.kysy_tiedo_float(True)[0]

# Create an athlet object from Kuntoilija class
athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender)

# Print some information about the ahtlete
text_to_show = f'Terve{athlete.nimi}, painoindeksisi tänään on {athlete.bmi}'
print(text_to_show)
fat_percentage = athlete.rasvaprosentti()
if gender == 1:
    usa_fat_percentage = athlete.usa_rasvaprosentti_mies(height, waist, neck)
else:
    usa_fat_percentage = athlete.usa_rasvaprosentti_nainen(height, waist, hips, neck)

text_to_show = f'suomalainen rasvaprosentti on {fat_percentage} ja amerikkalainen rasvaprosentti on {usa_fat_percentage}'