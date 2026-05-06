import boto3
import json

def stream_response(prompt):
    client = boto3.client('bedrock-runtime')
    response = client.invoke_model_with_response_stream(
        modelId='anthropic.claude-3-haiku-20240307-v1:0',
        body=json.dumps({"prompt": prompt, "max_tokens": 200})
    )
    
    for event in response.get('body'):
        chunk = json.loads(event.get('chunk').get('bytes').decode())
        yield chunk.get('completion')
