def notN(n):
    while True:
        try:
            n = int(input('Type a integer : '))
            break
        except ValueError:
# if not type(n) is int:
            print('Only integers are allowed. Try again.')
    print('Great :', n)
notN(n)
