PATH = 'output.txt'
def get_size_B(size: int):
    b_string = 'Сумма потребляемой памяти равна: '
    coeffs = [(1,'Б') , (1000, 'Кб'), (1000000, 'Мб') , (1000000000, 'Гб')]
    for i, (coeff, label) in enumerate(coeffs):
        rez = size // coeff
        if rez < 1:
            return(f'{b_string} {size // coeffs[i-1][0]} {coeffs[i-1][1]}')
    return(f'{b_string} {size // coeffs[-1][0]} {coeffs[-1][1]}')

def get_summary_rss(path: str):
    with open(path, 'r') as file:
        rez = sum([int(line.split()[5]) for line in file.readlines()[1:]])
        return(get_size_B(rez))

if(__name__) == '__main__':
    print(get_summary_rss(PATH))
