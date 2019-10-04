import pandas as pd
import numpy as np

from fbprophet import Prophet


def get_historical_stock_price(stock):
    print "Getting historical stock prices for stock ", stock
    url = "http://real-chart.finance.yahoo.com/table.csv?s=%s&ignore=.csv" % (
        stock)
    # print url
    c = pd.read_csv(url)
    return c


def main():
    stock = raw_input("Enter stock name(ex:GOOGL, AAPL): ")
    df_whole = get_historical_stock_price(stock)

    df = df_whole.filter(['Date', 'Close'], axis=1)

    df.columns = ['ds', 'y']
    df['y'] = np.log(df['y'])

    m = Prophet()
    m.fit(df)

    num_days = int(raw_input("Enter no of days to predict stock price for: "))
    future = m.make_future_dataframe(periods=num_days)
    forecast = m.predict(future)

    plt = m.plot(forecast)
    plt.show()

    plt = m.plot_components(forecast)
    plt.waitforbuttonpress()
    plt.show()


if __name__ == "__main__":
    print "hello"
    main()
