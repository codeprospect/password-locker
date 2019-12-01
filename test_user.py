import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("waikau", "maina", "4568")

    def testInit(self):
        self.assertEqual(self.new_user.firstName, 'waikau')
        self.assertEqual(self.new_user.secondName, 'maina')
        self.assertEqual(self.new_user.password, '4568')

    def tearDown(self):
        User.users = []

    def test_save(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users), 1)

    def test_display(self):
        self.assertEqual(User.display_users(), User.users)

    def test_find_by_name(self):
        self.new_user.save_user()
        test_user = User("newton", "ngure", "4678")
        test_user.save_user()
        found_user = User.find_by_name('newton')
        self.assertEqual(found_user.secondName, 'ngure')

if __name__ == '__main__':
    unittest.main()
