class Student:
    def __init__(self, name: str, surname: str, rating_list: list):
        self.name = name
        self.surname = surname
        self.rating_list = rating_list

    def __len__(self):
        return len(self.rating_list)

    def __str__(self):
        return print({self.name})


def sortt(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if len(array[j]) > len(array[j + 1]):
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


misha = Student("Misha", "Sahan", [1,5,7,3])
petro = Student("Petro", "Dron", [1,4,7,9,6])
ivan = Student("Ivan","Vasyliv",[6,7])
diana = Student("Diana", "Tokaruk", [5,3,8])
studenty = [misha,petro,diana,ivan]

sortt(studenty)
