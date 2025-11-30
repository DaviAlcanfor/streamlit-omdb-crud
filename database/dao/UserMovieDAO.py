from model import UserMovie
from decorators import db_operation

INSERT = "INSERT INTO user_movies (user_id, movie_id, rating, favorite, watched, to_watch) VALUES (%s, %s, %s, %s, %s, %s)"
SELECT_ALL = "SELECT * FROM user_movies"
SELECT = "SELECT * FROM user_movies WHERE user_id = %s AND movie_id = %s"
SELECT_BY_USER = "SELECT * FROM user_movies WHERE user_id = %s"
SELECT_BY_MOVIE = "SELECT * FROM user_movies WHERE movie_id = %s"
SELECT_USER_FAVORITES = "SELECT * FROM user_movies WHERE user_id = %s AND favorite = TRUE"
SELECT_USER_WATCHED = "SELECT * FROM user_movies WHERE user_id = %s AND watched = TRUE"
SELECT_USER_TO_WATCH = "SELECT * FROM user_movies WHERE user_id = %s AND to_watch = TRUE"
DELETE = "DELETE FROM user_movies WHERE user_id = %s AND movie_id = %s"
UPDATE = "UPDATE user_movies SET rating=%s, favorite=%s, watched=%s, to_watch=%s WHERE user_id=%s AND movie_id=%s"

class UserMovieDAO:
    def __init__(self):
        self.conn = None
    
    
    @db_operation
    def create(self, user_movie: UserMovie):
        """
        Creates a new user-movie relationship and stores it into database
        
        Args:
            user_movie: UserMovie object
        """
        with self.conn.cursor() as cur:
            cur.execute(
                INSERT, 
                (
                 user_movie.user_id,  
                 user_movie.movie_id, 
                 user_movie.rating, 
                 user_movie.favorite,
                 user_movie.watched,
                 user_movie.to_watch
                )
            )
    
    @db_operation 
    def delete(self, user_id: int, movie_id: int):
        """
        Deletes a user-movie relationship from database
        
        Args:
            user_id: int
            movie_id: int
        """
        with self.conn.cursor() as cur:
            cur.execute(DELETE, [user_id, movie_id])
            

            
    @db_operation
    def get(self, user_id: int, movie_id: int):
        """
        Gets a user-movie relationship based upon the user_id and movie_id

        Args:
            user_id: int
            movie_id: int 
            
        Returns:
            UserMovie object        
        """
        
        with self.conn.cursor() as cur:
            
            cur.execute(SELECT, [user_id, movie_id])
            row = cur.fetchone()
            
            return UserMovie(*row) if row else None


    @db_operation
    def get_by_user(self, user_id: int):
        """
        Gets all movies associated with a specific user

        Args:
            user_id: int
            
        Returns:
            list of UserMovie objects
        """
        with self.conn.cursor() as cur:
            
            cur.execute(SELECT_BY_USER, [user_id])
            rows = cur.fetchall()
            
            return [UserMovie(*row) for row in rows]


    @db_operation
    def get_by_movie(self, movie_id: int):
        """
        Gets all users associated with a specific movie

        Args:
            movie_id: int
            
        Returns:
            list of UserMovie objects
        """
        with self.conn.cursor() as cur:
            
            cur.execute(SELECT_BY_MOVIE, [movie_id])
            rows = cur.fetchall()
            
            return [UserMovie(*row) for row in rows]


    @db_operation
    def get_user_favorites(self, user_id: int):
        """
        Gets all favorite movies for a specific user

        Args:
            user_id: int
            
        Returns:
            list of UserMovie objects
        """
        with self.conn.cursor() as cur:
            
            cur.execute(SELECT_USER_FAVORITES, [user_id])
            rows = cur.fetchall()
            
            return [UserMovie(*row) for row in rows]


    @db_operation
    def get_user_watched(self, user_id: int):
        """
        Gets all watched movies for a specific user

        Args:
            user_id: int
            
        Returns:
            list of UserMovie objects
        """
        with self.conn.cursor() as cur:
            
            cur.execute(SELECT_USER_WATCHED, [user_id])
            rows = cur.fetchall()
            
            return [UserMovie(*row) for row in rows]


    @db_operation
    def get_user_to_watch(self, user_id: int):
        """
        Gets all to-watch movies for a specific user

        Args:
            user_id: int
            
        Returns:
            list of UserMovie objects
        """
        with self.conn.cursor() as cur:
            
            cur.execute(SELECT_USER_TO_WATCH, [user_id])
            rows = cur.fetchall()
            
            return [UserMovie(*row) for row in rows]


    @db_operation
    def get_all(self):
        """
        Gets all user-movie relationships from the database

        Returns:
            list of UserMovie objects
        """
        with self.conn.cursor() as cur:
            
            cur.execute(SELECT_ALL)
            rows = cur.fetchall()
            
            return [UserMovie(*row) for row in rows]
    
    
    @db_operation            
    def update(self, user_id: int, movie_id: int, user_movie: UserMovie):
        """
        Updates a user-movie relationship in the database
        
        Args:
            user_id: int
            movie_id: int
            user_movie: UserMovie object
        """
        with self.conn.cursor() as cur:
            cur.execute(
                UPDATE,
                (
                    user_movie.rating,
                    user_movie.favorite,
                    user_movie.watched,
                    user_movie.to_watch,
                    user_id,
                    movie_id
                )
            )