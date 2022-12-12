import sys, time

print('Zigzag')
print('Press Ctrl-C to quit.')
time.sleep(1)

indentSize = 0  # How many spaces to indent.

try:
    while True:  # The main program loop.
        # Zig to the right 20 times:
        for i in range(5):
            indentSize = indentSize + 1
            indentation = ' ' * indentSize
            print(' ' * indentSize + '********')
            time.sleep(0.1)  # Pause for 50 milliseconds.

        # Zag to the left 20 times:
        for i in range(5):
            indentSize = indentSize - 1
            indentation = ' ' * indentSize
            print(indentation + '********')
            time.sleep(0.1)  # Pause for 50 milliseconds.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
