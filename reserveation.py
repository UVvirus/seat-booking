# class reservation:
seat_list = []
seat_list.append([0, 0, 0, 0, 0])
seat_list.append([1, 0, 0, 0, 1])
seat_list.append([0, 1, 0, 1, 0])
seat_list.append([0, 0, 1, 1, 0])
seat_list.append([0, 1, 0, 1, 0])

print("0- seat is empty")
print("1- seat if filled")


def booked_seats(seat_list):
    for row in seat_list:
        print(row)
    print("")


def check_bookings():
    row = int(input("Enter a row number [0-4]:"))
    column = int(input("Enter a column number[0-4]:"))
    if seat_list[row][column] == 0:
        print("seat is empty")
    else:
        print("seat is booked")

def seat_book():
    booked=False
    while booked==False:
      row=int(input("Enter a row number of seat:"))
      column=int(input("Enter column number of seat:"))
      if seat_list[row][column]==0:
          print("seat is empty\n")
          print("seat is booking...")
          seat_list[row][column]=1
          print("seat is booked for you")
          booked=True
          print(seat_list[row][column])
      else:
          print("Already booked")



check_bookings()
booked_seats(seat_list)
seat_book()
