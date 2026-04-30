import unittest
from datetime import datetime, timedelta

from test import Task, TaskManager, validate_time

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
        time = "10:00.00 01/06/24"
        self.assertRaises(ValueError, validate_time, time)

    def test_invalid_date(self):
        time = "2024-13-58 10:00:00"
        self.assertRaises(ValueError, validate_time, time)

    def test_invalid_hour(self):
        time = "2024-10-10 40:00:00"
        self.assertRaises(ValueError, validate_time, time)

    def test_non_date_string(self):
        time = "agodfsdgfkhj9"
        self.assertRaises(ValueError, validate_time, time)

    def test_correct_date(self):
        time = "2024-06-01 10:00:00"
        self.assertEqual(validate_time(time), datetime(2024, 6, 1, 10, 0, 0))

if __name__ == "__main__":
    unittest.main()
