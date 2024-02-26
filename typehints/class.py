# Person Object / Clases
# Constructor:
# name : str
# second_name : str
# 
# Methods:
# __str__ (Output print formater)
class Person():
    
    def __init__(self, name:str, second_name:str) -> None:
        self.name = name
        self.second_name = second_name
    
    def __str__(self) -> str:
        return f"My name is {self.name.title()} {self.second_name.title()}"

# Function that print the Person Object Info
# Parameters
# person: Person()
# return None
def getInfo(person: Person):
    print(person)

# Output
getInfo(person=Person("jose","rodriguez"))    