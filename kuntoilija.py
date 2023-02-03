# KUNTOILIJAN TIEDOT OLIO OHJELMOINIA

# Kirjastot ja moduulit
import fitness

# Luokkamääritykset
# Kuntoilija luokka Yliluokka JunioriKuntoilijalle
class Kuntoilija:
    """Luokka kuntoilijan tietoja varten
    """
    # Olionmuodostin eli konstruktori
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):
        # Määritellään tulevan olion ominaisuudet (property), luokan kentät (field)
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
        self.bmi = fitness.laske_bmi(self.paino, self.pituus)
# Metodi painoindeksin laskemiseen
   

 # Metodi aikuisen rasvaprosentin laskemiseen
    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.aikuisen_rasvaprosentti(self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti

# JunioriKuntoilija on Kuntoilia luokan aliluokka
class JunioriKuntoilija(Kuntoilija):
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):
        super().__init__(nimi, pituus, paino, ika, sukupuoli)

    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.lapsen_rasvaprosentti(self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti

if __name__ == "__main__":
    
    kuntoilija = Kuntoilija('Kalle Kuntoilija', 171, 56, 18, 1)
    print(kuntoilija.nimi, 'painaa', kuntoilija.paino, 'kg')
    print('painoindeksi on', kuntoilija.bmi)
    print('rasvaprosentti on', kuntoilija.rasvaprosentti())

    juniorikuntoilija = JunioriKuntoilija('Aki', 171, 56, 17, 1)
    print('rasvaprosentti on', juniorikuntoilija.rasvaprosentti())