from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.db import connection
import json
from collections import OrderedDict



class Country:

	def __init__(self, name, webReq=0, timeSpent=0):
		self.name=name
		self.webReq=webReq
		self.timeSpent=timeSpent

class Device:
	def __init__(self, name, webReq=0, timeSpent=0):
		self.name=name
		self.webReq=webReq
		self.timeSpent=timeSpent 


total_data={}


class InsertData(APIView):
    def post(self, req):
    	dim=req.data["dim"]
    	metrics=req.data["metrics"]
    	return Response({"data":req.data})
        