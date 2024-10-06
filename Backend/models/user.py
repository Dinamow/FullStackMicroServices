# app/models/user.py

fake_users_db = {
    "user1": {
        "username": "user1",
        "full_name": "User One",
        "email": "user1@example.com",
        "hashed_password": "$2b$12$K9szgHsz4HX0Lq3z1vL5CO0GBO4CmV/MdUbV/rpXTg8vT4S5g5.1G",  # bcrypt hash for "password"
        "disabled": False,
    }
}
