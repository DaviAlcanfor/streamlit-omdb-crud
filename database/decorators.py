from config import connect

def with_connection(func):
    """Starts a connection and closes it after the function call"""
    
    def wrapper(self, *args, **kwargs):
        
        conn = connect()
        try:
            self.conn = conn
            return func(self, *args, **kwargs)

        finally:
            conn.close()
    return wrapper