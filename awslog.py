"""This module can be used to get CloudWatch logs of Lambda functions."""

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_lambda_functions():
    try:
        lambda_client = boto3.client('lambda')
        functions = lambda_client.list_functions()
        lambda_names = [function['FunctionName'] for function in functions['Functions']]
        return lambda_names
    except (NoCredentialsError, PartialCredentialsError):
        print("AWS credentials not found. Please configure your AWS credentials.")
        return []
    except Exception as e:
        print(f"Error listing Lambda functions: {e}")
        return []

def list_log_streams(log_group_name):
    try:
        logs_client = boto3.client('logs')
        response = logs_client.describe_log_streams(logGroupName=log_group_name, orderBy='LastEventTime', descending=True)
        log_streams = [log_stream['logStreamName'] for log_stream in response['logStreams']]
        return log_streams
    except Exception as e:
        print(f"Error listing log streams: {e}")
        return []

def get_log_events(log_group_name, log_stream_name):
    try:
        logs_client = boto3.client('logs')
        next_token = None
        while True:
            kwargs = {
                'logGroupName': log_group_name,
                'logStreamName': log_stream_name
            }
            if next_token:
                kwargs['nextToken'] = next_token

            response = logs_client.get_log_events(**kwargs)
            events = response['events']
            if not events:
                print("No log events found.")
                return
            for event in events:
                print(event['message'])
            next_token = response.get('nextForwardToken')
            if not next_token or next_token == kwargs.get('nextToken'):
                break
    except Exception as e:
        print(f"Error getting log events: {e}")

def main():
    print("Listing all Lambda functions in the region...")
    lambda_functions = list_lambda_functions()
    
    if not lambda_functions:
        print("No Lambda functions found.")
        return

    for idx, function_name in enumerate(lambda_functions, start=1):
        print(f"{idx}. {function_name}")
    
    try:
        function_index = int(input("Enter the number of the Lambda function: ")) - 1
        if function_index < 0 or function_index >= len(lambda_functions):
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    selected_function_name = lambda_functions[function_index]
    log_group_name = f"/aws/lambda/{selected_function_name}"
    
    print(f"Listing log streams for Lambda function '{selected_function_name}'...")
    log_streams = list_log_streams(log_group_name)
    
    if not log_streams:
        print("No log streams found.")
        return
    
    for idx, log_stream_name in enumerate(log_streams, start=1):
        print(f"{idx}. {log_stream_name}")
    
    try:
        stream_index = int(input("Enter the number of the log stream: ")) - 1
        if stream_index < 0 or stream_index >= len(log_streams):
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    selected_log_stream_name = log_streams[stream_index]
    
    print(f"Getting log events for log stream '{selected_log_stream_name}'...")
    get_log_events(log_group_name, selected_log_stream_name)

if __name__ == "__main__":
    main()