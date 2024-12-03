s = input()
    
if __name__ == '__main__':
    s=input()
    m=len(s)
    
    if any(i.isalnum() for i in s):
        print("True")

    if any(i.isalpha() for i in s):
        print("True")
                
    if any(i.isdigit() for i in s):
        print("True")
                
    if any(i.islower() for i in s):
        print("True")
    if any(i.isupper() for i in s):
        print("True")
            
    else:
        print("False")