#UID for 100 employees
#validate the IDS
import re

n=int(input())
for UID in range(n):
    UID=input()
    prog = re.compile(r"""
    ^
    (?=.*[A-Z]{2,})     # At least 2 uppercase English alphabet characters
    (?=.*\d{3,})        # At least 3 digits
    (?=.*[a-zA-Z\d])    # Only alphanumeric characters
    (?!.*(.).*\1+.*)       # No repeated character
    .{10}
    $
    """, re.VERBOSE)
    
    

    
    state= bool(re.match(prog,UID))
    if state is True:
        print("Valid")
    if state is False:
        print("Invalid")

