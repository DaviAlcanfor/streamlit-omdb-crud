from config import connect
from util.log import get_logger

log = get_logger(__name__)

def db_operation(func):
    """Takes care of starting and closing a connection and also handling the operation exceptions"""
    
    def wrapper(self, *args, **kwargs):
        
        try:
            conn = connect()
            self.conn = conn   
            log.info("WRAPPER: Connection started.")
            
            result =  func(self, *args, **kwargs)
            conn.commit()
            log.info("Operation commited.")
            
            return result

        except Exception:
            log.exception("WRAPPER: Error while database operation.")
            
        finally:
            if conn:
                conn.close()
                log.info("WRAPPER: Connection closed.")
            
    return wrapper
    