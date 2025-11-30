from ..model.Movie import Movie
from ..model.User import User
from util.decorators import db_operation
from util.log import get_logger

import inspect
import pandas as pd

log = get_logger(__name__)

MOVIE_COLUMNS = [p for p in inspect.signature(Movie.__init__).parameters if p != 'self']
USER_COLUMNS = [p for p in inspect.signature(User.__init__).parameters if p != 'self']

MOVIES_IN_DATABASE = "SELECT COUNT(*) FROM movies"
USERS_IN_DATABASE = "SELECT COUNT(*) FROM users"
TOP_RATED_MOVIES = """SELECT * FROM movies ORDER BY rating DESC LIMIT 3"""
MOST_WATCHED_MOVIES = "SELECT m.* FROM movies m JOIN user_movies um ON m.id = um.movie_id WHERE um.watched = TRUE GROUP BY m.id ORDER BY COUNT(um.movie_id) DESC LIMIT 3"

class MainDAO:
    def __init__(self):
        self.conn = None
        
    @db_operation
    def get_movies_count(self) -> int:
        """
        Gets the total number of movies in the database
        
        Returns:
            int
        """
        with self.conn.cursor() as cur:
            cur.execute(MOVIES_IN_DATABASE)
            result = cur.fetchone()
            return result[0]
        
    @db_operation
    def get_users_count(self) -> int:
        """
        Gets the total number of users in the database
        
        Returns:
            int
        """
        with self.conn.cursor() as cur:
            cur.execute(USERS_IN_DATABASE)
            result = cur.fetchone()
            return result[0]
        
    
    @db_operation
    def get_top_rated_movies(self) -> pd.DataFrame:
        """
        Gets the top 3 rated movies from the database
        
        Returns:
            pd.DataFrame
        """
        with self.conn.cursor() as cur:
            cur.execute(TOP_RATED_MOVIES)
            rows = cur.fetchall()
            return pd.DataFrame(rows, columns=MOVIE_COLUMNS)
           