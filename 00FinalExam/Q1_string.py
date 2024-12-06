# Defining a function that return string depending on the condition

def return_string(str1):
    if len(str1) < 2:
        return ""
    new_str = str1[len(str1)-2:]
    return new_str


ans = return_string("Delhi")

print(ans)