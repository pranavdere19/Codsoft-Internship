# Simple Calculator in Python

# Step 1: Take user input for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Step 2: Show operation choices
print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Step 3: Take user's choice
choice = input("Enter choice (1/2/3/4): ")

# Step 4: Perform calculation
if choice == '1':
    result = num1 + num2
    print(f"\n✅ Result: {num1} + {num2} = {result}")

elif choice == '2':
    result = num1 - num2
    print(f"\n✅ Result: {num1} - {num2} = {result}")

elif choice == '3':
    result = num1 * num2
    print(f"\n✅ Result: {num1} * {num2} = {result}")

elif choice == '4':
    if num2 != 0:  # Prevent division by zero
        result = num1 / num2
        print(f"\n✅ Result: {num1} / {num2} = {result}")
    else:
        print("\n❌ Error: Division by zero is not allowed!")

else:
    print("\n❌ Invalid choice! Please select 1, 2, 3, or 4.")