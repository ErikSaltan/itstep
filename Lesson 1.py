class Student:
    def __init__(self, name: str ='Azazel', age: int = 18, country: str = 'France'):
        self.name = name
        self.age = age
        self.country = country

    def print_data(self) -> None:
        print(f'Hello! My name is {self.name}. I am {self.age} years old. I`m from {self.country}.')

    def __str__(self):
        return f'Hello! My name is {self.name}. I am {self.age} years old. I`m from {self.country}.'
    def __del__(self):
        print(f'{self.name} is deleted :(')


first_student = Student('Nick', 20, 'USA')
second_student = Student('Kate', 19, 'Ukraine')
third_student = Student()

print(first_student)
print(second_student)
print(third_student)