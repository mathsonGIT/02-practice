
from flask import Flask
from datetime import datetime
import os


weekdays = ('Хорошего понедельника', 'Хорошего вторника', 'Хорошей среды', 'Хорошего четверга', 'Хорошей пятницы', 'Хорошей субботы', 'Хорошего воскресенья')

def html_wrapper(text):
    html = f'''
        <div style="text-align: center;">
        <h1>{text}</h1>
        </div>
    '''
    return html

def is_float(value):
  if value is None:
      return False
  try:
      float(value)
      return True
  except:
      return False


app = Flask(__name__)


@app.route('/hello-world/<string:name>')
def hello_function(name):
    weekday_string = weekdays[datetime.today().weekday()]
    html = html_wrapper(f'Привет, {name}. {weekday_string}')
    return html

@app.route('/max_number/<path:numbers>')
def max_numbers(numbers):
    n_list = numbers.split('/')
    rezult = max([float(number) for number in n_list if is_float(number)])
    return(html_wrapper(f'Максимальное число в строке равно {int(rezult)}'))


BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt') 

@app.route('/head_file/<int:size>/<path:relative_path>')
def file_processing(size: int, relative_path: str) -> str:
    FILE = os.path.join(BASE_DIR, relative_path)
    abs_path = os.path.abspath(FILE)
    with open(abs_path, 'r') as file:
        rezult_text = file.read(size)
        rezult_size = len(rezult_text)
    html = html_wrapper(f'''<ul>
        <li>Абсолютный путь к файлу: {abs_path}</li>
        <li>Размер содержимого : {rezult_size}</li>
        <li>Содержимое файла : {rezult_text} </li>
        </ul>
        ''')
    return(html)

#Accouting Finance Application endpoints
import pandas as pd
#COST_LIST = []
#def convert_list_to_df(records):
#    df = pd.DataFrame(records, columns = ['data', 'cost'])
#    df['data'] = pd.to_datetime(df['data'])
#    df.set_index('data', inplace=True)
#    return(df)
#COST_DF = pd.DataFrame(, columns = ['data', 'cost'])

@app.route('/add/<date>/<int:number>') # сохранение информации о совершённой в рублях трате за какой-то день;
def add_record(date, number):
    global COST_LIST
    COST_LIST.append([date, number])
    return(html_wrapper(f'Данные добавлены успешно. Всего записей {len(COST_LIST)}'))


@app.route('/calculate/<int:year>') # получение суммарных трат за указанный год;
def year_cost(year):
    df = convert_list_to_df(COST_LIST)
    html = html_wrapper(f'Суммарные затраты за {year} год равны {df.loc[f'{year}'].sum().tolist()[0]}')
    return(html)

@app.route('/calculate/<int:year>/<int:month>') # получение суммарных трат за указанные год и месяц
def month_cost(year, month):
    df = convert_list_to_df(COST_LIST)
    html = html_wrapper(f'Суммарные затраты за {year} год и {month} месяц равны {df.loc[f'{year}-{month}'].sum().tolist()[0]}')
    return(html)


if __name__ == '__main__':
    app.run(debug=True)
