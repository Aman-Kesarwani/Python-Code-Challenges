from dataclasses import dataclass, field
import random

def getPrice():
    return float(random.randint(50,100))

@dataclass
class Book:
    title: str = "No title"
    author: str = "No name"
    pages : float = 10.0
    price : float= field(default_factory= getPrice)


b1 = Book()

print(b1)