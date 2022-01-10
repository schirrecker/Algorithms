def weekday(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        #wildcard case
         case _:
            return "Please Enter a Valid Day Number"
print(weekday(1))   #Sunday
print(weekday(4))   #Wednesday
print(weekday(7))   #Saturday
print(weekday(11))  #Please Enter a Valid Day Number
