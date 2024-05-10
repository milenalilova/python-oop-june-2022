from project.band import Band
from project.concert import Concert
from project.core.musician_creator import MusicianCreator
from project.core.validator import Validator


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

        self.musician_creator = MusicianCreator()

    def create_musician(self, musician_type: str, name: str, age: int):
        if any(m.name == name for m in self.musicians):
            raise Exception(f'{name} is already a musician!')

        musician = self.musician_creator.create_musician(musician_type, name, age)

        self.musicians.append(musician)
        return f'{name} is now a {musician_type}.'

    def create_band(self, name: str):
        if any(b.name == name for b in self.bands):
            raise Exception(f'{name} band is already created!')

        band = Band(name)
        self.bands.append(band)
        return f'{name} was created.'

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f'{genre} concert in {place} was added.'

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.__find_object_by_name(musician_name, self.musicians, f"{musician_name} isn't a musician!")
        band = self.__find_object_by_name(band_name, self.bands, f"{band_name} isn't a band!")

        band.members.append(musician)
        return f'{musician_name} was added to {band_name}.'

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.__find_object_by_name(band_name, self.bands, f"{band_name} isn't a band!")

        if not any(m.name == musician_name for m in band.members):
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        musician = self.__find_object_by_name(musician_name, band.members, f"{musician_name} isn't a musician!")
        band.members.remove(musician)
        return f'{musician_name} was removed from {band_name}.'

    def start_concert(self, concert_place: str, band_name: str):
        band = self.__find_object_by_name(band_name, self.bands, f"{band_name} isn't a band!")
        concert = self.__find_concert_by_place(concert_place)

        Validator.validate_band_can_start_concert(
            band,
            f"{band.name} can't start the concert because it doesn't have enough members!")

        can_play_at_concert = Validator.validate_band_can_play_at_concert(band, concert)
        if not can_play_at_concert:
            raise Exception(f'The {band_name} band is not ready to play at the concert!')

        profit = self.__calculate_profit(concert)
        return f'{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}.'

    # def start_concert(self, concert_place: str, band_name: str):
    #     band = self.__find_object_by_name(band_name, self.bands, f"{band_name} isn't a band!")
    #     concert = self.__find_concert_by_place(concert_place)
    #
    #     Validator.validate_band_can_start_concert(
    #         band,
    #         f"{band.name} can't start the concert because it doesn't have enough members!")
    #
    #     if concert.genre == 'Rock':
    #         for band_member in band.members:
    #             if band_member.__class__.__name__ == 'Drummer' and \
    #                      "play the drums with drumsticks" not in band_member.skills:
    #                 raise Exception(f"The {band_name} band is not ready to play at the concert!")
    #             if band_member.__class__.__name__ == 'Singer' and "sing high pitch notes" not in band_member.skills:
    #                 raise Exception(f"The {band_name} band is not ready to play at the concert!")
    #             if band_member.__class__.__name__ == 'Guitarist' and "play rock" not in band_member.skills:
    #                 raise Exception(f"The {band_name} band is not ready to play at the concert!")
    #
    #     elif concert.genre == 'Metal':
    #         for band_member in band.members:
    #             if band_member.__class__.__name__ == 'Drummer' and "play the drums with drumsticks" not in band_member.skills:
    #                 raise Exception(f"The {band_name} band is not ready to play at the concert!")
    #             if band_member.__class__.__name__ == 'Singer' and "sing low pitch notes" not in band_member.skills:
    #                 raise Exception(f"The {band_name} band is not ready to play at the concert!")
    #             if band_member.__class__.__name__ == 'Guitarist' and "play metal" not in band_member.skills:
    #                 raise Exception(f"The {band_name} band is not ready to play at the concert!")
    #
    #     elif concert.genre == 'Jazz':
    #         for band_member in band.members:
    #             if band_member.__class__.__name__ == 'Drummer' \
    #                     and "play the drums with drum brushes" not in band_member.skills:
    #                 raise Exception(f"The {band_name} band is not ready to play at the concert!")
    #             if band_member.__class__.__name__ == 'Singer' \
    #                     and ("sing low pitch notes" not in band_member.skills
    #                          or "sing high pitch notes" not in band_member.skills):
    #                 raise Exception(f"The {band_name} band is not ready to play at the concert!")
    #             if band_member.__class__.__name__ == 'Guitarist' and "play jazz" not in band_member.skills:
    #                 raise Exception(f"The {band_name} band is not ready to play at the concert!")
    #
    #
    #     profit = concert.audience * concert.ticket_price - concert.expenses
    #     return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    @staticmethod
    def __find_object_by_name(obj_name, obj_list, message):
        for obj in obj_list:
            if obj.name == obj_name:
                return obj
        raise Exception(message)

    def __find_concert_by_place(self, concert_place):
        for concert in self.concerts:
            if concert.place == concert_place:
                return concert

    @staticmethod
    def __calculate_profit(concert):
        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return profit


# from project.band import Band
# from project.band_members.drummer import Drummer
# from project.band_members.guitarist import Guitarist
# from project.band_members.singer import Singer
# from project.concert import Concert
#
#
# class ConcertTrackerApp:
#     ALL_MUSICIANS_NAMES = []
#     ALL_BANDS_NAMES = []
#
#     def __init__(self):
#         self.bands = []
#         self.musicians = []
#         self.concerts = []
#
#     def create_musician(self, musician_type: str, name: str, age: int):
#         if musician_type not in ["Guitarist", "Drummer", "Singer"]:
#             raise ValueError("Invalid musician type!")
#         if name in self.ALL_MUSICIANS_NAMES:
#             raise Exception(f"{name} is already a musician!")
#         if musician_type == "Guitarist":
#             musician = Guitarist(name, age)
#         elif musician_type == "Drummer":
#             musician = Drummer(name, age)
#         else:
#             musician = Singer(name, age)
#         self.musicians.append(musician)
#         self.ALL_MUSICIANS_NAMES.append(name)
#         return f"{name} is now a {musician_type}."
#
#     def create_band(self, name: str):
#         if name in self.ALL_BANDS_NAMES:
#             raise Exception(f"{name} band is already created!")
#         band = Band(name)
#         self.bands.append(band)
#         self.ALL_BANDS_NAMES.append(name)
#         return f"{name} was created."
#
#     def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
#         for concert in self.concerts:
#             if concert.place == place:
#                 raise Exception(f"{place} is already registered for {concert.genre} concert!")
#         concert = Concert(genre, audience, ticket_price, expenses, place)
#         self.concerts.append(concert)
#         return f"{genre} concert in {place} was added."
#
#     def __find_musician_by_name(self, name: str):
#         for musician in self.musicians:
#             if musician.name == name:
#                 return musician
#         else:
#             raise Exception(f"{name} isn't a musician!")
#
#     @staticmethod
#     def __find_added_to_band_musician_by_name(band, name: str):
#         for musician in band.members:
#             if musician.name == name:
#                 return musician
#         else:
#             raise Exception(f"{name} isn't a member of {band.name}!")
#
#     def __find_band_by_name(self, name: str):
#         for band in self.bands:
#             if band.name == name:
#                 return band
#         else:
#             raise Exception(f"{name} isn't a band!")
#
#     def __find_concert_by_place(self, place: str):
#         for concert in self.concerts:
#             if concert.place == place:
#                 return concert
#
#     def add_musician_to_band(self, musician_name: str, band_name: str):
#         musician = self.__find_musician_by_name(musician_name)
#         band = self.__find_band_by_name(band_name)
#         band.members.append(musician)
#         return f"{musician_name} was added to {band_name}."
#
#     def remove_musician_from_band(self, musician_name: str, band_name: str):
#         band = self.__find_band_by_name(band_name)
#         musician = self.__find_added_to_band_musician_by_name(band, musician_name)
#         band.members.remove(musician)
#         return f"{musician_name} was removed from {band_name}."
#
#     def start_concert(self, concert_place: str, band_name: str):
#         band = self.__find_band_by_name(band_name)
#         concert = self.__find_concert_by_place(concert_place)
#         for musician_type in ["Drummer", "Singer", "Guitarist"]:
#             if not any(
#                     filter(
#                         lambda x: x.__class__.__name__ == musician_type,
#                         band.members
#                     )
#             ):
#                 raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
#
#         if concert.genre == 'Rock':
#             for band_member in band.members:
#                 if band_member.__class__.__name__ == 'Drummer' and \
#                          "play the drums with drumsticks" not in band_member.skills:
#                     raise Exception(f"The {band_name} band is not ready to play at the concert!")
#                 if band_member.__class__.__name__ == 'Singer' and "sing high pitch notes" not in band_member.skills:
#                     raise Exception(f"The {band_name} band is not ready to play at the concert!")
#                 if band_member.__class__.__name__ == 'Guitarist' and "play rock" not in band_member.skills:
#                     raise Exception(f"The {band_name} band is not ready to play at the concert!")
#
#         elif concert.genre == 'Metal':
#             for band_member in band.members:
#                 if band_member.__class__.__name__ == 'Drummer' and "play the drums with drumsticks" not in band_member.skills:
#                     raise Exception(f"The {band_name} band is not ready to play at the concert!")
#                 if band_member.__class__.__name__ == 'Singer' and "sing low pitch notes" not in band_member.skills:
#                     raise Exception(f"The {band_name} band is not ready to play at the concert!")
#                 if band_member.__class__.__name__ == 'Guitarist' and "play metal" not in band_member.skills:
#                     raise Exception(f"The {band_name} band is not ready to play at the concert!")
#
#         elif concert.genre == 'Jazz':
#             for band_member in band.members:
#                 if band_member.__class__.__name__ == 'Drummer' \
#                         and "play the drums with drum brushes" not in band_member.skills:
#                     raise Exception(f"The {band_name} band is not ready to play at the concert!")
#                 if band_member.__class__.__name__ == 'Singer' \
#                         and ("sing low pitch notes" not in band_member.skills
#                              or "sing high pitch notes" not in band_member.skills):
#                     raise Exception(f"The {band_name} band is not ready to play at the concert!")
#                 if band_member.__class__.__name__ == 'Guitarist' and "play jazz" not in band_member.skills:
#                     raise Exception(f"The {band_name} band is not ready to play at the concert!")
#
#
#         profit = concert.audience * concert.ticket_price - concert.expenses
#         return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
