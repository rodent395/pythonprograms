global x
x = 1
def main():
    global x
    choice = int(raw_input('Welcome!\n1. Random Question:   '))
    if choice == 1:
        Question()
    else:
            print 'thats not a question bro'
def Question():
    x = int(raw_input('What was the year the astronauts "landed" on the moon?:   '))
    if x == 1969:
        print 'Correct!'
while x == 1:
    main()
