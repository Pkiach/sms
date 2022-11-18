
from random import random


def get_lecturer_no(dept_code):
        lecturer_no=f"{dept_code}"# AC regnumber=AC
        two_n0=(ord(dept_code[0])+ord(dept_code[1]))%26
        r_no="".join([str(random.choice([1,2,3,4,5,6,7,8,9,0])) for str in range(5)])
        lecturer_no=f"{lecturer_no}{r_no}"# regnumber= AC17/0756
        return lecturer_no

def get_lecturer_username(First_name):
    return f"{First_name}"

def get_password(First_name):
    return f"{First_name}1234"# password geofrey1234

def get_admin_username(First_name):
    return f"{First_name}"



     
def get_admin_no(dept_code):
        # admin_no=f"{dept_code}"# AC regnumber=AC
        # two_n0=(ord(dept_code[0])+ord(dept_code[1]))%26
        admin_no="".join([str(random.choice([1,2,3,4,5,6,7,8,9,0])) for str in range(6)])
        # lecturer_no=f"{lecturer_no}{r_no}"# regnumber= AC17/0756/
        return admin_no

def get_admin_password(First_name):
    return f"{First_name}1234"# password geofrey1234

