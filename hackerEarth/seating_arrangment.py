def get_seat_num_and_seat_type(num):
    facing_seat_number = 0
    seat_type = ''
    if (num % 12 == 0 or num % 12 == 1 or num % 12 == 4 or num % 12 == 9):
        if num % 12 == 0:
            facing_seat_number = num - 11
            seat_type = 'WS'
        elif num % 12 == 1:
            facing_seat_number = num + 11
            seat_type = 'WS'
        elif num % 12 == 4:
            facing_seat_number = num + 5
            seat_type = 'AS'
        else:
            facing_seat_number = num - 5
            seat_type = 'AS'
        return str(facing_seat_number) + ' ' + seat_type
    elif (num % 12 == 11 or num % 12 == 2 or num % 12 == 8 or num % 12 == 5):
        if num % 12 == 11:
            facing_seat_number = num - 9
        elif num % 12 == 2:
            facing_seat_number = num + 9
        elif num % 12 == 8:
            facing_seat_number = num - 3
        else:
            facing_seat_number = num + 3
        return str(facing_seat_number) + ' MS'
    elif (num % 12 == 10 or num % 12 == 3 or num % 12 == 7 or num % 12 == 6):
        if num % 12 == 10:
            facing_seat_number = num - 7
            seat_type = 'AS'
        elif num % 12 == 3:
            facing_seat_number = num + 7
            seat_type = 'AS'
        elif num % 12 == 7:
            facing_seat_number = num - 1
            seat_type = 'WS'
        else:
            facing_seat_number = num + 1
            seat_type = 'WS'
        return str(facing_seat_number) + ' ' + seat_type
    else:
        return 0
test_cases = input()
for test_case in range(test_cases):
    seat_number = input()
    seat_num_and_seat_type = get_seat_num_and_seat_type(seat_number)
    print seat_num_and_seat_type