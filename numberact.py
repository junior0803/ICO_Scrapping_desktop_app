import re
import string


def listToString(s): 
    # return string  
    return ' '.join([str(elem) for elem in s])

def getNumber(str):
    s = str.replace(",", "")
    print(s)
    # if("million" in s or "Million" in s):
    #     Indices = 1000000
    # elif ("trillion" in s or "Trillion" in s):
    #     Indices = 1000000000
    # else:
    #     Indices = 1
    
    p = re.compile(r'-?\d+\.\d+')  # Compile a pattern to capture float values
    floats = p.findall(s)  # Convert strings to int
    if(len(floats) > 0):
        print(floats)
        ret = floats
    else:
        p = re.compile(r'-?\d+')  # Compile a pattern to capture int values
        ints = p.findall(s)
        ret = ints
    
    return listToString(ret)
