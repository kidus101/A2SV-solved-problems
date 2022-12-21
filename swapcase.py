def swap_case(s):
    stringList = list()
    for char in s:
        if char.upper() == char:
            char = char.lower()
            stringList.append(char) 
        else:
            char = char.upper()
            stringList.append(char) 
        
    return "".join(stringList)
            
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
