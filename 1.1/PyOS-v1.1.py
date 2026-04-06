# Loading / Загрузка
print("Loading...")
name = input("Username: ")
print("Welcome to the PyOS,", name)

# Commands / Команды
while True:
    command = input(">> ")

    if command == "info":
        print("Version: PyOS v1.1")
        print("Developer: BlankCode")

    elif command == "help":
        print("Commands: info, help, helloworld, nothing, exit")

    elif command == "helloworld":
        print("Hello World!")

    elif command == "nothing":
        print("Nothing...")

    elif command == "exit":
        break