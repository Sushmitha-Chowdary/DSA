def isValid(s):
    st=[]
    for ch in s:
        if ch in '({[':
            st.append(ch)
        else:
            if not st:
                return False
            top=st.pop()
            if ch==')' and top!='(':
                return False
            if ch==']' and top!='[':
                return False
            if ch=='}' and top!='{':
                return False
    return not st
s=input()
print(isValid(s))