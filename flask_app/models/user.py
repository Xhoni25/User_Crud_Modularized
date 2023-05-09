from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db_name = 'user_cr'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('user_cr').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        
        if results:
        # Iterate over the db results and create instances of friends with cls.
            for user in results:
                users.append( cls(user) )
            return users
    

#CREATE
    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE users.id = %(id)s;"
        results = connectToMySQL('user_cr').query_db(query, data)
        if results:
            return results[0]  
        return False

    #CREATE
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES ( %(first_name)s, %(last_name)s, %(email)s);"
        response1 = connectToMySQL(cls.db_name).query_db(query, data)  
        query2 = "SELECT id FROM users ORDER BY ID DESC LIMIT 1;"
        results2 = connectToMySQL(cls.db_name).query_db(query2)  
        if results2:
            return results2[0]
        return False

    #DELETE
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE users.id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)  
    
    #UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET users.first_name = %(first_name)s, users.last_name=%(last_name)s, users.email=%(email)s WHERE users.id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)  
    
    