from distutils import command


def command_list():
    """ Hackerrank, function performs commands on list from user input.
    """
    # First integer from user will be the number of commands to be expected
    N = int(input())
    arr = []
    
    # Splitting each command and checking which one it is
    for _ in range(N):
        command = input().split(" ")
        if command[0] == "insert":
            arr.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(arr)
        elif command[0] == "remove":
            arr.remove(int(command[1]))
        elif command[0] == "append":
            arr.append(int(command[1]))
        elif command[0] == "sort":
            arr.sort()
        elif command[0] == "pop":
            arr.pop()
        elif command[0] == "reverse":
            arr.reverse()


command_list()
