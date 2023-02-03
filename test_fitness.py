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