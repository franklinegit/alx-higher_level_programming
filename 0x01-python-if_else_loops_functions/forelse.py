#!/usr/bin/python3

def for1():
    print("for-else without break statement")
    for i in range(3):
        print(i)
    else:
        print("Loop completed successfully.")
    print("")
            
def for2():
    print("for-else with break statement")
    for i in range(4):
        if i == 3:
            break
        print(i)
    else:
        print("Loop completed successfully.")
    print("")
    
            

def main():
    for1()
    for2()

if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print("Error occured: ", e)