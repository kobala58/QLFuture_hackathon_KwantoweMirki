N = 3
M = 5


def square(i, j):
    first_sum = "+"
    second_sum = "+"
    tmp = first_sum.join([f"x{i}{l}*w{l}" for l in range(M)])
    tmp2 = second_sum.join([f"x{j}{l_2}*w{l_2}" for l_2 in range(M)])
    return f"({tmp})-({tmp2})"


final = "+"
newstr = ""
for i in range(N):
    for j in range(i + 1, N):
        tmp = square(i, j)
        newstr = f"{tmp}*{tmp}"
        print(newstr)
        print("\n-----------\n")


