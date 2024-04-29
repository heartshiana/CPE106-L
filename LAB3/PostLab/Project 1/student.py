class Student:
    def __init__(self, name, number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def get_student_name(self):
        return self.name

    def set_student_score(self, i, score):
        self.scores[i - 1] = score

    def get_student_score(self, i):
        return self.scores[i - 1]

    def get_average_student(self):
        return sum(self.scores) / len(self.scores)

    def get_high_score_student(self):
        return max(self.scores)

    def compare_names(self, other):
        return self.name == other.name

    def is_less_than(self, other):
        return self.name < other.name

    def is_greater_than_or_equal_to(self, other):
        return self.name >= other.name

    def to_string(self):
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores))


def main():
    student1 = Student("Heart", 5)
    student2 = Student("Hannah", 5)

    print("Equality test:", student1.compare_names(student2))
    print("Less than test:", student1.is_less_than(student2))
    print("Greater than or equal to test:", student1.is_greater_than_or_equal_to(student2))


if __name__ == "__main__":
    main()
