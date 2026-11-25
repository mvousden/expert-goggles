import pytest
import sqrt

@pytest.fixture(params=[(-3, 0.5)])
def testcase(request) -> int:
    return request.param


def test_sqrt(testcase: int) -> None:
    assert sqrt.sqrt(testcase[0], testcase[1]) == testcase[0] ** testcase[1]
