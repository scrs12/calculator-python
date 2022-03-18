# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Pilih operasi.")
print("1.Tambah")
print("2.Kurangi")
print("3.Kalikan")
print("4.Bagi")

while True:
    # take input from the user
    choice = input("Masukan pilihan(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Angka pertama: "))
        num2 = float(input("Angka kedua: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Lagisme atau kaga? (iya/kaga): ")
        if next_calculation == "kaga":
          break
    
    else:
        print("salah input qom")