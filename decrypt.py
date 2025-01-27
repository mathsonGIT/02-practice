import sys
def decrypt():
    cifr = sys.stdin.read()
    decifr = cifr.split('..')
    rezult = []
    for i, _c in enumerate(decifr):
        print(_c)
        if len(_c) == 0:
            rezult[i-1] = (decifr[i-1][:-1])
        else:
            rezult.append(_c[:-1])
    
    return ''.join(rezult)


            
    print(cifr.split('.'))

if(__name__) == '__main__':
    print(decrypt())