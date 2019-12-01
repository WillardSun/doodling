started = False
game_on = True
while game_on == True
    command = input(">")
    if command == ("help"):
        print('''
Commands:
start -> to start the car
stop -> to stop the car
quit -> to exit
            ''')
    elif command == ("start"):
        if started:
            print("Car already started!")
            started = True
        elif not started:
            print("Car starting...")
            started = True
    elif command == ("stop"):
        if started:
            print("Car stopping...")
            started = False
        elif not started:
            print("Car already stopped!")
            started = False
    elif command == ("quit"):
        game_on = False
        break
    else:
        print ("Sorry, that is not a command. Please refer to the 'help' command for further details.")







