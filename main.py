class Device:
    def __init__ (self, height, width, name):
        self.height=height
        self.width=width
        self.name=name

    def power_on(self):
        print(f"{self.name} has powered on.")

class Computer (Device):
    def power_on(self):
        print("Your computer has now turned on.")
    
    def power_off (self):
        print("Your computer has now turned off.")
    
    def log_in (self):
        print("You have logged in.")

class Vehicle:
    def __init__ (self, name, speed, size):
        self.name=name
        self.speed=speed
        self.size=size

    def switch_on (self):
        print(f"{self.name} has switched on.")
    
    def drive(self):
        print("You are now driving the vehicle.")
    
    def fix (self):
        print(f"Now fixing {self.name}")
    
class Car (Vehicle):
    def switch_on(self):
        print("Your car has now switched on.")
    def drive(self):
        print("Now driving your car.")
    def fix(self):
        print("Now fixing your car.")
    def switch_off(self):
        print("Your car has now switched off.")

class Motorbike (Vehicle):
    def switch_on(self):
        print("Your motorbike has now switched on.")
    def drive(self):
        print("Now driving your motorbike.")
    def fix(self):
        print("Now fixing your motorbike.")
    def switch_off(self):
        print("Your motorbike has now switched off.")
