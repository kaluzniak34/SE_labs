from enum import Enum
from datetime import datetime

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
		raise NameError