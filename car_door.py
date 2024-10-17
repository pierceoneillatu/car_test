class Car:
    def __init__(self, doors=4):
        self._doors = doors  # Default value is 4 doors
    
    # Getter method
    def get_doors(self):
        return self._doors
    
    # Setter method
    def set_doors(self, doors):
        if doors > 0:
            self._doors = doors
        else:
            raise ValueError("The number of doors must be greater than 0")

# Example usage:
car = Car()  # Default is 4 doors
print(car.get_doors())  # Output: 4

car.set_doors(2)  # Set to 2 doors
print(car.get_doors())  # Output: 2
