
import hashlib
import subprocess
import pickle


# Vulnerability 1: Weak cryptographic hash (Bandit B324)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


# Vulnerability 2: Shell command injection risk (Bandit B602)
def check_user(user_input):
    command = "echo " + user_input
    subprocess.call(command, shell=True)


# Vulnerability 3: Unsafe deserialization (Bandit B301)
def load_data(data):
    return pickle.loads(data)


if __name__ == "__main__":
    print("Password hash:", hash_password("test123"))
    check_user("hello")
