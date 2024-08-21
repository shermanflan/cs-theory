from collections import deque


class QueueException(Exception):
    pass


# TODO:
# Opt1: Use an array as the backing store. Requires tracking head and tail
# pointers. Queue can loop around as well.
class Queue(object):
    """
    Uses a deque for base model structure. More efficient than a list.
    Canonical implementation uses a linked list as a base model structure.
    """

    def __init__(self, *args):
        super().__init__()
        self.__values = deque(args)

    def add(self, data):
        self.__values.append(data)

    def remove(self):
        if self.__values:
            return self.__values.popleft()
        else:
            raise QueueException('Queue is empty!')

    def peek(self):
        if self.__values:
            return self.__values[0]
        else:
            raise QueueException('Queue is empty!')

    def isEmpty(self):
        if self.__values:
            return False
        else:
            return True

    def __repr__(self):
        return str(list(self.__values))