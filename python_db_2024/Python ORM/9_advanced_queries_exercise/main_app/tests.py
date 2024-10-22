from datetime import date

from django.test import TestCase

from main_app.models import Task


class TaskModelTestCase(TestCase):
    def setUp(self):
        # Create task instances with custom creation dates
        self.zero_task = Task.objects.create(
            title="Task 1",
            description="Description for Task 1",
            priority="High",
            creation_date=date(2023, 1, 15),
            completion_date=date(2023, 1, 25)
        )

    def test_zero_ongoing_high_priority_tasks(self):
        """
        Zero test the `ongoing_high_priority_tasks` method.

        Checks if ongoing tasks with high priority are correctly filtered.
        """
        ongoing_tasks = Task.ongoing_high_priority_tasks()
        self.assertIn(self.zero_task, ongoing_tasks)
        self.assertEqual(ongoing_tasks.count(), 1)