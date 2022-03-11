import allure
import pytest


# Reports can display many different types of provided attachments that can complement
# a test, step or fixture result.
# Attachments can be created either with invocation of
# allure.attach(body, name, attachment_type, extension):
#
# body - raw content to be written into the file.
#
# name - a string with name of the file
#
# attachment_type - one of the allure.attachment_type values
#
# extension - is provided will be used as an extension for the created file.
#
# or allure.attach.file(source, name, attachment_type, extension):
#
# source - a string containing path to the file.

@pytest.fixture
def attach_file_in_module_scope_fixture_with_finalizer(request):
    allure.attach('A text attacment in module scope fixture', 'blah blah blah', allure.attachment_type.TEXT)
    def finalizer_module_scope_fixture():
        allure.attach('A text attacment in module scope finalizer', 'blah blah blah blah',
                      allure.attachment_type.TEXT)
    request.addfinalizer(finalizer_module_scope_fixture)


def test_with_attacments_in_fixture_and_finalizer(attach_file_in_module_scope_fixture_with_finalizer):
    pass


def test_multiple_attachments():
    allure.attach.file('data/selenium.png', attachment_type=allure.attachment_type.PNG)
    allure.attach('<head></head><body> <h1>Selenium with Python</h1><h2> Learning Allure </h2> </body>', 'Attach with HTML type', allure.attachment_type.HTML)
