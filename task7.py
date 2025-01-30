from flask import Flask
import pandas as pd

def html_wrapper(text):
    html = f'''
        <div style="text-align: center;">
        <h1>{text}</h1>
        </div>
    '''
    return html

app = Flask(__name__)


#COST_LIST = []

DF_INIT = pd.DataFrame(data= [['20001201', 0]], columns = ['data', 'cost'])
DF_INIT['data'] = pd.to_datetime(DF_INIT['data'])
DF_INIT.set_index('data', inplace=True)


@app.route('/add/<date>/<int:number>') # сохранение информации о совершённой в рублях трате за какой-то день;
def add_record(date, number):
    global DF_INIT
    DF_INIT.loc[-1] = [[date, number]]
    return(html_wrapper(f'Данные добавлены успешно. Всего записей {DF_INIT.shape}'))


@app.route('/calculate/<int:year>') # получение суммарных трат за указанный год;
def year_cost(year):
    #df = convert_list_to_df(COST_LIST)
    html = html_wrapper(f'Суммарные затраты за {year} год равны {DF_INIT.loc[f'{year}'].sum().tolist()[0]}')
    return(html)

@app.route('/calculate/<int:year>/<int:month>') # получение суммарных трат за указанные год и месяц
def month_cost(year, month):
    html = html_wrapper(f'Суммарные затраты за {year} год и {month} месяц равны {DF_INIT.loc[f'{year}-{month}'].sum().tolist()[0]}')
    return(html)


if __name__ == '__main__':
  
    app.run(debug=True)