import pytest
# Depending on an outcome of a fixture execution,
# test that is dependent on it may receive a different status.
# Exception in the fixture would make all dependent tests broken,
# pytest.skip() call would make all dependent test skipped.

@pytest.fixture
def skip_fixture():
    pytest.skip()


@pytest.fixture
def fail_fixture():
    assert False


@pytest.fixture
def broken_fixture():
    raise Exception("Sorry, it's broken.")


def test_with_pytest_skip_in_the_fixture(skip_fixture):
    pass


def test_with_failure_in_the_fixture(fail_fixture):
    pass


def test_with_broken_fixture(broken_fixture):
    pass
