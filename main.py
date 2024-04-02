import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Some generic sound"

    def eat(self):
        return f"{self.name} is eating."

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return "Chirp"

    def to_dict(self):
        return {'type': 'Bird', 'name': self.name, 'age': self.age, 'wing_span': self.wing_span}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'], data['wing_span'])

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Roar"

    def to_dict(self):
        return {'type': 'Mammal', 'name': self.name, 'age': self.age, 'fur_color': self.fur_color}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'], data['fur_color'])

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        return "Hiss"

    def to_dict(self):
        return {'type': 'Reptile', 'name': self.name, 'age': self.age, 'scale_type': self.scale_type}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'], data['scale_type'])

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

    def to_dict(self):
        return {'role': 'ZooKeeper', 'name': self.name}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'])

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

    def to_dict(self):
        return {'role': 'Veterinarian', 'name': self.name}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'])

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def save_zoo_state(self, file_name):
        zoo_data = {
            "animals": [animal.to_dict() for animal in self.animals],
            "staff": [staff.to_dict() for staff in self.staff]
        }
        with open(file_name, 'w') as file:
            json.dump(zoo_data, file)

    @classmethod
    def load_zoo_state(cls, file_name):
        with open(file_name, 'r') as file:
            zoo_data = json.load(file)
        zoo = cls()
        for animal_data in zoo_data["animals"]:
            if animal_data['type'] == 'Bird':
                animal = Bird.from_dict(animal_data)
            elif animal_data['type'] == 'Mammal':
                animal = Mammal.from_dict(animal_data)
            elif animal_data['type'] == 'Reptile':
                animal = Reptile.from_dict(animal_data)
            zoo.add_animal(animal)
        for staff_data in zoo_data["staff"]:
            if staff_data['role'] == 'ZooKeeper':
                staff = ZooKeeper.from_dict(staff_data)
            elif staff_data['role'] == 'Veterinarian':
                staff = Veterinarian.from_dict(staff_data)
            zoo.add_staff(staff)
        return zoo
# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} says {animal.make_sound()}")

# Создание объектов и демонстрация работы
bird = Bird("Tweety", 3, "small")
mammal = Mammal("Leo", 5, "golden")
reptile = Reptile("Sly", 4, "rough")

animals = [bird, mammal, reptile] # Убедитесь, что список animals определен
zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

keeper = ZooKeeper("John")
vet = Veterinarian("Lucy")
zoo.add_staff(keeper)
zoo.add_staff(vet)

# Демонстрация работы
animal_sound(animals) # Теперь вызов этой функции должен работать
keeper.feed_animal(mammal)
vet.heal_animal(bird)


zoo.add_staff(keeper)
zoo.add_staff(vet)

# Сохранение состояния зоопарка в файл
zoo.save_zoo_state('zoo_state.json')

# Загрузка состояния зоопарка из файла
loaded_zoo = Zoo.load_zoo_state('zoo_state.json')



