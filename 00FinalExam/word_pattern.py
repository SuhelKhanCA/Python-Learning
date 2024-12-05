# Given a pattern and a string s, find if s follows the same pattern.

def word_pattern(pattern, sentence):
    words = sentence.split()
    st = set()
    d = {}
    if len(pattern) != len(words):
        return False
    for i, char in enumerate(pattern):
        if char not in d:
            if words[i] in st:
                return False
            d[char] = words[i]
            st.add(words[i])
        else:
            if d[char] != words[i]:
                return False       
    return True        

ans = word_pattern("abba", "dog cat cat dog")    
print(ans)