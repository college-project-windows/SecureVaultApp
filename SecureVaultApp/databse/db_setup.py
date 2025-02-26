from pymongo import MongoClient

# MongoDB connection string (Replace with actual connection URL if using remote MongoDB Atlas)
MONGO_URI = "mongodb://localhost:27017"

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Create or get database
db = client["SecureOrgApp"]

# Collections
users_collection = db["users"]
files_collection = db["files"]
chats_collection = db["chats"]

print("Connected to MongoDB Successfully!")
