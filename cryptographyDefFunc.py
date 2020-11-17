from cryptography.fernet import Fernet

# Sets key for specific user
def set_key(username):
    # Every user has its own special key to encrypt and decrypt the info
    # Here with the username we get a key for that specific user
    key = Fernet.generate_key()
    distraction_name = "@@@!!!llave" + username + "k!!!@@@"  # If anyone is watching the files I hope all the symbols will distract him/her
    file = open(distraction_name + ".key", "wb")
    file.write(key)  # Write the key to the file
    file.close()

# Encrypts username and password
def encrypt_some(username, password):
    # Read key / Get the key from the file
    distraction_name = "@@@!!!llave" + username + "k!!!@@@"
    file = open(distraction_name + ".key", "rb")
    key = file.read()  # The key will be type 'bytes'
    file.close()
    # Encode username
    encoded_username = username.encode()
    # Encrypt username
    f = Fernet(key)
    encrypted_username = f.encrypt(encoded_username)
    # Encode password
    encoded_password = password.encode()
    # Encrypt password
    f = Fernet(key)
    encrypted_password = f.encrypt(encoded_password)
    encrypted_list = (encrypted_username, encrypted_password)
    return  encrypted_list

# Encrypts all info from the user
def encrypt_all(username, user, password, email, info):
    # The difference between this and encrypt is that this encrypts all info
    # Read key / Get the key from the file
    distraction_name = "@@@!!!llave" + username + "k!!!@@@"
    file = open(distraction_name + ".key", "rb")
    key = file.read()  # The key will be type 'bytes'
    file.close()
    # Get key
    f = Fernet(key)

    # Encode username
    encoded_username = user.encode()
    # Encrypt username
    encrypted_username = f.encrypt(encoded_username)

    # Encode password
    encoded_password = password.encode()
    # Encrypt password
    encrypted_password = f.encrypt(encoded_password)

    # Encode email
    encoded_email = email.encode()
    # Encrypt email
    encrypted_email = f.encrypt(encoded_email)

    # Encode info
    encoded_info = info.encode()
    # Encrypt info
    encrypted_info = f.encrypt(encoded_info)

    encrypted_list = (encrypted_username, encrypted_password, encrypted_email, encrypted_info)
    return encrypted_list

# Gets the key from that specific user
def get_key(username):
    # Read key / Get the key from the file
    distraction_name = "@@@!!!llave" + username + "k!!!@@@"
    file = open(distraction_name + ".key", "rb")
    key = file.read()  # The key will be type 'bytes'
    file.close()
    return key

# Decrypts the username
def decrypt(encrypted_username, key):
    # Decrypt the encrypted username
    f = Fernet(key)
    decrypted_username = f.decrypt(encrypted_username)
    # Decode the encoded username
    original_username = decrypted_username.decode()
    return  original_username

# Decrypts the info in the specified tables
def decrypt_tables(tables, key):
    tables_original = []
    for table in tables:
        f = Fernet(key)
        decrypted = f.decrypt(table)
        original = decrypted.decode()
        tables_original.append(original)
    return tables_original
