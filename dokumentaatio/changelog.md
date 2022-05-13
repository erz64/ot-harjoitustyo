# Changelog

## Viikko 3
- Luotu pelinrakenne
- Uudet luokat: GameControl, Player ja Level
- Pelaaja voi liikuttaa keskellä olevaa objektia hiirellä
- Testattu että liikkuminen toimii oikein

## Viikko 4
- Uusi luokka: Enemy
- Luokan Enemy olioita syntyy satunnaisesti peli-ikkunan vasemmasta reunasta, joilla satunnainen suunta peli-ikkunan oikeaan reunaan
- Peliloppuu (peli-ikkuna sulkeutuu), kun pelaaja osuu johonkin näistä Enemy olioista
- Luotu uusi testi varmistamaan, että pelaajan osuessa johonkin Enemy olioon tämä törmäys eli "collision" tunnistetaan

## Viikko 5
- Uudet luokat: Boss, Bullet
- Luokan Boss olio eli päävihollinen syntyy vasempaan pelireunaan, kun aina kun edellisen päävihollisen tuhoutumisesta on kulunut tarpeeksi aikaa
- Päävihollinen liikkuu satunnaisesti ylös tai alas
- Pelaajan ohjaamasta objektista lähtee tasaisin välein Bullet luokan olioita eli luoteja kohti vasenta reunaa, jos jokin näistä luodeista osuu pääviholliseen, tämä menetttää elämäpisteitä. Kun elämäpisteet loppuvat, päävihollinen tuhoutuu

## Viikko 6
- Uusi luokka: BossAttack
- Lisätty tippuvia teriä eli luokan BossAttack olioita, kun päävihollinen on elossa
- Pelaaja ei ammu luoteja ellei päävihollinen ole elossa
- Lisätty peliin tasoja, aina kun päävihollinen kuolee taso nousee, ja vihollisia syntyy useammin. Taso näytetään vasemmassa yläreunassa.
- Lisätty paljon uusia testejä testaamaan mm. törmäyksiä ja liikkumista

## Viikko 7
- Lisätty tietokantatiedosto tallentamaan pelaajan saavutettu taso
- Muutettu Boss-spriten ja BossAttack-spriten ulkonäköä
- Lisätty alku- ja loppuruutu
- Lisätty testejä mm. GameControl luokan
