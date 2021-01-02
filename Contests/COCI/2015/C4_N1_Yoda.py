n = input()
m = input()
if len(n) > len(m):
    m = "0" * (len(n) - len(m)) + m
elif len(n) < len(m):
    n = "0" * (len(m) - len(n)) + n

n_output = "0"
m_output = "0"
for i in range(len(n)):
    if int(n[i]) < int(m[i]):
        m_output += m[i]
    elif int(n[i]) > int(m[i]):
        n_output += n[i]
    else:
        n_output += n[i]
        m_output += n[i]

if n_output == "0":
    print("YODA")
else:
    print(int(n_output))
if m_output == "0":
    print("YODA")
else:
    print(int(m_output))
