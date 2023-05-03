from mysqlconnection import connectToMySQL
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users').query_db(query)
        users = []
        for i in results:
            users.append(cls(i))
        return users
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        results = connectToMySQL('users').query_db(query,data)
        return results


    @classmethod
    def get_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s";
        result = connectToMySQL('users').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s,last_name = %(last_name)s,email = %(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users').query_db(query,data)

    @classmethod
    def deleteuser(cls,data):
        query = "DELETE from users WHERE id = %(id)s;"
        return connectToMySQL('users').query_db(query,data)