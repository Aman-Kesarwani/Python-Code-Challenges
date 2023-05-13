from dataclasses import dataclass

@dataclass
class Book:
    title : str
    author : str
    price: float

    def __post_init__(self):
        self.description = f"Title: {self.title}, Author: {self.author}, Price: {self.price}"

b1 = Book("Harry Potter", "JK rowling", 45.50)
b2 = Book("Digital Logic Design", "Marris Mano", 200)

print(b1.description)

