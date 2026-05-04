class Plant():
    def __init__(self, name: str) -> None:
        self.name = name
        self.height = 0
        self.age = 0

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"\n{self.name}: Error, Height can't be negative")
            print("Height update rejected")
        else:
            self.height = height
            print(f"Height updated: {self.height}cm")
    
    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"\n{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else: 
            self.age = age
            print(f"Age updated: {self.age} days old")

    def get_height(self) -> None:
        return self.height

    def get_age(self) -> None:
        return self.age
    def show(self) -> None:
        print(f"\nCurrent state: {self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p = Plant("Rose")
    p.set_height(25)
    p.set_age(30)
    p.set_height(-5)
    p.set_age(-5)
    p.show()