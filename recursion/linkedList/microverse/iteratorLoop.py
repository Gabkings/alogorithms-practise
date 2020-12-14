import re


def solution(file_object):
    file_iterator = iter(file_object)

    while True:
        line = next(file_iterator, "#").strip(' ').strip('\n')
        if line == '#':
            break
        matches = re.match(r'^(|[+\-])([1-9][0-9]*|[0-9])$', line)
        if matches is not None:
            numeric = int(line)
            if 1000000000 >= numeric >= -1000000000:
                if len(str(numeric)) == len(line) or (line[0] in '+-'):
                    yield line
    return
