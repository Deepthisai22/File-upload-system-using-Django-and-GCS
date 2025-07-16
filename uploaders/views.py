from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from django.core.files.uploadedfile import InMemoryUploadedFile

# ✅ Create + List
class FileUploadView(APIView):
    def post(self, request):
        serializer = UploadedFileSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            instance = serializer.save()
            print("Storage backend:", instance.file.storage.__class__)

            # Make the uploaded file public (important!)
            # blob = instance.file.storage.bucket.blob(instance.file.name)
            # blob.make_public()
            # public_url = blob.public_url
            # file = instance.file
            print("📁 FILE PATH:", instance.file.name)  # This helps debug
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        files = UploadedFile.objects.all()
        serializer = UploadedFileSerializer(files, many=True)
        return Response(serializer.data)

# 🔍 Read one file
class FileDetailView(APIView):
    def get(self, request, file_id):
        file_obj = get_object_or_404(UploadedFile, id=file_id)
        serializer = UploadedFileSerializer(file_obj)
        return Response(serializer.data)

# ✏️ Update
class FileUpdateView(APIView):
    def put(self, request, file_id):
        file_obj = get_object_or_404(UploadedFile, id=file_id)
        serializer = UploadedFileSerializer(file_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

# 🗑️ Delete from GCS + DB
class FileDeleteView(APIView):
    def delete(self, request, file_id):
        file_obj = get_object_or_404(UploadedFile, id=file_id)
        # delete file from GCS
        file_obj.file.delete()
        # delete from database
        file_obj.delete()
        return Response({"status": "deleted"}, status=204)

# ⬇️ Download
class FileDownloadView(APIView):
    def get(self, request, file_id):
        file_obj = get_object_or_404(UploadedFile, id=file_id)
        return redirect(file_obj.file.url)