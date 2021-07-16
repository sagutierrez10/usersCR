from mysqlconnection import connectToMySQL

class Users:
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
        
        results = connectToMySQL('users_schema').query_db(query)
        
        users = []
    
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = { 'id' : id }
        user = connectToMySQL('users_schema').query_db(query, data)[0]
        return user

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def setUser(CLS, user):
        query= 'UPDATE users SET first_name = %(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s;'
        data = { 'first_name' : user["first_name"], 'last_name' : user["last_name"], 'email' : user["email"], "id": user["id"]}
        print('UPDATE', connectToMySQL('users_schema').query_db( query, data ))

    @classmethod
    def deleteUser(cls, data):
        query = 'DELETE FROM users where id= %(id)s;'
        connectToMySQL('users_schema').query_db(query, data)