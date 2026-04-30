import unittest
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

if __name__ == "__main__":
    unittest.main()
