"""
emails
estimated time: 30 minutes
actual time:  minutes

"""
def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirm_name = input("Is your name {}? (Y/n) ".format(name))
        if confirm_name.upper() != "Y" and confirm_name != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))



def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()