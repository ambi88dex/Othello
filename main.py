from game import State

def main():
    start = State() 
    start.initialise()
    # print(start)
    x = start.play_move(3,5)
    print(start)
    y = start.play_move(3,6)
    print(start)

if __name__ == "__main__":
    main()