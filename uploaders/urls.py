from django.urls import path
from .views import (
    FileUploadView, FileDetailView, FileUpdateView,
    FileDeleteView, FileDownloadView
)

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),         # POST + GET (all)
    path('files/<int:file_id>/', FileDetailView.as_view(), name='file'),   # GET one
    path('files/<int:file_id>/update/', FileUpdateView.as_view(), name='file-update'),  # PUT
    path('files/<int:file_id>/delete/', FileDeleteView.as_view(), name='file-delete'),  # DELETE
    path('download/<int:file_id>/', FileDownloadView.as_view(), name='file-download'),  # GET (download)
]

