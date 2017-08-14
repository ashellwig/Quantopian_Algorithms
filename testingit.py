from zipline.examples import buyapple
from zipline.api import order, symbol, record

buyapple??


def initialize(context):
    pass


def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data.current(symbol('AAPL'), 'price'))

run_algorithm()
