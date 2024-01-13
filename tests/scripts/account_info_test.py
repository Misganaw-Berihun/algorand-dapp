import unittest
import tempfile
import os
import yaml

class TestGetKeysFunction(unittest.TestCase):

    def setUp(self):
        self.temp_yaml_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        self.temp_yaml_file.write("""
        accounts:
          tutor:
            address: "tutor_address"
            mnemonic: "tutor_mnemonic"
            private_key: "tutor_private_key"
          trainee_1:
            address: "trainee_1_address"
            mnemonic: "trainee_1_mnemonic"
            private_key: "trainee_1_private_key"
          trainee_2:
            address: "trainee_2_address"
            mnemonic: "trainee_2_mnemonic"
            private_key: "trainee_2_private_key"
        """)

    def tearDown(self):
        os.remove(self.temp_yaml_file.name)

    def test_get_keys_tutor(self):
        tutor_keys = get_keys("tutor", self.temp_yaml_file.name)
        expected_keys = {
            "address": "tutor_address",
            "mnemonic": "tutor_mnemonic",
            "private_key": "tutor_private_key"
        }
        self.assertEqual(tutor_keys, expected_keys)

    def test_get_keys_trainee_1(self):
        trainee_1_keys = get_keys("trainee_1", self.temp_yaml_file.name)
        expected_keys = {
            "address": "trainee_1_address",
            "mnemonic": "trainee_1_mnemonic",
            "private_key": "trainee_1_private_key"
        }
        self.assertEqual(trainee_1_keys, expected_keys)

    def test_get_keys_trainee_2(self):
        trainee_2_keys = get_keys("trainee_2", self.temp_yaml_file.name)
        expected_keys = {
            "address": "trainee_2_address",
            "mnemonic": "trainee_2_mnemonic",
            "private_key": "trainee_2_private_key"
        }
        self.assertEqual(trainee_2_keys, expected_keys)

if __name__ == '__main__':
    unittest.main()
