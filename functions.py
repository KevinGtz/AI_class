# -*- coding: utf-8 -*-

def most_common(lst):
    return max(set(lst), key=lst.count)
