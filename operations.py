import operator


def contains(target, reference):
    return reference in target

OPERATIONS = {
    'contains': contains,
    'equal': operator.eq,
    'notequal': operator.ne,
}
