# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    inp = input()
    if "I" in inp:
        rinda1=input().strip()
        rinda2=input().strip()
        return(rinda1,rinda2)
    if "F" in inp:
        with open('./tests/06') as test:
            t1=test.readline().strip()
            t2=test.readline().strip()
        return (t1,t2)
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pat, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    p = len(pat)
    t = len(text)

    oc = []

    phash = hash(pat)
    thash = hash(text[:p])

    for i in range(t-p+1):
        if phash == thash and text[i:i+p] == pat:
            oc.append(i)

        if i < t-p:
            thash = hash(text[1+i:1+p+i])
    

    # and return an iterable variable
    return oc

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
