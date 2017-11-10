def new_password(oldpassword, newpassword):
    for c in newpassword:
        if c in '0123456789':
            if len(newpassword) >= 6 and oldpassword != newpassword:
                return True
            else:
                return False
        else:
            return False


newpassword = input("Voer het nieuwe wachtwoord in: ")
print(new_password("vakProg17", newpassword))
