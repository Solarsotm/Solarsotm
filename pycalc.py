while True:
    print('calculator suite menu:')
    print('select your option')
    print('1| addition[+]')
    print('2| subtraction[-]')
    print('3| division[/]')
    print('4| multiplication[*]')

    # Introduccion del usuario

    try:
        user_input = int(input('select your option: '))
        A = int(input('input A: '))
        B = int(input('input B: '))
        #calculadora
        if user_input == 1:
            print('addition = A + B')
            print(A + B)
        elif user_input == 2:
            print('subtraction = A - B')
            print(A - B)
        elif user_input == 3:
            if B == 0:
                print('Error: Division by zero is not allowed.')
            else:
                print('division = A / B')
                print(A / B)
        elif user_input == 4:
            print('multiplication = A * B')
            print(A * B)
        else:
            print('Invalid option selected. Please choose a valid option (1, 2, 3, or 4).')
    except ValueError:
        print('Invalid input. Please enter integer values for the option and numbers A and B.')
