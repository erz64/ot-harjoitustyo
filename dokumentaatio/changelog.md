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

