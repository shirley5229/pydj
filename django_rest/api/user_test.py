import unittest
import requests

class UserTest(unittest.TestCase):
    """用户查询测试"""
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/users"

    def test_user1(self):
        ''' '''
        r = requests.get(self.base_url+'/1/',auth=('admin','django123'))
        result=r.json()
        print(result)
        self.assertEqual(result['username'],'admin')
        self.assertEqual(result['email'],'admin@admin.com')




if __name__=="__main__":
    unittest.main()
