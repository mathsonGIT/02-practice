import sys 
def get_mean_size():
    lines = sys.stdin.readlines()[1:]
    size = len(lines)
    b_string = 'Средний размер файлов равен: '
    if size > 0:
        rez = 0
        for line in lines:
            try:
                rez += int(line.split()[4])
            except:
                continue
        return(f'{b_string} {rez/size}')
    else:
        return(f'{b_string} {rez}')


if(__name__) == '__main__':
    print(get_mean_size())