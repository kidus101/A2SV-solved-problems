import textwrap

def wrap(string, max_width):
    new_string = "" 
    # 0 vs 4 , A  vs 4
    for char in string:
        if len(new_string) == max_width:
            print(new_string)
            new_string = char
        else:
            new_string += char
        
    return (new_string)
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
