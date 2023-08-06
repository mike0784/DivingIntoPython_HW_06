import validationDate as vd
from sys import argv
date = "10.10.1960"
if __name__ == '__main__':
    print(vd.date_check(date))
    print(vd.date_check(argv[1]))
