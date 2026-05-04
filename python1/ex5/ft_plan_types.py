class Plant():
    bloom = 0
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name:str, height: float, age:int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = 0
    
    def bloom(self) -> None:
        if self.is_blooming == 0:
            print(f"[asking the {self.name} to bloom]")
            self.is_blooming = 1
    
    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming == 0:
            print("Rose has not bloomed yet")
        else:
            print("Rose is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    
    def produce_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        print("Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.")
        
    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}")

class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str,  nutritional_value: int):
        super().__init__(name, height, age)
        self.nutritional_value = nutritional_value
        self.harvest_season = harvest_season
    
    def grow(self, h: float):
        self.height += h

    def to_age(self, a: int):
        self.age += a
    
    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"nutritional_value: {self.nutritional_value}")

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    p = Flower("Rose", 15.0, 10, "red")
    p.show()
    p.bloom()
    p.show()

    print("\n=== Tree")
    t = Tree("Oak", 200.0, 365, 5.0)
    t.show()
    t.produce_shade()

    print("\n=== Vegetable")
    v = Vegetable("tomato", 5.0, 10, "april", 0)
    v.show()
    print("[make tomato grow and age for 20 days]")
    v.grow(42)
    v.to_age(20)
    v.show()
