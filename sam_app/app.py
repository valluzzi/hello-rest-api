import json

# import requests


def lambda_handler(event, context):
    
    print("Received event: " + json.dumps(event, indent=2))

    method = event['httpMethod'] if 'httpMethod' in event else '???'
    print("Method: " + method.upper())
    print("=====================================")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"{method} call received!",
        }),
    }
