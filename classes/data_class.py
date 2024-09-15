from dataclasses import dataclass, asdict


@dataclass
class Person:
    name: str
    age: int

p = Person('John', 23)
print(p)
d = asdict(p)
print(d)
print(Person(**d))