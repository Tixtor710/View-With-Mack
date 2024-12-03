def print_formatted(number):
    # your code goes here
    width=len(bin(n)[2:])
    # your code goes here\
    for i in range(1,n+1):
        print(f"{(i):>{width}}",f"{oct(i)[2:]:>{width}}",f"{hex(i)[2:].upper():>{width}}",f"{bin(i)[2:]:>{width}}")
        
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)