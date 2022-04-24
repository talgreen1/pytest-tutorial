class User:
    def __init__(self, name, email, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f'User {self.name}, works as {self.current_job_title}, email: {self.email}')

    @staticmethod
    def say_hello():
        print('Hello')

