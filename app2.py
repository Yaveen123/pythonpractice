userToCheck = "NESA2423ka1"

def checkuser(userToCheck):
    if not len(userToCheck) >= 8:
        return False

    if not userToCheck[0].isupper():
        return False

    if not userToCheck[len(userToCheck)-2].islower():
        return False

    if not userToCheck[len(userToCheck)-1].isdigit():
        return False

    return True


print(checkuser(userToCheck))


