import pytest

if __name__ == '__main__':
    pytest.main(['-s', '-m=debug','--alluredir','./report/xml'])
    # pytest.main(['-s','-m=info'])
    # pytest.main(['-s', '-m=a'])
    # pytest.main(['-s'])