from django.test import TestCase
from django.urls import reverse
from .models import Job

class HomePageTest(TestCase):
    def test_homepage_status_code(self):
        """
        Test that the homepage loads successfully.
        """
        response = self.client.get(reverse("home"))  # assumes you named your URL 'home'
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        """
        Test that the homepage uses home.html template.
        """
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")


class JobModelTest(TestCase):
    def test_create_job(self):
        """
        Test that a Job object can be created and retrieved correctly.
        """
        job = Job.objects.create(
            title="Backend Developer",
            location="Remote",
            company="TechCorp",
            type="Full-time",
            description="Build APIs and services.",
            link="https://example.com/job/1"
        )

        # Fetch the job back
        saved_job = Job.objects.get(title="Backend Developer")
        self.assertEqual(saved_job.location, "Remote")
        self.assertEqual(str(saved_job), "Backend Developer - TechCorp")

