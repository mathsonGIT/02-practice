from flask import Flask

def html_wrapper(text):
    html = f'''
        <div style="text-align: center;">
        <h1>{text}</h1>
        </div>
    '''
    return html

app = Flask(__name__)


#COST_LIST = []

storage = dict()
COUNT_RECORDS = 0

@app.route('/add/<date>/<int:number>') # сохранение информации о совершённой в рублях трате за какой-то день;
def add_record(date, number):
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
    global storage
    global COUNT_RECORDS
    storage.setdefault(year, {}).setdefault(month, {}).setdefault(day, 0)
    storage[year][month][day] += number
    storage[year]['total'] = storage[year].get('total', 0) + number
    storage[year][month]['total'] = storage[year][month].get('total', 0) + number
    COUNT_RECORDS += 1
    return(html_wrapper(f'Данные добавлены успешно. Всего записей {COUNT_RECORDS}'))


@app.route('/calculate/<int:year>') # получение суммарных трат за указанный год;
def year_cost(year):
    global storage
    try:
        html = html_wrapper(f'Суммарные затраты за {year} год равны {storage.get(year, 0).get('total', 0)}')
    except:
        html = html_wrapper(f'Данные за {year} год отсутствуют')
    return(html)

@app.route('/calculate/<int:year>/<int:month>') # получение суммарных трат за указанные год и месяц
def month_cost(year, month):
    global storage
    try:
        html = html_wrapper(f'Суммарные затраты за {year} год и {month} месяц равны {storage[year][month].get('total', 0)}')
    except:
        html = html_wrapper(f'Данные за {year} год и {month} отсутствуют')
    return(html)


if __name__ == '__main__':
  
    app.run(debug=True)