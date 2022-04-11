```mermaid
    classDiagram
        game_control "1" --> "1" GameControl
        level "1" --> "1" Level
        GameControl "1" -- "1" Level
        Enemy "*" --|> "*" pygame.sprite.Sprite
        Player "1" --|> "*" pygame.sprite.Sprite
        class App{
            level
            game_control
        }
        class GameControl{

        }
        class Level{

        }
        class pygame.sprite.Sprite{

        }
        class Enemy{

        }
        class Player{
            
        }
```