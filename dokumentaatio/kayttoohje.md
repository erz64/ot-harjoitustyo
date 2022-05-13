# Käyttöohje

Pelataksesi peliä lataa viimeisimmän [releasen](https://github.com/erz64/ot-harjoitustyo/releases/tag/viikko7) lähdekoodi valitsemalla Assets-osion alta Source code.

## Pelin käynnistys
1. Asenna riippuvuudet komennolla:
```bash
poetry install
```
2. Alusta tietokannat komennolla
```
poetry run invokte build
```
3. Käynnistä peli komennolla:
```
poetry run invoke start
```
Peli-ikkunassa aukeaa alkuruutu, jossa näkee parhaimman saavutetun tason ja napin, jolla aloitetaan peli.

Liikuta vihreää palloa hiirellä ja väistele muita objekteja, kun päävihollinen syntyy yritä tuhota se päästäksesi seuraavalle tasolle.

Jos haluat pitää tauon pelin aikana paina Escape näippäintä.
