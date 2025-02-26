from db_setup import users_collection
from bson.objectid import ObjectId
import bcrypt

def hash_password(password):
    """Encrypt user password before storing."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

def create_user(username, password, role):
    """Create a new user in MongoDB."""
    hashed_pw = hash_password(password)
    user_data = {
        "username": username,
        "password": hashed_pw,
        "role": role,  # Example: "Admin", "Manager", "Employee"
        "created_at": datetime.utcnow()
    }
    users_collection.insert_one(user_data)
    print(f"User {username} added successfully!")

# Example usage
if __name__ == "__main__":
    create_user("john_doe", "securePass123", "Manager")
