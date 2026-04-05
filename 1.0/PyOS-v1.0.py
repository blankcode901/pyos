# Loading / Загрузка
print("Loading...")
name = input("Username: ")
print("Welcome to the PyOS,", name)

# Commands / Команды
while True:
    command = input(">> ")

    if command == "info":
        print("Version: PyOS v1.0")

    elif command == "help":
        print("Commands: info, help, exit")

    elif command == "exit":
        break