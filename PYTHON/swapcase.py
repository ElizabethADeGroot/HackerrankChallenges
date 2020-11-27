sWAP cASE

def swap_case(s):
    string = 'HackerRank.com presents "Pythonist 2".'
    updateString = ''
    for s in string:  
        if s.isupper() == True:
            updateString +=(s.lower())
        else:
            updateString +=(s.upper())
    return updateString
print(input().swapcase())
