a = "A"
b = "B"
c = 1.1

string = 'a={var1} b={var2} c={var3:.2f}'
formato = string.format(
    var1 = a, var2= b, var3 = c
)

print(formato)