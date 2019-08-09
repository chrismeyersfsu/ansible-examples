import mock
from copy import copy


def test_mock_dir():
    _dir = __builtins__['dir']
    print("Dir is {}".format(_dir))
    def mydir():
        print("about to call dir and it is {}".format(_dir))
        return _dir()


    #with mock.patch('__main__.__builtins__.dir', side_effect=mydir):
    with mock.patch('__main__.__builtins__.dir', return_value=[]):
        import foo
