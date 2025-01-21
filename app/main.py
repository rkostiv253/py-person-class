class Person:

    people = {}

    def __init__(self, name: str, age: int, spouse: str = None):
        self.name = name
        self.age = age
        self.spouse = spouse
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        name = person["name"]
        age = person["age"]
        result.append(age)
        result.append(name)

    for person in people:
        if person["wife"] or person["husband"] is not None:
            spouse = person.get("wife") or person.get("husband")

    return Person.people
