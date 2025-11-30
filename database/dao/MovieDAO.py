from ..model.Movie import Movie
from util.decorators import db_operation
from util.log import get_logger

import inspect
import pandas as pd

log = get_logger(__name__)

INSERT = "INSERT INTO movies (title, year, age_group, description, rating, duration, genre) VALUES (%s, %s, %s, %s, %s, %s, %s)"
SELECT_ALL = "SELECT * FROM movies"
SELECT = "SELECT * FROM movies WHERE id = %s"
DELETE = "DELETE FROM movies WHERE id = %s"
UPDATE = "UPDATE movies SET title=%s, year=%s, age_group=%s, description=%s,rating=%s, duration=%s, genre=%s WHERE id=%s"
COLUMNS = [p for p in inspect.signature(Movie.__init__).parameters if p != 'self']

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
            log.info(f"Created movie '{movie.title}'")
    
    @db_operation 
    def delete(self, id: int):
        """
        Deletes a movie from database based on the receiving id
        
        Args:
            id: int
        """
        with self.conn.cursor() as cur:
            cur.execute( DELETE, [id])
            log.info(f"Deleted movie with id {id}")
            

            
    @db_operation
    def get(self, id: int) -> pd.DataFrame:
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
            
            return pd.DataFrame(row, columns=COLUMNS)


    @db_operation
    def get_all(self) -> pd.DataFrame:
        """
        Gets all movies from the database

        Returns:
            list of Movie objects
        """
        with self.conn.cursor() as cur:
            
            cur.execute(SELECT_ALL)
            rows = cur.fetchall()
            log.info(f"Retrieved all movies, count: {len(rows)}")
            
            return pd.DataFrame([row[1:] for row in rows], columns=COLUMNS)
    
    
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
            log.info(f"Updated movie with id {id}")