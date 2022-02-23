def allocateParkingSlot():
    if parking == 1:
        if vehicleType != 1:
            print("Sorry this row is only available for bike. Please choose Two wheeler parking number.")
        elif slot > 10:
            print("Please choose slot lesser then 10")
        elif two_Wheeler_Parking_area[slot - 1] == 0:
            two_Wheeler_Parking_area[slot - 1] = vehicleType
        else:
            print("Slot Not Available")
    elif parking == 2:
        if vehicleType != 2:
            print("Sorry this row is only available for Car. Please choose Four wheeler parking number.")
        elif slot > 10:
            print("Please choose slot lesser then 10")
        elif four_Wheeler_Parking_area[slot - 1] == 0:
            four_Wheeler_Parking_area[slot - 1] = vehicleType
        else:
            print("Slot Not Available")
    else:
        print("Row Not Available")

# Declared Parking lots lists with unique name
two_Wheeler_Parking_area = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
four_Wheeler_Parking_area = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
    #Get vehicle type from user
    vehicleType = int(input("\n1.Two wheeler \n2. Four Wheeler\nEnter vehicle Type Number: "))

    #Get Parking area from user
    parking = int(input("\n1.Two Wheeler parking area \n2.Four wheeler parking area\nEnter the Parking type Number: "))

    #Get slot number from user
    slot = int(input("Enter the slot number: "))

    #Called function to allocate parking lot
    allocateParkingSlot()

    print("-------------------------------------------------------------")
    print(".....................AVAILABLE SLOT..........................")
    print("-------------------------------------------------------------")
    print(two_Wheeler_Parking_area)
    print(four_Wheeler_Parking_area)