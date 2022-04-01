```mermaid
sequenceDiagram
    participant Main
    participant Machine
    participant FuelTank
    participant Engine
    Main ->> Machine: Machine = Machine()
    Machine ->> FuelTank: self._tank = FuelTank()
    Machine ->> FuelTank: self._tank.fill(40)
    Machine ->> Engine: self._engine = Engine(self._tank)
    Machine ->> Engine: self._engine.start()
    Engine ->> Machine: self._fuel_tank_consume(5)
    Machine ->> FuelTank: self._fuel_tank_consume(5)
    Machine ->> Engine: running = self._engine.is.running()
    Engine ->> Machine: self._fuel_tank.fuel_contents()
    Machine ->> FuelTank: self.fuel_tank.fuel_contents()
    FuelTank -->> Machine: 40
    Machine -->> Engine: 40
    Engine -->> Machine: true
    Machine ->> Engine: self._engine.use_energy()
    Engine ->> Machine: self._fuel_tank.consume(10)
    Machine ->> FuelTank: self._fuel_tank.consume(10)
    FuelTank -->> Machine: 30
    Machine -->> Engine: 30
    Engine -->> Main
```
