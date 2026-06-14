from abc import ABC, abstractmethod

#Интерфейс элемента файловой системы
class FileSystemElement(ABC):
    @abstractmethod
    def display(self, indent: str = ""):
        pass
    @abstractmethod
    def get_size(self) -> int:
        pass

#Файл
class File(FileSystemElement):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
    def display(self, indent: str = ""):
        print(f"{indent}Файл: {self.name} ({self.size} bytes)")
    def get_size(self) -> int:
        return self.size

#Директория(компоновщик)
class Directory(FileSystemElement):
    def __init__(self, name: str):
        self.name = name
        self.children = []
    def add(self, element: FileSystemElement):
        self.children.append(element)
    def display(self, indent: str = ""):
        print(f"{indent}Директория: {self.name}")
        for child in self.children:
            child.display(indent + "  ")
    def get_size(self) -> int:
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size

# Клиентский код
def main():
    root = Directory("root")
    home = Directory("home")
    user = Directory("user")

    file1 = File("file1.txt", 100)
    file2 = File("file2.txt", 200)
    file3 = File("file3.txt", 300)

    root.add(home)
    home.add(user)
    user.add(file1)
    user.add(file2)
    root.add(file3)

    root.display()
    print(f"\nTotal size: {root.get_size()} bytes")

if __name__ == "__main__":
    main()
