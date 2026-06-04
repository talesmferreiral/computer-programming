# Inventory Management System - DataCode Solutions
# Simulates a basic product inventory with an interactive menu.
# Supports viewing, adding, and removing products using a while loop.

# Dictionary of Dictionaries: chosen because it allows direct access
# to any product by name (key), making lookups and updates more efficient.
estoque = {
    "arroz":    {"quantidade": 50, "preco": 5.99},
    "feijao":   {"quantidade": 30, "preco": 8.49},
    "macarrao": {"quantidade": 40, "preco": 3.75},
    "azeite":   {"quantidade": 15, "preco": 22.90},
    "sal":      {"quantidade": 60, "preco": 2.10},
}


def exibir_estoque():
    """Displays all products with their quantity and price."""
    print("\n===== CURRENT INVENTORY =====")
    print(f"{'Product':<12} {'Quantity':>10} {'Price':>10}")
    print("-" * 35)
    for produto, dados in estoque.items():
        print(f"{produto:<12} {dados['quantidade']:>10} R$ {dados['preco']:>7.2f}")
    print("=" * 35)


def entrada_produto():
    """Handles product restocking. Allows registering new products."""
    print("\n===== PRODUCT ENTRY =====")
    nome = input("Product name: ").lower()

    if nome not in estoque:
        print(f"Product '{nome}' not found in inventory.")
        adicionar = input("Would you like to register it? (y/n): ").lower()
        if adicionar == "y":
            preco = float(input("Enter the unit price: R$ "))
            estoque[nome] = {"quantidade": 0, "preco": preco}
            print(f"Product '{nome}' registered successfully!")
        else:
            print("Operation cancelled.")
            return

    quantidade = int(input(f"How many units of '{nome}' to add? "))
    estoque[nome]["quantidade"] += quantidade
    print(f"Inventory updated! '{nome}' now has {estoque[nome]['quantidade']} units.")


def saida_produto():
    """Handles product withdrawal. Validates stock availability."""
    print("\n===== PRODUCT EXIT =====")
    nome = input("Product name: ").lower()

    if nome not in estoque:
        print(f"Product '{nome}' not found in inventory.")
        return

    quantidade = int(input(f"How many units of '{nome}' to remove? "))

    if quantidade > estoque[nome]["quantidade"]:
        print(f"Insufficient stock! Available: {estoque[nome]['quantidade']} units.")
    else:
        estoque[nome]["quantidade"] -= quantidade
        print(f"Exit recorded! '{nome}' now has {estoque[nome]['quantidade']} units.")


# Main loop — keeps the menu running until the user chooses to exit
print("Welcome to the Inventory Management System - DataCode Solutions")

while True:
    print("\n===== MAIN MENU =====")
    print("1 - View inventory")
    print("2 - Product entry")
    print("3 - Product exit")
    print("4 - Exit program")
    print("=====================")

    opcao = input("Choose an option: ")

    if opcao == "1":
        exibir_estoque()
    elif opcao == "2":
        entrada_produto()
    elif opcao == "3":
        saida_produto()
    elif opcao == "4":
        print("\nSystem closed. Goodbye!")
        break
    else:
        print("Invalid option! Please enter a number between 1 and 4.")
