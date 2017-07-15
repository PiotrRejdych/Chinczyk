'''
>>> check_json()
True
>>> check_json_negative()
False
'''

import re


def check_json():
    json = '{' \
           ' "product_id": 2,' \
           ' "title" : "sample product",' \
           ' "description": "product\n description\n"' \
           '}'
    pattern = r'\{(\s*\"[a-zA-Z0-9_]+\"\s*:\s*(\d+|(\"[a-zA-Z0-9_\s]*\")),?)*\}'
    regexp = re.compile(pattern)
    return bool(regexp.match(json))


def check_json_negative():
    json = '{' \
           ' "product_id: 2,' \
           ' "title" : "sample product",' \
           ' "description": "product\n description\n"' \
           '}'
    pattern = r'\{(\s*\"[a-zA-Z0-9_]+\"\s*:\s*(\d+|(\"[a-zA-Z0-9_\s]*\")),?)*\}'
    regexp = re.compile(pattern)
    return bool(regexp.match(json))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
