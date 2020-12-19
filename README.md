# data-collector

### 

- URL - http://localhost:8000/v1/insert

  - It is a POST Method.

  - Body Parameters

  - ```json
    {
    	"dim": [{
    		"key": "device",
    		"val": "mobile"
    },
    {
    	"key": "country",
    	"val": "IN"
    }],
    "metrics": [{
    	"key": "webreq",
    	"val": 70
    },
    {
    	"key": "timespent",
    	"val": 30
    }]
    }
    ```

  - Output

  - ```
    {
        "webReq": 70,
        "timeSpent": 30,
        "country": {
            "IN": {
                "webReq": 70,
                "timeSpent": 30,
                "device": {
                    "mobile": {
                        "webReq": 70,
                        "timeSpent": 30
                    }
                }
            }
        }
    }
    ```

    

  

- URL - http://localhost:8000/v1/query

  - It is a POST method.

  - Body Parameters:--

  - ```json
    {
    	"dim": [{
    		"key": "country",
    		"val": "IN"
    }]
    }
    
    ```

  - Output

  - ```
    {
        "dim": [
            {
                "key": "country",
                "val": "IN"
            }
        ],
        "metrics": [
            {
                "key": "webreq",
                "val": 70
            },
            {
                "key": "timespent",
                "val": 30
            }
        ]
    }
    ```

    

