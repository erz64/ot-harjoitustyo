import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")  
    
    def test_rahan_lataus_toimii(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(str(self.maksukortti), "saldo: 5.1")
    
    def test_saldo_vahenee_jos_kortilta_nostetaan(self):
        self.maksukortti.ota_rahaa(5)

        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
    
    def test_saldo_ei_vahene_jos_kortilta_nostetaan_ja_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(15)

        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_metodi_ota_rahaa_palauttaa_arvon_True_jos_rahat_riittavat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)
    
    def test_metodi_ota_rahaa_palauttaa_arvon_False_jos_rahat_eivat_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(15), False)

