from cryptography.fernet import Fernet

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key)



def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Name", user, "Password", fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account name: ')
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode.")
        continue
