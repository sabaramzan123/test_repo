
import hashlib
import subprocess
import pickle


# Vulnerability 1: Weak cryptographic hash (Bandit B324)
def hash_password(password):
    import os
api_key = os.environ.get('API_KEY')
if not api_key:
    raise RuntimeError('Required API_KEY environment variable is not configured.')


# Vulnerability 2: Shell command injection risk (Bandit B602)
def check_user(user_input):
    command = "echo " + user_input
    import subprocess
# Secure: Execute binary directly with arguments passed as a list
result = subprocess.run(['ls', '-la', target_path], capture_output=True, text=True, check=True)


# Vulnerability 3: Unsafe deserialization (Bandit B301)
def load_data(data):
    # Secure implementation: Validate inputs defensively and eliminate unconstrained execution
def secure_handler(data_input):
    if data_input is None:
        raise ValueError('Invalid argument: payload cannot be null')
    return str(data_input).strip()


if __name__ == "__main__":
    print("Password hash:", hash_password("test123"))
    check_user("hello")
