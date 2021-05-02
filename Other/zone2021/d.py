from collections import deque

def main():
    s = input()
    t = deque([])
    r = 0
    for i in s:
        if i == 'R':
            r += 1
            continue
        
        if t == deque([]):
            t.append(i)
        else:
            if r % 2 == 1 and i != t[0]:
                t.appendleft(i)
            elif r % 2 == 1 and i == t[0]:
                t.popleft()
            elif r % 2 == 0 and i != t[-1]:
                t.append(i)
            elif r % 2 == 0 and i == t[-1]:
                t.pop()
    
    ans = ''.join(t)
    print(ans[::-1] if r % 2 else ans)

if __name__ == '__main__':
    main()