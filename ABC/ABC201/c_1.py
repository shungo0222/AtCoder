def main():
    s = input()
    
    o = [str(i) for i in range(10) if s[i] == 'o']
    x = [str(i) for i in range(10) if s[i] == 'x']
    
    ans = 0
    for i in range(10000):
        i = str(i).zfill(4)
        
        flag = True
        for j in o:
            if j not in i:
                flag = False
                break
        
        if flag:
            for j in x:
                if j in i:
                    flag = False
                    break
            
            if flag:
                ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()