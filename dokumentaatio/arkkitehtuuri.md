# Arkkitehtuurikuvaus

```mermaid
    classDiagram
        App "1" --> "1" GameControl
        App "1" --> "1" Level
        GameControl "1" -- "1" Level
        Enemy "*" --|> "*" Sprites
        Player "1" --|> "*" Sprites
        Level "1" --> "*" Sprites
        class App{
            level
            game_control
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
```
## Pelin kulku
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

Tämä tieto luetaan pelaajalle pelin alkuruudussa.

### Tiedostot

Peli tallentaa tiedot konfiguraatiotiedosto .env määrittelemään tietokantatiedostoon.

