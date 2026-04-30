import unittest
from datetime import datetime, timedelta

from Project.Code.test import TaskManager
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

if __name__ == "__main__":
    unittest.main()
