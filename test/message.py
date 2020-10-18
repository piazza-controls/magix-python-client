import json
import unittest

from magix_client import Message

json_str = '{"id":12345,"origin":"test"}'
json_with_payload = '{"id":12345,"origin":"test","payload":{"foo":"bar"}}'


class TestMessageFrom(unittest.TestCase):

    def test_from_json(self):
        msg = Message.from_json(json_str)
        assert msg != None
        assert msg.id == 12345
        assert msg.origin == 'test'
        pass

    def test_from_json_with_payload(self):
        class Payload:
            def __init__(self, foo):
                self.foo = foo

        msg = Message.from_json(json_with_payload, Payload)
        assert msg != None
        assert msg.id == 12345
        assert msg.origin == 'test'
        assert msg.payload.foo == 'bar'
        pass

    def test_to_json(self):
        msg = Message(id=1, origin='test')
        print(json.dumps(msg, default=(lambda o: o.__dict__)))
        pass


if __name__ == '__main__':
    unittest.main()
