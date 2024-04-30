from project.validators import validate_non_empty_string, validate_value_above_num


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        validate_non_empty_string(value, 'Invalid username!')
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        validate_value_above_num(value, 6, 'Users under the age of 6 are not allowed!')
        self.__age = value

    def __str__(self):
        output = f"Username: {self.__username}, Age: {self.__age}" + '\n'
        if not self.movies_liked:
            output += 'No movies liked.' + '\n'
        else:
            output += 'Liked movies:' + '\n' + '\n'.join([m.details for m in self.movies_liked])

        if not self.movies_owned:
            output += 'No movies owned.' + '\n'
        else:
            output += 'Owned movies:' + '\n' + '\n'.join(m.details for m in self.movies_owned)

        return output.strip()
