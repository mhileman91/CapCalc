#! python 3
# Hi! Thanks for viewing my code. Please feel free to recommend changes
# I am open to constructive criticism

instructions = '''
Voltage is obtained by reading voltage between common terminal \n
and terminal to be tested. (Run or Herm for dual, Run for single)\n
Amperage is obtained by ammeter across wire.\n
Capacitor must be under load to test.\n
'''
print(instructions)
isRunning = True
while isRunning == True:
    x = input("Input Voltage\n")
    y = input("Input Amperage\n")
    z = float(float(y) * 2652 / float(x))
    a = "{:.2f}".format(z)
    print(f"Your capacitor is reading {a}.")
    answer = input("Run again? Y/N \n")
    if answer.lower() == "y":
        continue
    elif answer.lower() == "n":
        print("Thank you for using CapCalc")
        isRunning = False
        break
        
