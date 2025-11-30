class UserMovie:
    def __init__(self, user_id: int, movie_id: int,  rating: int, favorite=False, watched=False, to_watch=False):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.favorite = favorite
        self.watched = watched
        self.to_watch = to_watch
