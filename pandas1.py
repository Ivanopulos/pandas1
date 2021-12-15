import pandas as pd  # from https://khashtamov.com/ru/pandas-introduction/
import os  # nntoinst
from tkinter import filedialog
import numpy as np  # nntoinst
import datetime  # nntoinst
import dill  # from https://coderoad.ru/2960864/%D0%9A%D0%B0%D0%BA-%D1%81%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D1%8C-%D0%B2%D1%81%D0%B5-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%B2-%D1%82%D0%B5%D0%BA%D1%83%D1%89%D0%B5%D0%BC-%D1%81%D0%B5%D0%B0%D0%BD%D1%81%D0%B5-python

def myseries():
    my_series = pd.Series([5, 6, 7, 8, 9, 10])
    print(my_series.index)
    print(my_series.values)
    print(my_series[4])
    my_series[[1, 2, 5]] = 30
    print(my_series[my_series > 10])
    my_series.name = 'numbers'
    my_series.index.name = 'letters'
    print(my_series)
    my_series.index = ['A', 'B', 'C', 'D', 'E', 'F']
    print(my_series)
def midataframe():
    df = pd.DataFrame({
        'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
        'population': [17.04, 143.5, 9.5, 45.5],
        'square': [2724902, 17125191, 207600, 603628]
    })
    print(df['country'])
    df.index = ['KZ', 'RU', 'BY', 'UA']
    print(df.loc['KZ'])
    print(df.loc[['KZ', 'RU'], 'population'])
    print(df.loc['KZ': 'BY', :])
    print(df[df.population > 10][['country', 'square']])
    print(df[df['population'] > 10][['country', 'square']])
    print(df.iloc[0])
    df.reset_index()  # reset index
    df['density'] = df['population'] / df['square'] * 1000000  # new column
    df.drop(['density'], axis='columns')  # delete column
def pdopenfail(path=""):
    # df = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)
    if path == "":
        path = filedialog.askopenfilename() #  open in explorer
    if path.find("//")>0: #  if it full path
        print("found full path")
        print(path)
    else:
        print("guess path") #  if it not full path maybe it here or desktop
        print(os.getcwd()) #  https://ru.stackoverflow.com/questions/535318/%D0%A2%D0%B5%D0%BA%D1%83%D1%89%D0%B0%D1%8F-%D0%B4%D0%B8%D1%80%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D1%8F-%D0%B2-python
        if os.path.exists(os.getcwd() + "/" + path):
            print("found here")
            path=os.getcwd() + "/" + path
        if os.path.exists(os.environ['USERPROFILE'] + '\Desktop/' + path):
            print(os.environ['USERPROFILE'] + '\Desktop/' + path)
            path = os.environ['USERPROFILE'] + '\Desktop/' + path
    if path[len(path)-3:] == "csv":
        return pd.read_csv(path)
    if path[len(path) - 4:] == "xlsx" or path[len(path) - 3:] == "xls" or path[len(path) - 4:] == "xlsm":
        return pd.read_excel(path)
def dti():
    dti = pd.to_datetime(
    ["1/1/2018", np.datetime64("2018-01-01"), datetime.datetime(2018, 1, 1)]
    )
    print(dti)
    dti = pd.date_range("2018-01-01", periods=3, freq="H")
    print(dti)
    idx = pd.date_range("2018-01-01", periods=10, freq="H") # gz freq="H" M..
    ts = pd.Series(range(len(idx)), index=idx)
    print(ts)
    idx1 = pd.DataFrame(idx)
    print(idx1, "here")
    idx1.columns=['Date']
    idx1 = idx1.sort_values("Date", axis=0)
    idx1= idx1.apply(pd.to_datetime)
    idx1['cour']=5
    idx1.set_index('Date', inplace=True)
    print(idx1, "here1")
    #pd.to_datetime(idx1, infer_datetime_format=True)
    print(idx1.resample("2H").last().diff()) #  gz !!!!!!!! #.mean() средний .interpolate оставить последний .ohlc() open high low close .diff() for df .last().diff() for series
    #df.loc['2012-Feb':'2015-Feb', 'Close'].diff()
    print(idx[0])
    print((idx[0]+ pd.Timedelta("1 day") + pd.offsets.BDay()).day_name())
    #df.resample('W')['finish'].mean()

    # pd.Timestamp(datetime.datetime(2012, 5, 1))
    # Out: Timestamp('2012-05-01 00:00:00')
    # pd.Timestamp("2012-05-01")
    # Out: Timestamp('2012-05-01 00:00:00')
    # pd.Timestamp(2012, 5, 1)
    # Out: Timestamp('2012-05-01 00:00:00')
    # pd.Period("2012-05", freq="D")
    # Out: Period('2012-05-01', 'D')

    # pd.DatetimeIndex(["2018-01-01", "2018-01-03", "2018-01-05"], freq="infer")
    # Out: DatetimeIndex(['2018-01-01', '2018-01-03', '2018-01-05'], dtype='datetime64[ns]', freq='2D') # freq='2D')

    # pd.to_datetime("2010/11/12", format="%Y/%m/%d") # gz fast
    # Out[51]: Timestamp('2010-11-12 00:00:00')
    # pd.to_datetime("12-11-2010 00:00", format="%d-%m-%Y %H:%M")
    # Out[52]: Timestamp('2010-11-12 00:00:00')
def seq1():
    x = np.linspace(1, 25, num=25)  # numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
    print(x,'001')
    df = pd.DataFrame(np.sin(x) * np.random.randint(10, 50), columns=['Curve'])
    df.columns = ['curve']
    print(df,'002')
    print(df.curve)
    print(df.curve.shift(-1), '0021')
    a = df.curve - df.curve.shift(-2) < 0
    b = df.curve - df.curve.shift(-1) < 0
    b1 = df.curve < 0
    c = a & b & b1  # use | for 'or'
    print(a, b, b1, c, '003')
    #c = np.logical_or(a, b) has 2 operand, that'swhy not to kc
    print(c,'004')
    d = (c != c.shift()).cumsum() # фактически счетчик серий ответов не включая(шифт) себя
    print(d,'005')
    df['c'] = c #  new column to
    df['d'] = d
    print(df,'006')
    df = df.groupby(d).filter(lambda x: all(x['c'])) # filter looks where is true //f.e. for print use list(filter(lambda s: len(s)>3,['hjg','hfgh'....]
    #n = 1
    #print(list(map(lambda n: n * 2, [1, 2, 3, 4, 5]))) #! map runs over the list[1,2,3,4,5] and over the def/lambda.
    print(df,'007')
    max_group = df.loc[df.groupby(d).cumcount().idxmax()]['d']
    print(max_group,'008')
    df_added = df.loc[df['d'] == max_group]
    print(df_added,'009')
    return df
def snl_session(fn="savedsession.pkl"):
    if os.path.exists(fn):  # os.path.isfile() if needed to check this folder or file
        dill.load_session(fn)
        print('session loaded')
    else:
        dill.dump_session(fn)
        print('session saved')

