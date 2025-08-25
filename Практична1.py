class Denys:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculate_course(self):
        if self.birth_year is None:
            return None
        age = 2025 - self.birth_year
        course = age - 17
        return course if 1 <= course <= 6 else None

    def get_name_list(self):
        return [self.first_name, self.last_name]