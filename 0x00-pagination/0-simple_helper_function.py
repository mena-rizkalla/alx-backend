#!/usr/bin/python3


def index_range(page, page_size) -> tuple:
    my_tuple = ((page - 1) * page_size, page_size * page)
    return my_tuple
