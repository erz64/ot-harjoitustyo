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
