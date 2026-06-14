from abc import ABC, abstractmethod


# Абстрактный класс Animal
class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass


# Конкретные классы животных
class Lion(Animal):
    def make_sound(self) -> str:
        return "Рычание!"


class Monkey(Animal):
    def make_sound(self) -> str:
        return "Визг!"


class Elephant(Animal):
    def make_sound(self) -> str:
        return "Трубление!"


# Абстрактная фабрика
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass


# Конкретные фабрики
class LionFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Lion()


class MonkeyFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Monkey()


class ElephantFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Elephant()


def interact_with_animal(factory: AnimalFactory) -> None:
    animal = factory.create_animal()
    print(f"Звук: {animal.make_sound()}")


# Пример использования

lion_factory = LionFactory()
monkey_factory = MonkeyFactory()
elephant_factory = ElephantFactory()

interact_with_animal(lion_factory)
interact_with_animal(monkey_factory)
interact_with_animal(elephant_factory)
