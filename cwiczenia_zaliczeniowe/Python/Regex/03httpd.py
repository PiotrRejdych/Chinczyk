'''
>>> check_logs()
True
>>> check_logs_negative()
False
'''

import re


def check_logs():
    log = "[Wed Oct 11 14:32:52 2000] [error] [client 127.0.0.1] client denied by server configuration: /export/home/live/ap/htdocs/test"
    pattern = r"\[.*\] \[error\] \[.*\] [a-zA-Z0-9_:/ ]*"
    regexp = re.compile(pattern)
    return bool(regexp.match(log))


def check_logs_negative():
    log = "[Wed Oct 11 14:32:52 2000] [client 127.01.0.1] client denied by server configuration: /export/home/live/ap/htdocs/test"
    pattern = r"\[.*\] \[error\] \[.*\] [a-zA-Z0-9_:/ ]*"
    regexp = re.compile(pattern)
    return bool(regexp.match(log))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
