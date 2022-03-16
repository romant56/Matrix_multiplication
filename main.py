Am = int(input("Enter the number of rows of matrix A: "))
An = int(input("Enter the number of columns of matrix A:"))
Bm = int(input("\nEnter the number of rows of matrix B:"))
Bn = int(input("Enter the number of columns of matrix B:"))


if An != Bm:
    print("\nSince matrix A has " + str(An) + " column(s) and matrix B has " + str(Bm) + " row(s), the two matrices cannot be multiplied.")
print()
d = {}
for row in range(1, Am + 1):
    rowtemp = (input("Enter the numbers in matrix A row " + str(row) + ", with each value separate by a space:").split())
    d["A{0}".format(row)] = rowtemp
print()
for row in range(1, Bm + 1):
    rowtemp = (input("Enter the numbers in matrix B row " + str(row) + ", with each value separate by a space:").split())
    d["B{0}".format(row)] = rowtemp


d["C{0}".format(row)] = []
sum = 0
for row in range(1, Am + 1):
    for column in range(len(d["B1"])):
        for i in range(1, An + 1):
            sum += float(d["A{0}".format(row)][i - 1]) * float(d["B{0}".format(i)][column])
        try:
            d["C{0}".format(row)].append(sum)
        except:
            d["C{0}".format(row)] = [sum]
        sum = 0

print("\nThe product is:")
for row in range(1, Am + 1):
    print(d["C{0}".format(row)])
