# KUNTOILIJAN TIEDOT OLIO OHJELMOINIA

# Kirjastot ja moduulit
import fitness

# Luokkamääritykset

class Kuntoilija:
    """Luokka kuntoilijan tietoja varten
    """
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):
        # Määritellään tulevan olion ominaisuudet (property), luokan kentät (field)
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli

if __name__ == "__main__":
    
    kuntoilija = Kuntoilija('Kalle Kuntoilija', 171, 56, 22, 'mies')
    print(kuntoilija.nimi, 'painaa', kuntoilija.paino, 'kg')