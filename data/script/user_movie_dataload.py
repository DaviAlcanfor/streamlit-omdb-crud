from faker import Faker
import random

from util.connection import connect
from util.log import get_logger
from database.dao.MainDAO import MainDAO

log = get_logger(__name__)
fake = Faker()
dao = MainDAO()

INSERT = "INSERT INTO user_movies (user_id, movie_id, favorite, watched, to_watch, rating) VALUES (%s, %s, %s, %s, %s, %s)"
N_USERS = dao.get_users_count()
N_MOVIES = dao.get_movies_count()

try:
    conn = connect()
    log.info("Database connected.")

except Exception:
    log.exception("Error while connecting.")
    

def insert_link():
    
    try:
        user_id = random.randint(1, N_USERS)
        movie_id = random.randint(1, N_MOVIES)
        favorite = random.choice([True, False])
        watched = random.choice([True, False])
        to_watch = random.choice([True, False])
        rating = random.uniform(1.0, 10.0)
        
        with conn.cursor() as cur:
            cur.execute(
                INSERT,
                (user_id, movie_id, favorite, watched, to_watch, rating)
            )
            conn.commit()
        
        return f"Inserted '{user_id}'-'{movie_id}' link"
        
    except Exception as e:
        log.exception("Error inserting link.")
        

def dataload(quant: int):
    
    for i in range(quant):
        
        try:
            log.info(insert_link() + f" [{i+1}]")
            
        except Exception:
            log.exception(f"Error during link insertion. [{i+1}]")
        
    conn.close()
    log.info("Connection closed.")
    
dataload(100)