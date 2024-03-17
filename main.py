from random import randint, choice
from sys import argv

def usage():
    print("Usage:")
    print("main.py [-cd/-oem] [amount]")
    print("Default key amount is 1.")

def cd():
    # XXX-YYYYYYY
    
    # Generate random number in range 0-999.
    # zfill makes sure the number has 3 digits.
    XXX = str(randint(0, 999)).zfill(3)
    # randint output converted to string for zfill.
    
    # If XXX is invalid, generate again
    while XXX in [333, 444, 555, 666, 777, 888, 999]:
        XXX = str(randint(0, 999)).zfill(3)

    # Random 7 digit number
    YYYYYYY = str(randint(0, 9999999)).zfill(7)
    # Sum all digits
    YYYYYYY_sum = sum(int(i) for i in str(YYYYYYY))

    # Generate new YYYYYYY values when last digit is 8 or 9
    # or when sum is not divisible by 7.
    while int(YYYYYYY[-1]) >= 8 or not YYYYYYY_sum % 7 == 0:
        YYYYYYY = str(randint(0, 9999999)).zfill(7)
        YYYYYYY_sum = sum(int(i) for i in str(YYYYYYY))

    #print(f"Last digit of Y: {int(YYYYYYY[-1])}")
    #print(f"YYYYYYY_sum % 7 == {YYYYYYY_sum%7}")

    return f"{XXX}-{YYYYYYY}"

def oem():
    # XXXXX-OEM-YYYYYYY-ZZZZZ
    
    # XXXXX defines date and year of key production.
    # [Day of year][Year]
    
    # Day of year could be anything from 001-366
    XXXXX_day = str(randint(1, 366)).zfill(3)

    # Year could be anything from 95-03
    # However Windows 95 only supports years up to 2002.
    # For compatibility, keys from 1995-2002 will be generated.
    XXXXX_year = choice(['95', '96', '97', '98', '99', '00', '01', '02'])

    # Combine day and year
    XXXXX = XXXXX_day + XXXXX_year

    # YYYYYYY has the exact same rule as in CD keys, except
    # the first digit cannot be 0.
    YYYYYYY_nd = str(randint(0, 999999)).zfill(6)
    # Script will add the first digit after confirmation that
    # sum of other digits is divisible by 7.

    YYYYYYY_nd_sum = sum(int(i) for i in str(YYYYYYY_nd))

    # Loop until sum divisible by 7
    while not YYYYYYY_nd_sum % 7 == 0:
        YYYYYYY_nd = str(randint(0, 999999)).zfill(6)
        YYYYYYY_nd_sum = sum(int(i) for i in str(YYYYYYY_nd))

    # Add first digit
    YYYYYYY = '0' + YYYYYYY_nd

    # ZZZZZ does not matter.
    ZZZZZ = str(randint(0, 99999)).zfill(5)

    return f"{XXXXX}-OEM-{YYYYYYY}-{ZZZZZ}"

def gen(amount, keytype):
    for i in range(amount):
        if keytype == 'oem':
            print(oem())
        elif keytype == 'cd':
            print(cd())
        else:
            print("O_o")
            break

if len(argv)>1:
    match argv[1]:
        case '-cd':
            try:
                if len(argv)>2:
                    gen(int(argv[2]), 'cd')
                else:
                    gen(1, 'cd')
            except Exception as e:
                print(str(e) + '\n')
                usage()
                
        case '-oem':
            try:
                if len(argv)>2:
                    gen(int(argv[2]), 'oem')
                else:
                    gen(1, 'oem')
            except Exception as e:
                print(str(e) + '\n')
                usage()
                
        case _:
            usage()
else:
    usage()
