import pytest
import allure
# Basic Reporting
# Test with no errors - Success
# Assert fail - status fail
# any other exception - status is broken
# skipped for some reason - status is skipped

class TestBasicReporting:
    def test_success(self):
        """this test succeeds"""
        assert True
    def test_failure_due_to_assert_fail(self):
        """this test fails"""
        assert False
    def test_skip(self):
        """this test is skipped"""
        pytest.skip('for a reason!')
    def test_broken(self):
        raise Exception('oops')


# Tests with pytest Xfail.

@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    xfail_step()
    assert False

@allure.step
def xfail_step():
    pass

# conditional Mark

@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_unexpected_pass():
    """this test is an xfail that will be marked as unexpected success"""
    assert True

@pytest.mark.skipif('2 + 2 != 5', reason='This test is skipped by a triggered condition in @pytest.mark.skipif')
def test_skip_by_triggered_condition():
    pass

@pytest.mark.skipif('2 + 2 != 4', reason='This test is skipped by a triggered condition in @pytest.mark.skipif')
def test_not_skip_as_triggered_condition_not_true():
    pass
