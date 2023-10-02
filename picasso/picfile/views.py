from rest_framework import viewsets
# from rest_framework import status
# from rest_framework.parsers import FormParser, MultiPartParser
# from rest_framework.response import Response
# from rest_framework.views import APIView
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import upload


from .models import File

from .serializers import FileSerializer


def async_job(request):
    local_path = 'F://Dev/Picasso/picasso/picfile/sample.mp4'
    path = 'celery-videos/sample.mp4'

    upload.apply_async(args=[local_path, path], ignore_result=True)

    return HttpResponse('Start uploading...')


# def file_list(request):
#     files = File.objects.all().order_by("-id")
#     return render(request, 'file_upload/file_list.html', {'files': files})
#
#
# # Regular file upload without using ModelForm
# def file_upload(request):
#     if request.method == "POST":
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             # get cleaned data
#             upload_method = form.cleaned_data.get("upload_method")
#             raw_file = form.cleaned_data.get("file")
#             new_file = File()
#             new_file.file = handle_uploaded_file(raw_file)
#             new_file.upload_method = upload_method
#             new_file.save()
#             return redirect("/file/")
#     else:
#         form = FileUploadForm()
#
#     return render(request, 'file_upload/upload_form.html', {'form': form,
#                                                             'heading': 'Upload files with Regular Form'})
#

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class UploadViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer