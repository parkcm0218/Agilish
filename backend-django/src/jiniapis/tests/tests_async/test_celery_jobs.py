#_*_coding: utf-8 _*_

from jiniapis.tasks import world
from jiniapis.tests.base import JiniapisBaseTest


class TestCeleryTasks(JiniapisBaseTest):

    # success smoke test 
    # def test_smoke_test(self):

    #     assert 1 is not 1, "Should be equal"

    def test_celery_tasks_module_level_test(self):
        res= world.delay(1000)

        # check return value with .get() function
        assert res.get() == 1000
        assert res.successful() == True
