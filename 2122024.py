
T= int(input())
for i in range(T):
    s=input()

    even_characters = [] # For storing even characters
    odd_characters = [] # For storing odd characters

    for i in range(len(s)):
        if i % 2 == 0: # check if the index is even
            even_characters.append(s[i])
        else:
            odd_characters.append(s[i])
    even_characters=''.join(even_characters)
    odd_characters=''.join(odd_characters)
    res=(even_characters,odd_characters)
    print(' '.join(res))