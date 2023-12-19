def main():
    expression = input("Expression: ")
    x, y, z = expression.split()
    x, y, z = int(x), y, int(z)

    match y:
        case "+":
            print(f"{float(x + z):.1f}")
        case "-":
            print(f"{float(x - z):.1f}")
        case "/":
            print(f"{float(x / z):.1f}"if z != 0 else "Error: Cannot divide by zero.")
        case "*":
            print(f"{float(x * z):.1f}")

main()
