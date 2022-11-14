if __name__ == '__main__':
    n = int(input())
    
    if 1<=n<=20:
        num_range = range(0,n)
        for num_item in num_range:
            print(num_item * num_item)
        
    
