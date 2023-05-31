# time: O( n )
class Employee:
    def __init__(self, fun, empl=[]):
        self.employees = empl
        self.fun = fun
        self.present = -1
        self.absent = -1


def max_party(person):
    if person.present >= 0:
        return person.present

    x = person.fun
    for lower in person.employees:
        x += party_without(lower)

    y = party_without(person)
    person.present = max(x, y)
    return person.present


def party_without(person):
    if person.absent >= 0:
        return person.absent

    x = 0
    for lower in person.employees:
        x += max_party(lower)

    person.absent = x
    return person.absent
