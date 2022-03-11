import allure
import time

# Retries
# Allure allows you to aggregate information about test being re-executed during
# a single test run as well as history of test execution over some period of time.
#
# For retries you can use Pytest rerun failures plugin.
#
# For example if we have a very unreliable step method that fails often,
# after specifying --reruns=5 in the Pytest startup options we would see
# all unsuccessful attempts to run this test displayed on the Retries tab.

import random

@allure.step
def passing_step():
    pass


@allure.step
def flaky_broken_step():
    if random.randint(1, 5) != 1:
        raise Exception('Broken!')


def test_broken_with_randomized_time():
    passing_step()
    time.sleep(random.randint(1, 3))
    flaky_broken_step()
