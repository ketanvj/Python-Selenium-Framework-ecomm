import allure
import pytest
# Allure tracks invocations of every fixture and shows in full details
# what methods with what arguments were invoked,
# preserving the correct sequence of the calls that were made.
# You don’t need to mark your fixtures to make them visible in the report,
# they will be detected automatically for different scopes

@pytest.fixture(params=[True, False], ids=['param_true', 'param_false'])
def function_scope_fixture_with_finalizer(request):
    if request.param:
        print('True')
    else:
        print('False')
    def function_scope_finalizer():
        #function_scope_step()
        pass
    request.addfinalizer(function_scope_finalizer)


@pytest.fixture(scope='class')
def class_scope_fixture_with_finalizer(request):
    def class_finalizer_fixture():
        #class_scope_step()
        pass
    request.addfinalizer(class_finalizer_fixture)


@pytest.fixture(scope='module')
def module_scope_fixture_with_finalizer(request):
    def module_finalizer_fixture():
        #module_scope_step()
        pass
    request.addfinalizer(module_finalizer_fixture)


@pytest.fixture(scope='session')
def session_scope_fixture_with_finalizer(request):
    def session_finalizer_fixture():
        #session_scope_step()
        pass
    request.addfinalizer(session_finalizer_fixture)


class TestClass(object):

    def test_with_scoped_finalizers(self,
                                    function_scope_fixture_with_finalizer,
                                    class_scope_fixture_with_finalizer,
                                    module_scope_fixture_with_finalizer,
                                    session_scope_fixture_with_finalizer):
        #step_inside_test_body()
        self.test_step_1();
        self.test_step_2();

    @allure.step
    def test_step_1(self):
        pass

    @allure.step
    def test_step_2(self):
        pass

