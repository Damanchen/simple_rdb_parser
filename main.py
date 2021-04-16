from parser import RdbParser, RdbCallback
from encodehelpers import bytes_to_unicode
import time


class MyCallback(RdbCallback):
    ''' Simple example to show how callback works.
        See RdbCallback for all available callback methods.
        See JsonCallback for a concrete example
    '''

    def __init__(self):
        super(MyCallback, self).__init__(string_escape=None)

    def encode_key(self, key):
        return bytes_to_unicode(key, self._escape, skip_printable=True)

    def encode_value(self, val):
        return bytes_to_unicode(val, self._escape)

    def set(self, key, value, expiry, info):
        print('%s = %s' % (self.encode_key(key), self.encode_value(value)))

    def hset(self, key, field, value):
        print('%s.%s = %s' % (self.encode_key(key), self.encode_key(field), self.encode_value(value)))

    def sadd(self, key, member):
        print('%s has {%s}' % (self.encode_key(key), self.encode_value(member)))

    def rpush(self, key, value):
        print('%s has [%s]' % (self.encode_key(key), self.encode_value(value)))

    def zadd(self, key, score, member):
        print('%s has {%s : %s}' % (str(key), str(member), str(score)))

    def aux_field(self, aux_key, aux_val):
        print('%s = %s' % (self.encode_key(aux_key), self.encode_value(aux_val)))

    def start_module(self, key, length, expiry, info):
        print("Start of module key: %s, module name: %s, expire: %s, info: %s" % (key, length, expiry, info))
        return True

    def handle_module_data(self, key, opcode, data):
        print(key, opcode, data)

    def end_module(self, key, buffer_size=None, buffer=None):
        print("End of module, key: %s, buffer_size: %s, buffer: %s\n" % (key, buffer_size, buffer))

    def print_some_log(self, log):
        print(log)


if __name__ == '__main__':
    callback = MyCallback()
    parser = RdbParser(callback)
    parser.parse('/path/to/dump.rdb')
