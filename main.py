# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Some generic sound"

    def eat(self):
        return f"{self.name} is eating."


# Подклассы Animal: Bird, Mammal, Reptile
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return "Chirp"


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Roar"


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        return "Hiss"


# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} says {animal.make_sound()}")


# Класс Zoo, использующий композицию
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)


# Классы сотрудников ZooKeeper и Veterinarian
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")


# Создание объектов и демонстрация работы
bird = Bird("Tweety", 3, "small")
mammal = Mammal("Leo", 5, "golden")
reptile = Reptile("Sly", 4, "rough")

animals = [bird, mammal, reptile]
zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

keeper = ZooKeeper("John")
vet = Veterinarian("Lucy")
zoo.add_staff(keeper)
zoo.add_staff(vet)

# Демонстрация работы
animal_sound(animals)
keeper.feed_animal(mammal)
vet.heal_animal(bird)
