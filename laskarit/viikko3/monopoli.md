```mermaid
    classDiagram
        Pelaaja "1" --> "1" Pelinappula
        Ruutu "40" --> Pelilauta "0-8" 
        Pelinappula "1" --> "1" Ruutu
        Pelaaja "2-8" --> "1" Peli
        Peli "1" --> "1" Pelilauta
        Peli "1" --> "2" Nopat
        


        class Peli{
            
        }
        class Nopat{
            
        }
        class Pelaaja{
            
        }
        class Pelinappula{

        }
        class Pelilauta{
            
        }
        class Ruutu{

        }
```