import pytest
#session,module,class,function
@pytest.fixture(scope='function',autouse=True)
def session_fixture():
    print("class----")