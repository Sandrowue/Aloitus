# KYSYY KUNTOILIJAN PERUSTIEDOT JA LUO KUNTOILIJA-OLIOITA

# Kirjastot ja Moduulit

import kuntoilija
import questions
# Enter information about an athlete
name = input('Nimi: ')

# Ask details about her/him

question = questions.Question('Kuinka paljon painat (kg)? ')
weight = question.kysy_tiedo_float(True)[0]

question = questions.Question('Kuinka pitkä olet (cm)? ')
height = question.kysy_tiedo_float(True)[0]

question = questions.Question('Kuinka vanha olet? ')
age = question.kysy_tiedo_integer(True)[0]

question = questions.Question('Sukupuoli: 1 = mies, 0 = nainen: ')
gender = question.kysy_tiedo_integer(True)[0]

question = questions.Question('Mikä on kaulanympäryksesi (cm)? ')
neck = question.kysy_tiedo_float(True)[0]

question = questions.Question('Mikä on vyötärön mittasi (cm)? ')
waist = question.kysy_tiedo_float(True)[0]
if gender == 0: 
    question = questions.Question('Mikä on lantionympäryksesi (cm) ?')
    hips = question.kysy_tiedo_float(True)[0]

# Create an athlet object from Kuntoilija class
athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender)

# Print some information about the ahtlete
text_to_show = f'Terve {athlete.nimi}, painoindeksisi tänään on {athlete.bmi}'
print(text_to_show)
fat_percentage = athlete.rasvaprosentti()
if gender == 1:
    usa_fat_percentage = athlete.usa_rasvaprosentti_mies(height, waist, neck)
else:
    usa_fat_percentage = athlete.usa_rasvaprosentti_nainen(height, waist, hips, neck)

text_to_show = f'suomalainen rasvaprosentti on {fat_percentage} ja amerikkalainen rasvaprosentti on {usa_fat_percentage}'
print(text_to_show)