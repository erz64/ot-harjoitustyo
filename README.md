
# Avoid the objects

Sovellus on peli, jossa pelaaja väistelee ympäriltä tulevia objekteja ja yrittää selvitä mahdollisimman kauan.

## Dokumentaatio

[tuntikirjanpito.md](https://github.com/erz64/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[vaatimusmaarittely.md](https://github.com/erz64/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[changelog.md](https://github.com/erz64/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri.md](https://github.com/erz64/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus
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

## Komentorivitoiminnot

Ohjelman pystyy suorittamaan komennolla:
```bash
poetry run invoke start
```
Testit voidaan suorittaa komennolla:
```
poetry run invoke test
```
Testikattavuuden voi saada komennolla:
```
poetry run invoke coverage-report
```
### Pylint
Koodin laadun tarkistus voidaan suorittaa komennolla:
```
poetry run invoke lint
```

