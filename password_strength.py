import string
import getpass
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--verbose", help="Displays extra information", action="store_true")
parser.add_argument("--hidepass", help="Hides the password while it's typed", action="store_true")
args = parser.parse_args()

low = string.ascii_lowercase
upp = string.ascii_uppercase
dig = string.digits
sym = string.punctuation

low_count = 0
upp_count = 0
dig_count = 0
sym_count = 0

consecutive_low = 0
low_list = [0]
consecutive_upp = 0
upp_list = [0]
consecutive_dig = 0
dig_list = [0]
consecutive_sym = 0
sym_list = [0]
consecutive_list = [consecutive_low, consecutive_upp, consecutive_dig, consecutive_sym]
lists = [low_list, upp_list, dig_list, sym_list]

last_char = 0 #low = 2, upp = 3, dig = 5, sym = 7

if args.hidepass:
    password = getpass.getpass(prompt="Password: ")
else:
    password = str(input("Password: "))

lenght = len(password)

for char in password:
    if char in low:
        if last_char % 2 == 0:
            consecutive_low = consecutive_low+1
        else:
            consecutive_list = [consecutive_low, consecutive_upp, consecutive_dig, consecutive_sym]
            for var in consecutive_list:
                if var != 0:
                    (lists[consecutive_list.index(var)]).append(var)
                    consecutive_list[consecutive_list.index(var)] = 0
            consecutive_low = consecutive_list[0]
            consecutive_upp = consecutive_list[1]
            consecutive_dig = consecutive_list[2]
            consecutive_sym = consecutive_list[3]
            consecutive_low = consecutive_low+1
        last_char = 2
        low_count = low_count+1
    if char in upp:
        if last_char % 3 == 0:
            consecutive_upp = consecutive_upp+1
        else:
            consecutive_list = [consecutive_low, consecutive_upp, consecutive_dig, consecutive_sym]
            for var in consecutive_list:
                if var != 0:
                    (lists[consecutive_list.index(var)]).append(var)
                    consecutive_list[consecutive_list.index(var)] = 0
            consecutive_low = consecutive_list[0]
            consecutive_upp = consecutive_list[1]
            consecutive_dig = consecutive_list[2]
            consecutive_sym = consecutive_list[3]
            consecutive_upp = consecutive_upp+1
        last_char = 3
        upp_count = upp_count+1
    if char in dig:
        if last_char % 5 == 0:
            consecutive_dig = consecutive_dig+1
        else:
            consecutive_list = [consecutive_low, consecutive_upp, consecutive_dig, consecutive_sym]
            for var in consecutive_list:
                if var != 0:
                    (lists[consecutive_list.index(var)]).append(var)
                    consecutive_list[consecutive_list.index(var)] = 0
            consecutive_low = consecutive_list[0]
            consecutive_upp = consecutive_list[1]
            consecutive_dig = consecutive_list[2]
            consecutive_sym = consecutive_list[3]
            consecutive_dig = consecutive_dig+1
        last_char = 5
        dig_count = dig_count+1
    if char in sym:
        if last_char % 7 == 0:
            consecutive_sym = consecutive_sym+1
        else:
            consecutive_list = [consecutive_low, consecutive_upp, consecutive_dig, consecutive_sym]
            for var in consecutive_list:
                if var != 0:
                    (lists[consecutive_list.index(var)]).append(var)
                    consecutive_list[consecutive_list.index(var)] = 0
            consecutive_low = consecutive_list[0]
            consecutive_upp = consecutive_list[1]
            consecutive_dig = consecutive_list[2]
            consecutive_sym = consecutive_list[3]
            consecutive_sym = consecutive_sym+1
        last_char = 7
        sym_count = sym_count+1

consecutive_list = [consecutive_low, consecutive_upp, consecutive_dig, consecutive_sym]
for var in consecutive_list:
    if var != 0:
        (lists[consecutive_list.index(var)]).append(var)
        consecutive_list[consecutive_list.index(var)] = 0

#point system

#ppoint = positive points
#npoint = negative points

low_ppoints = low_count*1
upp_ppoints = upp_count*2
dig_ppoints = dig_count*2
sym_ppoints = sym_count*4

con_low_npoints = max(low_list)*2
con_upp_npoints = max(upp_list)*2
con_dig_npoints = max(dig_list)*2
con_sym_npoints = max(sym_list)*1

lenght_ppoints = lenght*2

ppoints = (low_ppoints+upp_ppoints+dig_ppoints+sym_ppoints+lenght_ppoints)
npoints = (con_low_npoints+con_upp_npoints+con_dig_npoints+con_sym_npoints)
result = ppoints-npoints
print(f"Result: {result}")

if args.verbose:

    print(f"\nLenght: + ({lenght} * 2)")

    print(f"\nLow_count: + ({low_count} * 1)")
    print(f"Upp_count: + ({upp_count} * 2)")
    print(f"Dig_count: + ({dig_count} * 2)")
    print(f"Sym_count: + ({sym_count} * 4)")

    print(f"\nHighest consecutive low: - ({max(low_list)} * 2)")
    print(f"Highest consecutive upp: - ({max(upp_list)} * 2)")
    print(f"Highest consecutive dig: - ({max(dig_list)} * 2)")
    print(f"Highest consecutive sym: - ({max(sym_list)} * 1)")

    # print(f"\nlow_list: {low_list}, higher: {max(low_list)}")
    # print(f"upp_list: {upp_list}, higher: {max(upp_list)}")
    # print(f"dig_list: {dig_list}, higher: {max(dig_list)}")
    # print(f"sym_list: {sym_list}, higher: {max(sym_list)}")
