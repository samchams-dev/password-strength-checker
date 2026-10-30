import string
from getpass import getpass

def validate_passwd(passwd):
    weaknesses = []
    
    if len(passwd) < 8:
        weaknesses.append("Password must contain at least 8 characters")
    if not any(char.isupper() for char in passwd):
        weaknesses.append("Password must contain at least one uppercase letter")
    if not any(char.islower() for char in passwd):
        weaknesses.append("Password must contain at least one lowercase letter")
    if not any(char.isdigit() for char in passwd):
        weaknesses.append("Password must contain at least one digit")
    if not any(char in string.punctuation for char in passwd):
        weaknesses.append("Password must contain at least one special character")
    return weaknesses


def match_passwd(passwd, confirm_passwd):
    return confirm_passwd == passwd


def check_passwd(passwd):
    score = 0

    if len(passwd) >= 12:
        score += 1
    if len(passwd) >= 16:
        score += 1

    num_count = sum(1 for char in passwd if char.isdigit())
    sym_count = sum(1 for char in passwd if char in string.punctuation)
    
    if num_count > 1:
        score += num_count
    if sym_count > 1:
        score += sym_count

    return score

def main():
    while True:
        passwd = getpass("Enter your password: ")
        weaknesses = validate_passwd(passwd)
    
        if weaknesses:
            for w in weaknesses:
                print(w)
            continue

        confirm_passwd = getpass("Re-type your password: ")

        if not match_passwd(passwd, confirm_passwd):
            print("Passwords do not match.")
            continue

        break

    print("Password accepted.")


    passwd_score = check_passwd(passwd)


    if passwd_score == 0:
        print("WEAK PASSWORD")
    elif passwd_score < 3:
        print("MODERATE PASSWORD STRENGTH")
    else:
        print("STRONG PASSWORD")

if __name__ == "__main__":
    main()
    


