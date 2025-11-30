from model import Movie
from database.config import connect

# All queries as constants
INSERT = "INSERT INTO movies (title, year, age_group, description, rating, duration, genre) VALUES (%s, %s, %s, %s, %s, %s, %s)"
SELECT_ALL = "SELECT * FROM movies"
SELECT = "SELECT * FROM movies WHERE id = %s"
DELETE = "DELETE FROM movies WHERE id = %s"
UPDATE = "UPDATE movies SET title=%s, year=%s, age_group=%s, description=%s,rating=%s, duration=%s, genre=%s WHERE id=%s"

class MovieDAO:
    def __init__(self):
        pass
    
    def create(self, movie: Movie):
        """
        Creates a new movie and stores it into database
        
        Args:
            movie: Movie object
        """
        
        conn = connect()
        
        with conn.cursor() as cur:
            
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
            conn.commit()
        conn.close()
    
            
    def delete(self, id: int):
        """
        Deletes a movie from database based on the receiving id
        
        Args:
            id: int
        """
        conn = connect()
        
        with conn.cursor() as cur:
            
            cur.execute( DELETE, [id])
            conn.commit()
        conn.close()

            
    
    def get(self, id: int):
        """
        Gets a movie based upon the received ID

        Args:
            id: int 
            
        Returns:
            Movie object        
        """
        conn = connect()
        
        with conn.cursor() as cur:
            
            cur.execute( SELECT, [id])
            row = cur.fetchone()
            
            return Movie(*row)
        conn.close()



    def get_all(self):
        """
        Gets all movies from the database

        Returns:
            list of Movie objects
        """
        
        conn = connect()
        
        with conn.cursor() as cur:
            
            cur.execute(SELECT_ALL)
            rows = cur.fetchall()
            
            return [Movie(*row[1:]) for row in rows]
        conn.close()
    
                
    def update(self, id: int, movie: Movie):
        """
        Updates a movie in the database based on the receiving id
        
        Args:
            id: int
            movie: Movie object
        """
        conn = connect()
        
        with conn.cursor() as cur:
            
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
            conn.commit()
        conn.close()