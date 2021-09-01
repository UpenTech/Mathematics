
print("""***ax^2 + bx + c = 0***""")

coeff_a = float(input("Enter a (i.e coefficient of x^2): "))
coeff_b = float(input("Enter b (i.e coefficient of x): "))
coeff_c = float(input("Enter c (i.e constant): "))
print("""
      """)

def print_Root(root_1,root_2,coeff_a,coeff_b,coeff_c):

    if coeff_b >= 0 and coeff_c >= 0:
        print("The roots of the equation;\n"
        f"{coeff_a} x^2 + {coeff_b} x + {coeff_c} = 0 is:\n\n ")
    elif coeff_b >= 0 and coeff_c < 0:
        print("The roots of the equation;\n"
        f"{coeff_a} x^2 + {coeff_b} x - {coeff_c} = 0 is:\n\n ")
    elif coeff_b < 0 and coeff_c < 0:
        coeff_b = -coeff_b
        print("The roots of the equation;\n"
        f"{coeff_a} x^2 - {coeff_b} x - {coeff_c} = 0 is:\n\n ")
    else:
        coeff_b = -coeff_b
        print("The roots of the equation;\n"
        f"{coeff_a} x^2 - {coeff_b} x + {coeff_c} = 0 is:\n\n ")

    print(f"Root 1: {root_1}\nRoot 2: {root_2}")


def print_Imaginary(real_Part,imaginary_Part,coeff_a,coeff_b,coeff_c):

    if coeff_b >= 0 and coeff_c >= 0:
        print("The roots of the equation;\n"
        f"{coeff_a} x^2 + {coeff_b} x + {coeff_c} = 0 is:\n\n ")
    elif coeff_b >= 0 and coeff_c < 0:
        print("The roots of the equation;\n"
        f"{coeff_a} x^2 + {coeff_b} x - {coeff_c} = 0 is:\n\n ")
    elif coeff_b < 0 and coeff_c < 0:
        coeff_b = -coeff_b
        print("The roots of the equation;\n"
        f"{coeff_a} x^2 - {coeff_b} x - {coeff_c} = 0 is:\n\n ")
    else:
        coeff_b = -coeff_b
        print("The roots of the equation;\n"
        f"{coeff_a} x^2 - {coeff_b} x + {coeff_c} = 0 is:\n\n ")


    print(f"Root 1: {real_Part} + i {imaginary_Part}\n")
    print(f"Root 2: {real_Part} - i {imaginary_Part}\n")


determinant = coeff_b**2 - 4 * coeff_a * coeff_c
determinant = round(determinant,3)


if determinant > 1:
    determinant = determinant**(1/2)
    root_1 = (-coeff_b + determinant)/ (2 * coeff_a)
    root_1 = round(root_1,3)
    root_2 = (-coeff_b - determinant)/ (2 * coeff_a)
    root_2 = round(root_2,3)
    print_Root(root_1,root_2,coeff_a,coeff_b,coeff_c)

else:

    if determinant == 0.00:
        root_1 = root_2 = -coeff_b / (2 * coeff_a)
        root_1 = round(root_1,3)
        print_Root(root_1,root_2,coeff_a,coeff_b,coeff_c)

    else:
        determinant = (-determinant)**(1/2)
        real_Part = (-coeff_b) / (2 * coeff_a)
        imaginary_Part = determinant / (2 * coeff_a)
        real_Part = round(real_Part,3)
        imaginary_Part = round(imaginary_Part,3)
        print_Imaginary(real_Part,imaginary_Part,coeff_a,coeff_b,coeff_c)






