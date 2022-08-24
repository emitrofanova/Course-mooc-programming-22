# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    ident_str = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    if len(pic) > 11:
        return False
    if not(pic[0:6].isnumeric() and pic[7:10].isnumeric() and (pic[6] == "+" or pic[6] == "-" or pic[6] == "A") and (pic[10] in ident_str)):
        return False
    if pic[6] == "+":
        year = int("18" + pic[4:6])
    elif pic[6] == "-":
        year = int("19" + pic[4:6])
    elif pic[6] == "A":
        year = int("20" + pic[4:6])
    else:
        return False
    month = int(pic[2:4])
    day = int(pic[0:2])
    try:
        birth = datetime(year, month, day)
    except:
        return False
    pers_id = int(pic[0:6] + pic[7:10]) % 31
    if ident_str[pers_id] != pic[10]:
        return False
    return True

if __name__ == "__main__":
    print(is_it_valid("310823A9877"))
