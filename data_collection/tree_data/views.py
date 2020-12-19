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


total_data={"webReq":0, "timeSpent":0, "country":{}}


class InsertData(APIView):
	def post(self, req):
		dim=req.data["dim"]
		metrics = req.data["metrics"]
		dvc={}
		cntry=""
		for data in dim:
			if data["key"]=="device":
				dvc.update({"device":data["val"], "webReq":0, "timeSpent":0})
			elif data["key"]=="country":
				cntry=data["val"]
		for data in metrics:
			if data["key"]=="webreq":
				dvc.update({"webReq":data["val"]})
			elif data["key"]=="timespent":
				dvc.update({"timeSpent":data["val"]})
		
		total_data["webReq"]+=dvc["webReq"]
		total_data["timeSpent"]+=dvc["timeSpent"]
		if cntry in total_data["country"].keys():
			total_data["country"][cntry]["webReq"]+=dvc["webReq"]
			total_data["country"][cntry]["timeSpent"]+=dvc["timeSpent"]
			if dvc["device"] in total_data["country"][cntry]["device"]:
				total_data["country"][cntry]["device"][dvc["device"]]["webReq"]+=dvc["webReq"]
				total_data["country"][cntry]["device"][dvc["device"]]["timeSpent"]+=dvc["timeSpent"]
			else:
				total_data["country"][cntry]["device"].update({dvc["device"]:{"webReq":dvc["webReq"], "timeSpent":dvc["timeSpent"]}})

		else:
			total_data["country"].update({cntry:{"webReq":dvc["webReq"], "timeSpent":dvc["timeSpent"], "device":{dvc["device"]:{"webReq":dvc["webReq"], "timeSpent":dvc["timeSpent"]}}}})

		print("yes")
		return Response({"data":total_data})
        