# Testing different types of looping
# Compare with loops.cpp

def main():

    # for loop over list
    print("for loop - list of states")
    states_list = ["Washington", "Oregon", "California"]
    for state in states_list:
        print("\t{}".format(state))

    # while loop over list
    print("while loop - list of states")
    i = 0
    while i < len(states_list):
        print("\t{}".format(states_list[i]))
        i += 1

    # loop over dictionary
    capitals_dict = {"Utah": "Salt Lake City", "California": "Sacramento", "New Mexico": "Santa Fe"}
    print("for loop - dict")
    for state, city in capitals_dict.items():
        print("\t{}: {}".format(state, city))

    # continue
    print("Evens to 10")
    for i in range(11):
        if i % 2 != 0:
            continue
        print("\t{}".format(i))

    # break
    print("To 5")
    for i in range(10):
        if i > 5:
            break
        print("\t{}".format(i))

    # for else
    print("Never find 100")
    for i in range(10):
        if i == 100:
            break
    else:
        print("\tNope")

    
if __name__ == "__main__":
    main()