if __name__ == '__main__':
    n = int(input())
    if 1<=n<=150:
        print_range = range(1,n+1)
        for i in print_range:
            print(i, end='')
