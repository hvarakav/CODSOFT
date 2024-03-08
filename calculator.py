def perform_operation(number1, number2, operation_symbol):
  """
  Executes a basic arithmetic operation based on the symbol.

  Args:
      number1: The first operand (float).
      number2: The second operand (float).
      operation_symbol: The symbol representing the operation (str, one of "+", "-", "*", "/").

  Returns:
      The result of the calculation (float) or None if an error occurs.
  """
  operations = {
      "+": lambda a, b: a + b,
      "-": lambda a, b: a - b,
      "*": lambda a, b: a * b,
      "/": lambda a, b: b and a / b  # Short-circuiting for division by zero
  }
  if operation_symbol in operations:
    return operations[operation_symbol](number1, number2)
  else:
    print("Invalid operation symbol provided.")
    return None

while True:
  # Get valid user input
  while True:
    try:
      number1 = float(input("Enter the first number: "))
      number2 = float(input("Enter the second number: "))
      operation_symbol = input("Choose an operation (+, -, *, /): ")
      break
    except ValueError:
      print("Invalid input. Please enter numbers only.")

  # Perform calculation and display result
  result = perform_operation(number1, number2, operation_symbol)
  if result is not None:
    print(f"{number1} {operation_symbol} {number2} = {result}")

  # Ask user if they want to continue
  choice = input("Do you want to perform another calculation? (y/n): ")
  if choice.lower() != "y":
    break

print("Calculator closed.")