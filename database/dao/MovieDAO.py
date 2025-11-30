from model import Movie
from decorators import db_operation

INSERT = "INSERT INTO movies (title, year, age_group, description, rating, duration, genre) VALUES (%s, %s, %s, %s, %s, %s, %s)"
SELECT_ALL = "SELECT * FROM movies"
SELECT = "SELECT * FROM movies WHERE id = %s"
DELETE = "DELETE FROM movies WHERE id = %s"
UPDATE = "UPDATE movies SET title=%s, year=%s, age_group=%s, description=%s,rating=%s, duration=%s, genre=%s WHERE id=%s"

class MovieDAO:
    def __init__(self):
        self.conn = None
    
    
    @db_operation
    def create(self, movie: Movie):
        """
        Creates a new movie and stores it into database
        
        Args:
            movie: Movie object
        """
        with self.conn.cursor() as cur:
            cur.execute(
                INSERT, 
                (
                 movie.title,  
                 movie.year, 
                 movie.age_group, 
                 movie.description, 
                 movie.rating, 
                 movie.duration, 
                 movie.genre
                )
            )
    
    @db_operation 
    def delete(self, id: int):
        """
        Deletes a movie from database based on the receiving id
        
        Args:
            id: int
        """
        with self.conn.cursor() as cur:
            cur.execute( DELETE, [id])
            

            
    @db_operation
    def get(self, id: int):
        """
        Gets a movie based upon the received ID

        Args:
            id: int 
            
        Returns:
            Movie object        
        """
        
        with self.conn.cursor() as cur:
            
            cur.execute( SELECT, [id])
            row = cur.fetchone()
            
            return Movie(*row)


    @db_operation
    def get_all(self):
        """
        Gets all movies from the database

        Returns:
            list of Movie objects
        """
        with self.conn.cursor() as cur:
            
            cur.execute(SELECT_ALL)
            rows = cur.fetchall()
            
            return [Movie(*row[1:]) for row in rows]
    
    
    @db_operation            
    def update(self, id: int, movie: Movie):
        """
        Updates a movie in the database based on the receiving id
        
        Args:
            id: int
            movie: Movie object
        """
        with self.conn.cursor() as cur:
            cur.execute(
                UPDATE,
                (
                    movie.title,
                    movie.year,
                    movie.age_group,
                    movie.description,
                    movie.rating,
                    movie.duration,
                    movie.genre,
                    id
                )
            )