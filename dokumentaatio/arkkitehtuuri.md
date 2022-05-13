# Arkkitehtuurikuvaus

## Pelin logiikka
```mermaid
    classDiagram
        App "1" --> "1" GameControl
        App "1" --> "1" EventQueue
        App "1" --> "1" Level
        GameControl "1" -- "1" Level
        EventQueue "1" --> "1" GameControl
        Enemy "*" --|> "*" Sprites
        Player "1" --|> "*" Sprites
        BossAttack "*" --|> "*" Sprites
        Bullet "*" --|> "*" Sprites
        Level "1" --> "*" Sprites
        class App{
            
        }
        class GameControl{

        }
        class Level{

        }
        class Sprites{

        }
        class Enemy{

        }
        class Player{
            
        }
        class BossAttack{
        
        }
        class Bullet{
        
        }
        class EventQueue{
        
        }
        
```
## Pelin kulku
Ohjelman toimiminen, siitä asti kun pelaaja syöttää komennon poetry run invoke start, siihen asti kun pelaaja sulkee ohjelman:
Kun pelaaja suorittaa tämän komennon, app tiedosto alustaa Level luokan, joka taas alustaa pelaajan ja ensimmäisen päävihollisen. Tätä level luokkaa käytetään parametrina app tiedoston alustaessa GameControl luokan. App tämän jälkeen kutsuu GameControl main_menu funktiota, jolloin peli lähtee käyntiin. Peli on käynnissä kunnes pelaaja sulkee sen.
```mermaid
    sequenceDiagram
        participant App
        participant Level
        participant GameControl
        participant Player
        participant Boss
        App->>Level: Initialize level
        Level->>Player: Initialize player
        Player-->>Level: None
        Level->>Boss: Initialize first boss
        Boss-->>Level: None
        Level-->>App: None
        App->>GameControl: Start game
        GameControl-->>App: End game
```

## Tiedostojen tallennus ja luku:
Kun pelaaja häviää pelin, sovellus tallentaa tiedon saavutetusta tasosta SQLite-tietokantaan.

Pelaajan paras saavutettu taso luetaan pelaajalle pelin alkuruudussa.

### Tiedostot

Peli tallentaa tiedot konfiguraatiotiedosto .env määrittelemään tietokantatiedostoon.

