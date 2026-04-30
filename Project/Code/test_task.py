import unittest
from datetime import datetime, timedelta

from Project.Code.test import TaskManager, validate_time
from test import Task

class TestTask(unittest.TestCase):
    def test_task_initialization(self):
        name = "Sample Task"
        time = "2024-06-01 10:00:00"
        executable = "calc"
        task = Task(name, time, executable)
        self.assertEqual(task.name, name)
        self.assertEqual(task.time, time)
        self.assertEqual(task.executable, executable)
        self.assertFalse(task.completed)

    def test_is_due(self):
        past = datetime.now() - timedelta(seconds = 5)
        task = Task("name", past, "notepad")
        self.assertTrue(task.is_due())
        self.assertFalse(task.completed)

    def test_is_completed(self):
        task = Task("sample name", "2024-06-01 10:00:00", "calc")
        task.complete()
        self.assertTrue(task.completed)


class TestTaskManager(unittest.TestCase):

    def test_init_manager(self):

        task_list = [Task("sample name 2", "2024-06-01 10:00:00", "notepad")]
        manager = TaskManager(task_list)
        self.assertEqual(task_list, manager.tasks)

    def test_add_task(self):
        manager = TaskManager(tasks=[])
        manager.add_task(Task("sample name", "2024-06-01 10:00:00", "calc"))
        self.assertEqual(len(manager.tasks), 1)

class TestTime(unittest.TestCase):
    def test_invalid_format(self):
        task = Task("sample name", "10:00.00 01/06/24", "")
        self.assertFalse(validate_time(task))

    def test_invalid_date(self):
        task = Task("sample name", "2024-13-58 10:00:00", "")
        self.assertFalse(validate_time(task))

    def test_invalid_hour(self):
        task = Task("sample name", "2024-10-10 40:00:00", "")
        self.assertFalse(validate_time(task))

    def test_non_date_string(self):
        task = Task("sample name", "agodfsdgfkhj9", "")
        self.assertFalse(validate_time(task))

    def test_correct_date(self):
        task = Task("sample name", "2024-06-01 10:00:00", "calc")
        self.assertTrue(validate_time(task))

if __name__ == "__main__":
    unittest.main()
