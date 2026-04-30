from enum import Enum
from datetime import datetime
import os

def validate_time(task):
	return datetime.strptime(task.time, "%Y-%m-%d %H:%M:%S")

class Task:
	def __init__(self, name, time, executable):
		self.name = name
		self.time = time
		self.executable = executable
		self.completed = False

	def __repr__(self):
		return f"Task(name={self.name!r}, time={self.time!r}, executable={self.executable!r}, completed={self.completed!r})"

	def is_due(self):
		now = datetime.now()
		return now >= self.time

	def complete(self):
		os.system(self.executable)
		self.completed = True

class TaskManager:
	def __init__(self, tasks):
		self.tasks = tasks

	def add_task(self, task):
		self.tasks.append(task)