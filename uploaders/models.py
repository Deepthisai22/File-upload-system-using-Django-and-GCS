from django.db import models
from storages.backends.gcloud import GoogleCloudStorage

# Create a storage instance
gcs_storage = GoogleCloudStorage()

class UploadedFile(models.Model):
    file = models.FileField(storage=gcs_storage, upload_to='uploads/')  # ✅ GCS enforced here
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
