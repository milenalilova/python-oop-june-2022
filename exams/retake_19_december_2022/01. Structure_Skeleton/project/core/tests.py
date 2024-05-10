# Create an instance of ConcertTrackerApp
from project.concert_tracker_app import ConcertTrackerApp

app = ConcertTrackerApp()

# Create musicians
app.create_musician("Singer", "Emily", 25)
app.create_musician("Drummer", "Jack", 30)
app.create_musician("Guitarist", "Oliver", 22)

# Assign skills to musicians
app.musicians[0].learn_new_skill("sing low pitch notes")
app.musicians[0].learn_new_skill("sing high pitch notes")
app.musicians[1].learn_new_skill("play the drums with drum brushes")
app.musicians[2].learn_new_skill("play jazz")

# Create a band
app.create_band("JazzBand")

# Add musicians to the band
app.add_musician_to_band("Emily", "JazzBand")
app.add_musician_to_band("Jack", "JazzBand")
app.add_musician_to_band("Oliver", "JazzBand")

# Create a concert
app.create_concert("Jazz", 40, 8.50, 100, "New York")
print(app.concerts[0].genre)

# Verify the band members
print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
# print(app.bands[0].members[0].type)
# print(app.bands[0].members[0].skills)
# print(app.bands[0].members[1].type)
# print(app.bands[0].members[1].skills)
# print(app.bands[0].members[2].type)
# print(app.bands[0].members[2].skills)
print()
# Start the concert and print the result
print(app.start_concert("New York", "JazzBand"))
