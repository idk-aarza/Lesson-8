speed1=int(input('Enter your first speed'))
speed2=int(input('Enter your second speed'))
speed3=int(input('Enter your third speed'))
total=3
average=(speed1+speed2+speed3) /total
print(average)

if speed1<average:
    print('The speed 1 is slow', average-speed1)
elif speed2<average:
    print('The speed 2 is slow', average-speed2)
elif speed3<average:
    print('The speed 3 is slow', average-speed3)
else:
    print("invalid")