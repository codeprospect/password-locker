import unittest
from generate import Generator

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.new_user = Generator("instagram", "codeprospect", "4568")

    def testinit(self):
        self.assertEqual(self.new_user.media, 'instagram')
        self.assertEqual(self.new_user.account, 'codeprospect')
        self.assertEqual(self.new_user.password, '4568')

    def testSave(self):
        self.new_user.save_passwords()
        self.assertEqual(len(Generator.passwords),1)

    def testpasswordGenerator(self):
        passwordd = Generator.password('8')
        self.assertEqual(Generator.passwords[1], passwordd)

    def testDisplayPasswords(self):
        self.assertEqual(Generator.display_passwords(),Generator.passwords)

if __name__ == '__main__':
    unittest.main()
