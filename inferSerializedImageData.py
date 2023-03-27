import json
import base64
import boto3

ENDPOINT = 'image-classification-2023-02-04-21-53-36-205'

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['image_data'])

    runtime= boto3.client('runtime.sagemaker')

    inferences = runtime.invoke_endpoint(EndpointName=ENDPOINT,
                                ContentType='image/png',
                                       Body=image)

    # We return the data back to the Step Function    
    event["inferences"] = inferences['Body'].read().decode('utf-8')
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }



 