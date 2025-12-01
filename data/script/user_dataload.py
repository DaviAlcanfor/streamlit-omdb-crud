from faker import Faker

from util.connection import connect
from util.log import get_logger

log = get_logger(__name__)
fake = Faker()

INSERT = "INSERT INTO user_client (name, email, password, icon) VALUES (%s, %s, %s, %s)"

try:
    conn = connect()
    log.info("Database connected.")

except Exception:
    log.exception("Error while connecting.")
    

def insert_user():
    
    try:
        name = fake.name()
        email = fake.email()
        password = fake.password()
        icon = fake.image_url()
        
        with conn.cursor() as cur:
            cur.execute(
                INSERT,
                (name, email, password, icon)
            )
            conn.commit()
        
        return f"Inserted user '{name}'"
        
    except Exception as e:
        log.exception("Error inserting user.")
        

def dataload(quant: int):
    
    for i in range(quant):
        
        try:
            log.info(insert_user() + f" [{i+1}]")
            
        except Exception:
            log.exception(f"Error during user insertion. [{i+1}]")
        
    conn.close()
    log.info("Connection closed.")
    
dataload(100)