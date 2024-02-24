x = int(input("Enter number of candies to buy: "))
avail_candies = 6
i = 1

while i <= x:
    if x > avail_candies:
        print("Not enough stock: Only {} candies available".format(avail_candies))
        break
    
    else:
        print("candy {}".format(i))
    i += 1
    avail_candies -= 1

print("candies left in stock: {}".format(avail_candies))


colours = ["blue", "red", "green", "yellow"]
show = str(input("Enter colour of choice: "))
ncol = int(input("How many times do you want the colour printed out: "))

for c in colours:
    if c != show:
        print("You do not want: {}".format(c))
        continue
    
    else:
        print("You want: ")
        print(ncol * c)
