import os, random
from dotenv import load_dotenv
from util.data import get_api_data
from database.config import connect

load_dotenv()

INSERT = "INSERT INTO movies (title, year, age_group, description, rating, duration, genre) VALUES (%s, %s, %s, %s, %s, %s, %s)"
API_KEY = os.getenv("API_KEY")
AGE_GROUPS = [10, 12, 14, 16, 18]


conn = connect()


def fetch_movie():
    
    # The goal here is to get a random movie to supply the number of movies needed
    id = random.randint(1000000, 9999999)

    url = f"http://www.omdbapi.com/?i=tt{id}&apikey={API_KEY}"
    data = get_api_data(url)

    if data.get("Response") == "False":
        return None
    return data



def insert_movie(data):
    
    title = data.get("Title")
    year = int(data.get("Year", 0))
    age_group = random.choice(AGE_GROUPS)
    description = data.get("Plot") or ""
    rating = float(data.get("imdbRating", 0) or 0)
    duration = int(data.get("Runtime", "0 min").split()[0])
    genre = data.get("Genre") or ""
    
    with conn.cursor() as cur:
        cur.execute(
            INSERT,
            (title, year, age_group, description, rating, duration, genre)
        )
        conn.commit()
    print(f"Inserted '{title}'.")



def dataload(quant: int):
    
    for i in range(quant):
        
        data = fetch_movie()
        if not data:
            continue
        
        try:
            insert_movie(data)
        except Exception as e:
            print(f"Error occured while inserting movie[{i+1}].")
            
    conn.close()    
        
dataload(100)