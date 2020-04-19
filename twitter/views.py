from django.shortcuts import render

from django.http import JsonResponse
from twitter.models import Tweet
from django.core import serializers

import datetime

def get_tweets(request):
    tweets = Tweet.objects.all()
    data = list(tweets.values())
    return JsonResponse(data, safe=False)
