class Building:
    def __init__(self, name: str, floors: int) -> None:
        self.name = name
        self.floors = floors


class Elevator:
    def __init__(self, building: Building) -> None:
        self.building = building
        self.is_door_closed = False
        self.floor = 0

    def open_door(self) -> None:
        self.is_door_closed = False
        print("Door opened!")

    def close_door(self) -> None:
        self.is_door_closed = True
        print("Door closed!")

    def up(self, floor: int) -> None:
        if floor not in range(self.building.floors + 1):
            print(f"Error: Floor {floor} is outside the building limits.")
            return

        if floor <= self.floor:
            print("Error: The destination floor must be above the current floor.")
            return

        if not self.is_door_closed:
            self.close_door()

        print(f"Going up from floor {self.floor} to floor {floor}.")
        self.floor = floor

        self.open_door()

    def down(self, floor: int) -> None:
        if floor not in range(self.building.floors + 1):
            print(f"Error: Floor {floor} is outside the building limits.")
            return

        if floor >= self.floor:
            print("Error: The destination floor must be below the current floor.")
            return

        if not self.is_door_closed:
            self.close_door()

        print(f"Going down from floor {self.floor} to floor {floor}.")
        self.floor = floor

        self.open_door()

    def call_elevator(self, actual_floor: int) -> None:
        if actual_floor not in range(self.building.floors + 1):
            print(
                f"Error: Floor {actual_floor} is outside the limit "
                f"of {self.building.floors} floors."
            )
            return

        if self.floor == actual_floor:
            print(f"The elevator is already on floor {actual_floor}.")
            return

        if actual_floor < self.floor:
            self.down(actual_floor)
        else:
            self.up(actual_floor)


building = Building("Vivendas de Itaparica", 12)
elevator = Elevator(building)

print(elevator.building.name)

print(
    f"Current elevator status: "
    f"{'Closed' if elevator.is_door_closed else 'Open'} "
    f"- Floor: {elevator.floor}"
)

elevator.up(5)

elevator.call_elevator(5)

elevator.call_elevator(12)
