print("SWAP TWO NUMBERS USING BIT MANIPULATION")

a=int(input("Enter A Number: "))
b=int(input("Enter B Number: "))

a=a^b
b=a^b
a=a^b

print(f"A is: {a}\nB is: {b}" )


# Output:

# ----------------------------------------
# Enter A Number: 52
# Enter B Number: 64
# A is: 64
# B is: 52
# -----------------------------------------