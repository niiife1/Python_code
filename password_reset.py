password = input()

ideal_word = []
while True:
    command = input().split(" ")
    command1 = command[0]
    if command1 != "Done":
        if command1 == "TakeOdd":
            password = (password[1::2])
            print(password)
            continue

        elif command1 == "Cut":
            command2 = int(command[1])
            command3 = int(command[2])
            if len(password) > command2:
                password = password[0: command2] + password[command3 + command2::]
                print(password)
                continue

        elif command1 =="Substitute":
            command2 = command[1]
            command3 = command[2]
            if command2 in password:
                password = password.replace(command2, command3)
                print(password)

            else:
                print("Nothing to replace!")
            continue
    print(f"Your password is: {password}")
    break