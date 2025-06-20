def brute_force(username):
    print(f"Starting brute force on {username}...")
    passwords = ["123456", "admin", "password", "letmein"]
    for pwd in passwords:
        print(f"Trying password: {pwd}")
        if pwd == "admin":
            print(f"Password found: {pwd}")
            return
    print("Password not found.")