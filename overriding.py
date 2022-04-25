class Employee:
    def set_number_of_working_hours(self):
        self.number_of_working_hours = 40

    def display_number_of_working_hours(self):
        print(self.number_of_working_hours)


class Trainee(Employee):
    def set_number_of_working_hours(self):
        self.number_of_working_hours = 45

    def reset_number_of_working_hours(self):
        super().set_number_of_working_hours()




emp = Employee()
emp.set_number_of_working_hours()
emp.display_number_of_working_hours()

trainee = Trainee()
trainee.set_number_of_working_hours()
trainee.display_number_of_working_hours()

