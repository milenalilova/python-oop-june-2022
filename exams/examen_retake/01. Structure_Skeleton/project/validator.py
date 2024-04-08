class Validator:
    @staticmethod
    def validate_phone_number(number: str):
        for ch in number:
            if number[0] != '0':
                raise ValueError('Invalid phone number!')
            elif len(number) != 10:
                raise ValueError('Invalid phone number!')
            elif not ch.isdigit():
                raise ValueError('Invalid phone number!')

        return number

