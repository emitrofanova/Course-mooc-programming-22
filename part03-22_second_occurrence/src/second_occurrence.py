# Write your solution here
st = input("Please type in a string: ")
subst = input("Please type in a substring: ")
if subst in st:
    index = st.find(subst)
    st = st[index + len(subst):]
    if subst in st:
        index2 = st.find(subst)
        print(f"The second occurrence of the substring is at index {index + index2 + len(subst)}.")
    else:
        print("The substring does not occur twice in the string.")
else:
        print("The substring does not occur twice in the string.")

