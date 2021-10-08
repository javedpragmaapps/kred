class Register:
    def __init__(self):
        pass

    @property
    def provider(self):
        return self._provider

    @provider.setter
    def provider(self, value):
        if isinstance(value, str):
            self._provider = value
        else:
            raise ValueError('provider must be a str')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if isinstance(value, str):
            self._email = value
        else:
            raise ValueError('email must be a str')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if isinstance(value, str):
            self._password = value
        else:
            raise ValueError('password must be a str')

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if isinstance(value, str):
            self._phone = value
        else:
            raise ValueError('phone must be a str')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError('name must be a str')

    @property
    def domain(self):
        return self._name

    @domain.setter
    def domain(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError('domain must be a str')




