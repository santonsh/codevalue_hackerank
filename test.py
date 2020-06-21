import unittest
import string
import random


def input_check(func):
    def check_wrapper(key, message):
        # empty message case
        if message is None or message == '':
            return ''

        # wrong key case
        ab_len = 26
        if len(key) != ab_len or len(set(key)) != ab_len or not key.isupper() or not key.isalpha():
            raise Exception("wrong encryption key")

        return func(key, message)

    return check_wrapper


def mapping_dict(orig_AB, dest_AB):
    ''' An aux function to creat a mapping dictionary from original ab to new ab '''
    map_dict = {}
    for idx, c in enumerate(orig_AB):
        map_dict[c] = dest_AB[idx]
        map_dict[c.lower()] = dest_AB[idx].lower()

    return map_dict


@input_check
def encrypt(key, message):
    map_dict = mapping_dict(string.ascii_uppercase, key)
    enc = [map_dict[c] for c in message]
    return ''.join(enc)


@input_check
def decrypt(key, message):
    map_dict = mapping_dict(key, string.ascii_uppercase)
    dec = [map_dict[c] for c in message]
    return ''.join(dec)


class TestEncDec(unittest.TestCase):

    def test_enc_dec(self):
        ab = string.ascii_uppercase
        key = ''.join(random.sample(ab, len(ab)))
        msg = 'HelloWorld'
        enc = encrypt(key, msg)
        dec = decrypt(key, enc)
        print(f"key is {key}")
        print(f'original msg is: {msg}')
        print(f'encrypted msg is: {enc}')
        print(f'decrypted msg is: {dec}')
        self.assertEqual(msg, dec)

    def test_msg(self):
        self.assertEqual(encrypt(None, '')+decrypt(None, ''), '')
        self.assertEqual(encrypt(None, None)+decrypt(None, None), '')

    def test_key(self):
        ab = string.ascii_uppercase
        key = ''.join(random.sample(ab, len(ab)))
        msg = 'HelloWorld'

        with self.assertRaises(Exception):
            # wrong len
            wrong_key = key[:-1]
            encrypt(wrong_key, msg)
        with self.assertRaises(Exception):
            # non unique ab
            wrong_key = key[:-1]+key[-2]
            encrypt(wrong_key, msg)
        with self.assertRaises(Exception):
            # not alphanumerical
            wrong_key = key[:-1]+'1'
            encrypt(wrong_key, msg)
        with self.assertRaises(Exception):
            # not all capital
            wrong_key = key[:-1]+key[-1].lower()
            encrypt(wrong_key, msg)


if __name__ == '__main__':
    unittest.main()
