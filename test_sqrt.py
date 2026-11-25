import pytest
import sqrt

@pytest.fixture(params=[-3, 5, 7, 9])
def testcase(request) -> int:
    return request.param


def test_sqrt(testcase: int) -> None:
    assert sqrt.sqrt(testcase) == testcase ** 0.5
