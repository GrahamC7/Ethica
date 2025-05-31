import boto3
import json

def get_bedrock_client():
    # Create and return a Bedrock client.
    return boto3.client(
        service_name='bedrock-runtime',
        region_name='us-east-1',  # Change to your desired region as needed
    )

def generate_story_with_bedrock(prompt: str) -> str:
    # Generate a story using Amazon Bedrock's text generation capabilities.

    client = get_bedrock_client()

    body = json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": 500,
        "temperature": 0.7,
        "anthropic_version": "bedrock-2023-05-31",  # Specify the model version
    })

    response = client.invoke_model(
        modelId='anthropic.claude-2',  # Specify the model ID
        body=body,
    )

    return json.loads(response.get('body').read())['completion']