from models import User  
from storage import Storage

def add_user(name, user_id, storage):
    """Adds a new user to the system."""
    users = storage.load_users()
    if not any(user.user_id == user_id for user in users):  # Check if user ID already exists
        users.append(User(name, user_id))
        storage.save_users(users)
        print("User added successfully.")
    else:
        print("User with ID already exists.")

def list_users(storage):
    """Lists all users in the system."""
    users = storage.load_users()
    for user in users:
        print(user)

def update_user(user_id, new_name, storage):
    """Updates a user's information."""
    users = storage.load_users()
    found_user = next((user for user in users if user.user_id == user_id), None)
    if found_user:
        found_user.name = new_name
        storage.save_users(users)
        print(f"User with ID {user_id} updated successfully.")
    else:
        print(f"User with ID {user_id} not found.")

def delete_user(user_id, storage):
    """Deletes a user from the system."""
    users = storage.load_users()
    users = [user for user in users if user.user_id != user_id]  # Remove user with the given ID
    storage.save_users(users)
    print(f"User with ID {user_id} deleted successfully.")

def search_users(name_or_id, storage):
    """Searches for users by name or ID."""
    users = storage.load_users()
    matching_users = [user for user in users if name_or_id.lower() in user.name.lower() or str(user.user_id) == name_or_id]
    for user in matching_users:
        print(user)
