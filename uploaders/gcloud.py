from storages.backends.gcloud import GoogleCloudStorage
import os
from google.oauth2 import service_account

class GCSMediaStorage(GoogleCloudStorage):
    location = ''
    default_acl = 'publicRead'
    credentials = service_account.Credentials.from_service_account_file(
        os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    )

