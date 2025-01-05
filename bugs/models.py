import uuid
from django.db import models
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    if not value.name.lower().endswith(('.jpg', '.jpeg', '.png')):
        raise ValidationError("Only .jpg, .jpeg, and .png files are allowed.")

class Project(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, db_index=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Bug(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    id = models.UUIDField(primary_key=True, editable=False, unique=True, db_index=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BugScreenshot(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, db_index=True, default=uuid.uuid4)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE, related_name="screenshots")
    image = models.ImageField(upload_to="bug_screenshots/", validators=[validate_file_extension])

    def __str__(self):
        return f"Screenshot for {self.bug.title}"

