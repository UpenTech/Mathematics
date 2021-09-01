print("""***ax^2 + bx + c = 0***""")

coeff_a = float(input("Enter a (i.e coefficient of x^2): "))
coeff_b = float(input("Enter b (i.e coefficient of x): "))
coeff_c = float(input("Enter c (i.e constant): "))
print("""


      """)

determinant = coeff_b**2 - 4 * coeff_a * coeff_b

if determinant > 1:
    determinant = determinant**(1/2)
    root_1 = (-coeff_b + determinant)/ (2 * coeff_a)
    root_2 = (-coeff_b - determinant)/ (2 * coeff_a)
else:
    if determinant == 0:
        root_1 = root_2 = -coeff_b / (2 * coeff_a)
    else:
        determinant = (-determinant)**(1/2)
        root_1 = str(-coeff_b / (2 * coeff_a)) + " i" + str(determinant / (2 * coeff_a))
        root_2 = str(-coeff_b / (2 * coeff_a)) + " i" + str(determinant / (2 * coeff_a))


print(f"The roots of the equation {coeff_a}x^2 + {coeff_b}x + c are:")
print(f"Root 1: {root_1} and Root 2: {root_2}")

