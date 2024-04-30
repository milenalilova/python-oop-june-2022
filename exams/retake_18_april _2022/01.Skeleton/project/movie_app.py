# 121/150 in Judje. Need to find mistake


from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        user = self.__find_user_by_username(username)
        if user is not None:
            raise Exception('User already exists!')
        user = User(username, age)
        self.users_collection.append(user)
        return f'{username} registered successfully.'

    def upload_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        if not user:
            raise Exception('This user does not exist!')

        if movie in self.movies_collection:
            raise Exception('Movie already added to the collection!')

        if username != movie.owner.username:
            raise Exception(f'{user.username} is not the owner of the movie {movie.title}!')

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__find_user_by_username(username)

        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')
        if username != movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        for attribute, new_value in kwargs.items():
            setattr(movie, attribute, new_value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')

        if username != movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return 'No movies found.'

        sorted_movies_collection = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        result = [m.details() for m in sorted_movies_collection]
        return '\n'.join(m for m in result)

    def __str__(self):
        usernames = [u.username for u in self.users_collection]
        output = 'All users: No users.' if not self.users_collection else f"All users: {', '.join(usernames)}" + '\n'

        movies = [m.title for m in self.movies_collection]
        output += 'All movies: No movies.' if not self.movies_collection else f"All movies: {', '.join(movies)}"

        return output.strip()

    def __find_user_by_username(self, username):
        for u in self.users_collection:
            if u.username == username:
                return u
