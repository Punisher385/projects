class DenysExtended(Denys):
    def __init__(self, first_name=None, last_name=None, birth_year=None,
                 university=None, specialty=None, student_id=None):
        super().__init__(first_name, last_name, birth_year)
        self.university = university
        self.specialty = specialty
        self.student_id = student_id

    def get_full_info(self):

        return {
            "Ім'я": self.first_name,
            "Прізвище": self.last_name,
            "Рік народження": self.birth_year,
            "Університет": self.university,
            "Спеціальність": self.specialty,
            "Студентський квиток": self.student_id
        }

    def _generate_email(self):

        if self.first_name and self.last_name and self.university:
            return f"{self.first_name.lower()}.{self.last_name.lower()}@{self.university.lower()}.edu"
        return None