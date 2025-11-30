from ..model.User import User
from util.decorators import db_operation

import pandas as pd

INSERT = "INSERT INTO users (name, email, password, icon) VALUES (%s, %s, %s, %s)"
SELECT_ALL = "SELECT * FROM users"
SELECT = "SELECT * FROM users WHERE id = %s"
SELECT_BY_EMAIL = "SELECT * FROM users WHERE email = %s"
DELETE = "DELETE FROM users WHERE id = %s"
UPDATE = "UPDATE users SET name=%s, email=%s, password=%s, icon=%s WHERE id=%s"

class UserDAO:
    def __init__(self):
        self.conn = None
    
    
    @db_operation
    def create(self, user: User):
        """
        Creates a new user and stores it into database
        
        Args:
            user: User object
        """
        with self.conn.cursor() as cur:
            cur.execute(
                INSERT, 
                (
                 user.name,  
                 user.email, 
                 user.password, 
                 user.icon
                )
            )
    
    @db_operation 
    def delete(self, id: int):
        """
        Deletes a user from database based on the receiving id
        
        Args:
            id: int
        """
        with self.conn.cursor() as cur:
            cur.execute(DELETE, [id])
            

            
    @db_operation
    def get(self, id: int):
        """
        Gets a user based upon the received ID

        Args:
            id: int 
            
        Returns:
            User object        
        """
        
        with self.conn.cursor() as cur:
            
            cur.execute(SELECT, [id])
            row = cur.fetchone()
            
            return User(*row[1:]) if row else None


    @db_operation
    def get_by_email(self, email: str):
        """
        Gets a user based upon the received email

        Args:
            email: str 
            
        Returns:
            User object        
        """
        
        with self.conn.cursor() as cur:
            
            cur.execute(SELECT_BY_EMAIL, [email])
            row = cur.fetchone()
            
            return User(*row[1:]) if row else None


    @db_operation
    def get_all(self):
        """
        Gets all users from the database

        Returns:
            list of User objects
        """
        with self.conn.cursor() as cur:
            
            cur.execute(SELECT_ALL)
            rows = cur.fetchall()
            
            return pd.DataFrame([row[1:] for row in rows], columns=["name","email","password","icon"])
    
    
    @db_operation            
    def update(self, id: int, user: User):
        """
        Updates a user in the database based on the receiving id
        
        Args:
            id: int
            user: User object
        """
        with self.conn.cursor() as cur:
            cur.execute(
                UPDATE,
                (
                    user.name,
                    user.email,
                    user.password,
                    user.icon,
                    id
                )
            )