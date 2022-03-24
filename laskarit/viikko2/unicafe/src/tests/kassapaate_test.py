import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)
    
    def test_kassan_raha_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_myytyjen_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat, 0)

    def test_kateisella_edullisen_lounaan_ostaessa_kassan_raha_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(250)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisella_edullisen_lounaan_ostaessa_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)
    
    def test_kateisella_edullisen_lounaan_ostaessa_edullisten_lounaiden_myyty_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(250)

        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisella_edullisen_lounaan_ostaessa_saldo_ei_riita_vaihtorahojen_palautus(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)
    
    def test_kateisella_edullisen_lounaan_ostaessa_myytyjen_edullisten_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateisella_edullisen_lounaan_ostaessa_ja_saldo_ei_riita_kassan_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    #------------------------------------------------------------
    
    def test_kateisella_maukkaan_lounaan_ostaessa_kassan_raha_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisella_maukkaan_lounaan_ostaessa_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
    
    def test_kateisella_maukkaan_lounaan_ostaessa_edullisten_maukkaiden_myyty_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateisella_maukkaan_lounaan_ostaessa_saldo_ei_riita_vaihtorahojen_palautus(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(390), 390)
    
    def test_kateisella_maukkaan_lounaan_ostaessa_myytyjen_maukkaiden_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(230)

        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisella_maukkaan_lounaan_ostaessa_ja_saldo_ei_riita_kassan_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(230)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    #--------------------------------------------------------------------------------------------
    def test_kortilla_edullisen_lounaan_ostaessa_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kortilla_edullisen_lounaan_ostaessa_kortilta_lahtee_rahaa_oikea_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 260)
    
    def test_kortilla_edullisen_lounaan_ostaessa_funktio_palauttaa_arvon_True(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_kortilla_edullisen_lounaan_ostaessa_myytyjen_edullisten_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortilla_edullisen_lounaan_ostaessa_kun_saldo_ei_riita_kortin_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 20)
    
    def test_kortilla_edullisen_lounaan_ostaessa_kun_saldo_ei_riita_myytyjen_edullisten_lounaiden_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 2)
    
    def test_kortilla_edullisen_lounaan_ostaessa_kun_saldo_ei_riita_funktio_palauttaa_arvon_false(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
    #--------------------------------------------------------------------------------------
    def test_kortilla_maukkaan_lounaan_ostaessa_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kortilla_maukkaan_lounaan_ostaessa_kortilta_lahtee_rahaa_oikea_maara(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 100)
    
    def test_kortilla_maukkaan_lounaan_ostaessa_funktio_palauttaa_arvon_True(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    
    def test_kortilla_maukkaan_lounaan_ostaessa_myytyjen_maukkaiden_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortilla_maukkaan_lounaan_ostaessa_kun_saldo_ei_riita_kortin_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        

        self.assertEqual(self.maksukortti.saldo, 100)
    
    def test_kortilla_maukkaan_lounaan_ostaessa_kun_saldo_ei_riita_myytyjen_maukkaiden_lounaiden_maara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kortilla_maukkaan_lounaan_ostaessa_kun_saldo_ei_riita_funktio_palauttaa_arvon_false(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
    
    def test_kortille_ladattaessa_rahaa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,100)

        self.assertEqual(self.maksukortti.saldo, 600)
    
    def test_kortille_ladattessa_rahaa_kassassa_oleva_rahan_maara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
    
    def test_kortille_ladattaessa_negatiivnen_summa_rahaa_kassassa_oleva_maara_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_ladattaessa_negatiivinen_summa_kortin_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)

        self.assertEqual(self.maksukortti.saldo, 500)
    

    
