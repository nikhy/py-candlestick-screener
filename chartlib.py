import os, pandas

def is_consolidating(df, percentage=2):
    recent_candlesticks = df[-15:]
    
    max_close = recent_candlesticks['close'].max()
    min_close = recent_candlesticks['close'].min()

    threshold = 1 - (percentage / 100)
    if min_close > (max_close * threshold):
        return True        

    return False

def is_breaking_out(df, percentage=2.5):
    last_close = df[-1:]['close'].values[0]

    if is_consolidating(df[:-1], percentage=percentage):
        recent_closes = df[-16:-1]

        if last_close > recent_closes['close'].max():
            return True

    return False

for filename in os.listdir('datasets/daily'):
    df = pandas.read_csv('datasets/daily/{}'.format(filename))
    
    if is_consolidating(df, percentage=2):
        print("{} is consolidating".format(filename))

    if is_breaking_out(df):
        print("{} is breaking out".format(filename))