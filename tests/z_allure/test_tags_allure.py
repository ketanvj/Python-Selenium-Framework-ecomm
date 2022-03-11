import allure

# Tags

# Grouping your tests, filtering the execution by groups
# 3 types
# 1. BDD-style markers denoting Epics, Features and Stories
# 2. Severity labels
# 3. Custom labels


def test_without_any_annotations_that_wont_be_executed():
    pass


@allure.story('epic_1')
def test_with_epic_1():
    pass


@allure.story('story_1')
def test_with_story_1():
    pass

@allure.story('story_2')
def test_with_story_2():
    pass


@allure.feature('feature_2')
@allure.story('story_2')
def test_with_story_2_and_feature_2():
    pass

# pytest tests.py --allure-stories story_1,story_2

# pytest tests.py --allure-features feature2 --allure-stories story2