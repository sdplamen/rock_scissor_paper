def calendar(yy, mm):
    import calendar, datetime
    print(calendar.month(yy, mm))
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
calendar(yy, mm)
