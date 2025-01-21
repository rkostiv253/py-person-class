class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        Person.name = person["name"]
        Person.age = person["age"]
        result.append(Person.age)
        result.append(Person.name)

    for person in people:
        if person.get["wife"] or person.get["husband"]:
            Person.spouse = person.get("wife") or person.get("husband")

    return list(Person.people)
