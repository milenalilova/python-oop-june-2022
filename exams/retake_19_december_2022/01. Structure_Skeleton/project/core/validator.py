class Validator:
    @staticmethod
    def validate_non_empty_string_or_white_space(value, message):
        if not value.strip():
            raise ValueError(message)

    @staticmethod
    def validate_min_length_or_non_white_spaces(value, message):
        if value.strip is None or len(value) < 2:
            raise ValueError(message)

    @staticmethod
    def validate_non_empty_string(value, message):
        if not value:
            raise ValueError(message)

    @staticmethod
    def validate_value_above_num(value, num, message):
        if value < num:
            raise ValueError(message)

    @staticmethod
    def validate_genre_is_valid(genre, genre_list, message):
        if genre not in genre_list:
            raise ValueError(message)

    @staticmethod
    def validate_band_can_start_concert(band, message):
        can_start = True

        member_types = {
            'Singer': 0,
            'Drummer': 0,
            'Guitarist': 0
        }

        def count_band_members_types(band):
            for member in band.members:
                member_types[member.type] += 1

        count_band_members_types(band)

        for member_type, count in member_types.items():
            if count < 1:
                can_start = False
                raise Exception(message)

        return can_start

    @staticmethod
    def validate_band_can_play_at_concert(band, concert):

        can_play_at_concert = {
            'Rock': True,
            'Metal': True,
            'Jazz': True,
        }

        skills_needed = {
            'Rock': {
                'Drummer': ['play the drums with drumsticks'],
                'Singer': ['sing high pitch notes'],
                'Guitarist': ['play rock'],
            },
            'Metal': {
                'Drummer': ['play the drums with drumsticks'],
                'Singer': ['sing low pitch notes'],
                'Guitarist': ['play metal'],
            },
            'Jazz': {
                'Drummer': ['play the drums with drum brushes'],
                'Singer': ['sing high pitch notes', 'sing low pitch notes'],
                'Guitarist': ['play jazz']
            },
        }

        for member in band.members:
            required_skills = skills_needed[concert.genre].get(member.type)
            if any(skill not in member.skills for skill in required_skills):
                can_play_at_concert[concert.genre] = False
                break

            # for skill in skills_needed[concert.genre][member.type]:
            #     if skill not in member.skills:
            #         can_play_at_concert[concert.genre] = False
            #         break

        return can_play_at_concert[concert.genre]
