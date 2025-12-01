import os, random, time
from dotenv import load_dotenv

from util.connection import connect
from util.data import get_api_data, validate_float, validate_int
from util.log import get_logger


load_dotenv()
log = get_logger(__name__)

INSERT = "INSERT INTO movies (title, year, age_group, description, rating, duration, genre) VALUES (%s, %s, %s, %s, %s, %s, %s)"
API_KEY = os.getenv("API_KEY")
AGE_GROUPS = [10, 12, 14, 16, 18]


try:
    conn = connect()
    log.info("Database connected.")

except Exception:
    log.exception("Error while connecting.")
    
    
def fetch_movie():
    
    # The goal here is to get a random movie to supply the number of movies needed
    id = random.randint(1000000, 9999999)

    url = f"http://www.omdbapi.com/?i=tt{id}&apikey={API_KEY}"
    data = get_api_data(url)

    if data.get("Response") == "False":
        return None
    return data



def insert_movie(data):
    
    try:
        title = data.get("Title")
        year = validate_int(data.get("Year", 0))
        age_group = random.choice(AGE_GROUPS)
        description = data.get("Plot") or ""
        rating = validate_float(data.get("imdbRating", 0))
        duration = validate_int(data.get("Runtime", "0 min").split()[0])
        genre = data.get("Genre") or ""
        
        with conn.cursor() as cur:
            cur.execute(
                INSERT,
                (title, year, age_group, description, rating, duration, genre)
            )
            conn.commit()
        
        return f"Inserted {title}"
        
    except Exception:
        log.exception("Error.")
        return None

def dataload(quant: int):
    
    for i in range(quant):
        
        data = fetch_movie()
        if not data:
            log.warning(f"Could not fetch data [{i+1}]")
            continue
        
        try:
            log.info(insert_movie(data) + f" [{i+1}]")
        
        except Exception:
            log.exception(f"Error error while inserting movie[{i+1}].")
        
        time.sleep(0.3)
            
    conn.close()
    log.info("Connection closed")
        
dataload(100)