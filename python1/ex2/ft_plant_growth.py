class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height  += 1.0

    def to_age(self) -> None:
        self.age += 1

if __name__ == "__main__":
    start = 1
    end = 7
    p = Plant("Rose", 25, 30)

    print("=== Garden Plant Growth ===")
    print("=== Day 1 ===")
    p.show()
    for i in range(start, end):
        print(f"=== Day {i+1} ===")
        p.grow()
        p.to_age()
        p.show()

    total = 1.0 * 6
    print(f"Growth this week: {total}cm")
