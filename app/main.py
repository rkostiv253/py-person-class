class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    name_to_person = {}
    result = []
    for person in people:
        Person.name = person["name"]
        Person.age = person["age"]
        result.append(Person.age)
        result.append(Person.name)

    for person in people:
        person_instance = name_to_person[person["name"]]
        if person.get("wife"):
            person_instance.wife = name_to_person[person.get("wife")]
        elif person.get("husband"):
            person_instance.husband = name_to_person[person.get("husband")]

    return list(Person.people)
