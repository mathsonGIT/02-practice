import sys
def one_point_processing(text:str):
    return(''.join(text.split('.')))

def two_points_processing(text: str):
    
    decifr = text.split('..')
    size = len(decifr)
    for i, _c in enumerate(decifr):
        print(_c)
        temp = _c
        num_outliers = 1
        while len(temp) == 0:
            if (i+num_outliers) < size:
                temp = decifr[i+num_outliers]
            else:
                break
            num_outliers += 1
        decifr[i-1] = decifr[i-1][:-num_outliers]
 
    return one_point_processing(''.join(decifr))


            
    print(cifr.split('.'))

if(__name__) == '__main__':
    text = sys.stdin.read()
    print(two_points_processing(text))