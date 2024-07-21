#!/usr/bin/python3


my_tuple = ()


def index_range(page, page_size):
    my_tuple = ((page - 1) * page_size, page_size * page)
    return my_tuple
