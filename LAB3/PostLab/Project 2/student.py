import random

class Student(object):
    def __init__(self, name, number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def get_name(self):
        return self.name

    def set_score(self, i, score):
        self.scores[i - 1] = score

    def get_score(self, i):
        return self.scores[i - 1]

    def get_average(self):
        return sum(self.scores) / len(self.scores)

    def get_high_score(self):
        return max(self.scores)

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __str__(self):
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))


def main():
    students = [
        Student("Larrline", 5),
        Student("Syrah", 5),
        Student("Jhianne", 5),
    ]

    # Set scores for each student
    for student in students:
        for i in range(1, 6):
            student.set_score(i, random.randint(60, 100))

    random.shuffle(students)

    print("Unsorted list:")
    for student in students:
        print(student)
        print("-" * 20)

    students.sort()

    print("\nSorted list:")
    for student in students:
        print(student)
        print("-" * 20)


if __name__ == "__main__":
    main()
