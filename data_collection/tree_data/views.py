from rest_framework.views import APIView, status
from rest_framework.response import Response



total_data={"webReq":0, "timeSpent":0, "country":{}} # because I am storing the tree in-memory


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

		return Response({"data":total_data})



class QueryData(APIView):
	def post(self, req):
		dim=req.data["dim"]
		dataKey=dim[0]["key"]

		output={"dim":dim}

		if dataKey=="country":
			if dim[0]["val"] in total_data["country"].keys():
				output.update({"metrics":[{"key":"webreq", "val":total_data["country"][dim[0]["val"]]["webReq"]},{"key":"timespent", "val":total_data["country"][dim[0]["val"]]["timeSpent"]}]})
			else:
				output.update({"metrics":[{"key":"webreq", "val":0},{"key":"timespent", "val":0}]})

		else:
			output.update({"msg":"Invalid query, kindly enter query for only countries"})

		return Response(output)