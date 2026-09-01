import unit_converter


def show_menu():
    print("--- ENGINEERING UNIT CONVERTER---")
    print("1. Millimetres to Inches")
    print("2. Inches to Millimetres")
    print("3. Centimetres to Inches")
    print("4. Inches to Centimetres")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    if choice == "1":
        val = float(input("Enter mm: "))
        print(f"Result: {unit_converter.mm_to_inches(val)} inches")
    elif choice == "2":
        val = float(input("Enter inches: "))
        print(f"Result: {unit_converter.inches_to_mm(val)} mm")
    elif choice == "3":
        val = float(input("Enter cm: "))
        print(f"Result: {unit_converter.cm_to_inches(val)} inches")
    elif choice == "4":
        val = float(input("Enter inches: "))
        print(f"Result: {unit_converter.inches_to_cm(val)} cm")
    elif choice == "5":
        print("Goodbye!")
        return
    else:
        print("Invalid option!")

show_menu()