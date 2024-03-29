SpecialSym = "&#~-/_@*-+<>%.!?,\;" # attention \
EndEmail = [".com", ".fr", ".pix", ".gouv"]

def contain_specialsymt(string  : str) -> bool:
    return any(char in SpecialSym for char in string)

def contains_number(string : str) -> bool:
    return any(char.isdigit() for char in string)

def contains_upper(string : str) -> bool:
    return any(char.isupper() for char in string)

def contains_lower(string : str) -> bool:
    return any(char.islower() for char in string)

def contains_endemail(email : str) -> bool:
    return any(endmail in email[len(email)-5:] for endmail in EndEmail)

def check_password(password : str) -> bool:
    try:
        assert len(password) >= 8, "The password must be longer than 8 characters."
        assert contains_number(password), "The password must contain at least one number."
        assert contains_upper(password), "The password must contain at least one capital letter."
        assert contain_specialsymt(password), "The password must contain at least one special character."
        return True
    except AssertionError as error:
        return error

def check_username(username : str) -> bool | str:
    try:
        assert len(username) >= 5, "The username must be longer than 5 characters."
        return True
    except AssertionError as error:
        return error
    
def check_email(email : str) -> bool | str:
    try:
        assert len(email) >= 6, "The email is to short."
        assert "@" in email, "The email is invalide."
        assert contains_endemail(email), "The email is invalide."
        return True
    except AssertionError as error:
        return error