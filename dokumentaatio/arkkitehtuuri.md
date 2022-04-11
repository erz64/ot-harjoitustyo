```mermaid
    classDiagram
        game_control "1" --> "1" GameControl
        level "1" --> "1" Level
        GameControl "1" -- "1" Level
        Enemy "*" --|> "*" Sprite
        Player "1" --|> "*" Sprite
        class App{
            level
            game_control
        }
        class GameControl{

        }
        class Level{

        }
        class Sprite{

        }
        class Enemy{

        }
        class Player{
            
        }
```