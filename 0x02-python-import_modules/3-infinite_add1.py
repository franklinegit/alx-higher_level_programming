#!/usr/bin/python3

if __name__ == "__main__":
    
    import sys
    try:
        summ = 0
        for i in range(1, len(sys.argv)):
            summ += int(sys.argv[i])
        print("Total = {}".format(summ))
        
    except ValueError:
        print("Invalid input value.", file=sys.stderr)
    except TypeError:
        print("Invalid input type.", file=sys.stderr)
    except Exception as e:
        print("Error; {e}", file=sys.stderr)
    else:
        print("Infinite addition successful.")
        print("")