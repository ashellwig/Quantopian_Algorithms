'''
Title: Dual Moving Average Algorithm (DMA.py)
Author: Quantoptian (Quickstart Guide)
Date: 14|08|2017
Purpose: Learn Quantoptian Syntax
'''

from zipline.api import order_target, record, symbol


def initialize(context):
    context.i = 0
    context.asset = symbol('CIM')