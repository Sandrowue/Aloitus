# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN    

# Muuttujat
# Kysytään käyttäjältä tiedot
pituus_teksti = input('Kuinka pitkä olet(cm)?')
paino_teksti = input('Kuinka paljon painat(kg)?')
ika_teksti = input('Kuinka vanha olet?')
sukupuoli_teksti = input('Sukupuoli: mies - vastaa: 1 / nainen - vastaa: 0:') 

pituus = float(pituus_teksti)
paino = float(paino_teksti)
ika = float(ika_teksti)
sukupuoli = float(sukupuoli_teksti)
# Määritellään funktio painoindeksin laskentaan
def laske_bmi(paino, pituus):
    """Laskee painoindeksin (BMI)

    Args:
        paino (float): paino (kg)
        pituus (float): pituus (cm)

    Returns:
        float: painoindeksin kahden desimaalin tarkkuudella
    """
    pituus = pituus / 100 # muutetaan pituus metreiksi
    bmi = round(paino / pituus**2, 2)
    #print('Painoindeksisi on', bmi)
    return bmi

#Aikuisen rasvaprosentti = (1.20 × painoindeksi) + (0.23 × ikä) − (10.8 × sukupuoli) − 5.4

#jossa sukupuoli 1, jos mies ja 0, jos nainen. 

def aikuisen_rasvaprosentti(bmi, ika, sukupuoli):
    """_summary_

    Args:
        bmi (float): painoindeksi
        ika (float): henkilön ikä
        sukupuoli (float): 1 -> mies, 0 -> nainen

    Returns:
        float: Aikuisen kehon rasvaprosentti
    """

    rasvaprosentti = round(bmi * 1.20 + 0.23 * ika - 10.8 * sukupuoli - 5.4, 1)
    return rasvaprosentti

oma_bmi = laske_bmi(paino, pituus)
oma_rasvaprosentti = aikuisen_rasvaprosentti(oma_bmi, ika, sukupuoli)

print('Painoindeksisi on:', oma_bmi, 'ja kehon rasvaprosentti on:', oma_rasvaprosentti)