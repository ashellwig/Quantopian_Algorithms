"""
Title: Dual Moving Average Algorithm (DMA.py)
Author: Quantoptian (Quickstart Guide)
Date: 14|08|2017
Purpose: Learn Quantoptian Syntax
"""

from zipline.api import order_target, record, symbol


def initialize(context):
    context.i = 0
    context.asset = symbol('CIM')  # Chimera Investment Corp.


def handle_data(context, data):
    # Skipping first 300 days for full windows
    context.i += 1
    if context.i < 300:
        return

    # Computing the averages
    short_mavg = data.history(context.asset, 'price', bar_count=100,
                              frequency="1d").mean()
    long_mavg = data.history(context.asset, 'price', bar_count=300,
                             frequency="1d").mean()

    # Trading Logic
    if short_mavg > long_mavg:
        order_target(context.asset, 100)
    elif short_mavg < long_mavg:
        order_target(context.asset, 0)

    # Save Values
    record(CIM=data.current(context.asset, 'price'),
           short_mavg=short_mavg,
           long_mavg=long_mavg)
