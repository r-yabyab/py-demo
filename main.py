def main():
    print("hello")
    # file = open("numbers.txt", "r")
    # file = open("data.txt", "r")
    with open("data.txt", "r") as file:
        # lines = file.readlines()
    

        print(file.readline().split()[1])

    # for line in lines:
    #     print("LINES")
    #     print(line)
    #     parts = line.split()
    #     print("PARTS")
    #     print(parts[0])
    #     # number = int(parts[1])
    #     # print(number)

def main1():
    print("sub")


if __name__ == "__main__":
    main()