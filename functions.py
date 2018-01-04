# -*- coding: utf-8 -*-

def most_common(lst):
    return max(set(lst), key=lst.count)

def less_common(lst):
    return min(set(lst), key=lst.count)

def foo():
    pass
    
