# FITNESS-MODULIN TESTIT

# KIRJASTOJEN JA MODULIEN LATAUKSET
import fitness

def test_laske_bmi():
    assert fitness.laske_bmi(64.7, 170) == 22.39
    assert fitness.laske_bmi(40, 170) == 13.84
    assert fitness.laske_bmi(100, 170) == 34.6

def test_aikuisen_rasvaprosentti():
    # testejä aikuisia miehiä
    assert fitness.aikuisen_rasvaprosentti(22.4, 20, 1) == 15.3
    assert fitness.aikuisen_rasvaprosentti(13.8, 40, 1) == 9.6
    assert fitness.aikuisen_rasvaprosentti(34.6, 70, 1) == 41.4

    # testejä aikuisia naisia
    assert fitness.aikuisen_rasvaprosentti(24.97, 35, 0) == 32.6
    assert fitness.aikuisen_rasvaprosentti(21.45, 22, 0) == 25.4
    assert fitness.aikuisen_rasvaprosentti(22.09, 44, 0) == 31.2

def test_lapsen_rasvaprosentti():
    #tyttö
    assert fitness.lapsen_rasvaprosentti(23.81, 14, 0) == 27.6
    #poika
    assert fitness.lapsen_rasvaprosentti(24.44, 14, 1) == 24.9

def test_usarasvaprosentti_mies():
    assert fitness.usarasvaprosentti_mies(178, 100, 36) ==28.02
    assert fitness.usarasvaprosentti_mies(170, 90, 33) == 25.1
    assert fitness.usarasvaprosentti_mies(189, 110, 39) == 30.08

def test_usarasvaprosentti_nainen():
    assert fitness.usarasvaprosentti_nainen(176, 105, 70, 30) == 28.48
    assert fitness.usarasvaprosentti_nainen(165, 100, 55, 28) == 21.83
    assert fitness.usarasvaprosentti_nainen(159, 95, 75, 29) == 30.81