def replace(s):
    l = []
    for i in range(len(s)):
        if(s[i] == ' '):
            l.append('%20')
        else:
            l.append(s[i])
    return "".join(l)

if __name__ == '__main__':
    s = "We are Happy!"
    print(replace(s))