s = "abbaccde"

st = []
for ch in s:
    if st and st[-1] == ch:
        st.pop()
    else:
        st.append(ch)

