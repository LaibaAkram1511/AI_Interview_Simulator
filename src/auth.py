import bcrypt
from src.database import SessionLocal, User


def hash_password(password):
    password_bytes = password.encode("utf-8")[:72]
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt).decode("utf-8")


def verify_password(password, hashed_password):
    password_bytes = password.encode("utf-8")[:72]
    return bcrypt.checkpw(password_bytes, hashed_password.encode("utf-8"))


def signup_user(full_name, email, password):
    db = SessionLocal()

    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        db.close()
        return False, "Email already registered."

    hashed_password = hash_password(password)

    user = User(
        full_name=full_name,
        email=email,
        password=hashed_password
    )

    db.add(user)
    db.commit()
    db.close()

    return True, "Account created successfully."


def login_user(email, password):
    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if not user:
        db.close()
        return None, "Invalid email or password."

    if not verify_password(password, user.password):
        db.close()
        return None, "Invalid email or password."

    db.close()
    return user, "Login successful."