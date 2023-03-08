import re

class User:
    def __init__(self,userID,username,password,email):

        # (?=...) is a positive lookahead which means the pattern must be in the following characters
        # (?=.*[A-Z]) means upper case character must be ahead
        # (?=.*[a-z]) means a lower case character must be ahead
        # (?=.*/d)    means a digit (0-9) must be ahead
        # (?=.*[@#$]) a special character must be ahead
        # {6,12} between 6 and twelve characters in length

        assert type(userID)==int and userID>=0,"userID has to be a positive integer"
        assert len(username)>0 and len(username<16),"username has to be between 1 and 15 character is length"
        assert re.fullmatch(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$])[A-Za-z0-9@#$]{6,200}$", password),"password does not meet the specified requirements"
        assert re.fullmatch(r"^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$",email),"invalid email provided"

        self.userID=userID
        self.username=username
        self.password=password
        self.email=email

user = User(1,"Brent","bve12310987","P@ssw0rd","brentve12310987@gmail.com")

user.userID=2