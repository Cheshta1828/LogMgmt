from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
#from .task import add
import logging
def index(request):
 logger = logging.getLogger("loggers")
 logger = logging.getLogger("signal")  # Use the correct logger name

 message = {
  'message' : "user visits index()"
 }
 logger.info(message)
 return HttpResponse("hello")