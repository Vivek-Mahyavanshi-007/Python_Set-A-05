fh = open('Output.txt', 'w')

a = int(input('Enter year: '))

if a % 4 == 0:
    result = f"{a} is a Leap Year."
else:
    result = f"{a} is Not a Leap Year."

print(result)
fh.write(result)

fh.close()
