L = input("Enter loan amount: ")
i = 0.05
n = input("number of payments: ")

L = float(L)
i = float(i)
n = float(n)

M = L*(i*(1+i)*n) / ((1+i)*(n-1))

print("Therefore, your monthly payment for mortgage is {0:f}" .format(M))
