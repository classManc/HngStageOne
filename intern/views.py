from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.utils import timezone
from datetime import timedelta

# Create your views here.

class InternDetails(APIView):
    def get(self,request):
        slack_name = request.query_params.get('slack_name', 'None')
        track = request.query_params.get('track','None')
        current_datetime_utc = timezone.now()
        current_day = current_datetime_utc.strftime('%A')
        current_utc_time = current_datetime_utc + timedelta(minutes=2)
        github_file_url = 'https://github.com/classManc/HngStageOne.git/intern/views.py'
        github_repo_url = 'https://github.com/classManc/HngStageOne.git'

        return Response({'slack_name':slack_name, 'track':track, 'current_day':current_day,
                         'utc_time':current_utc_time, 'github_file_url':github_file_url,
                         'github_repo_url':github_repo_url}, status= status.HTTP_200_OK)
