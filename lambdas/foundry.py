import json
import logging

from boto3.session import Session
from time import sleep

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
region_name = 'us-east-1'
instance_id = 'i-0b77ab0785378a0eb'


def turn_on_foundry(region=region_name):
    session = Session()
    client = session.client(service_name='ec2', region_name=region)
    logger.info(f'Starting the Foundry Instance {instance_id}.')
    client.start_instances(InstanceIds=[instance_id])


def turn_off_foundry(region=region_name):
    session = Session()
    client = session.client(service_name='ec2', region_name=region)
    logger.info(f'Stopping the Foundry instance {instance_id}.')
    client.stop_instances(InstanceIds=[instance_id])


def get_foundry_status(region=region_name):
    session = Session()
    client = session.client(service_name='ec2', region_name=region)

    status_response_dict = client.describe_instance_status(
        InstanceIds=[
            instance_id,
        ],
        IncludeAllInstances=True,
    )
    logger.debug(f'Foundry Status: {json.dumps(status_response_dict)}')
    instance_responses = status_response_dict.get('InstanceStatuses')
    if len(instance_responses) > 0:
        instance_status = instance_responses[0].get(
            'InstanceState',
        ).get('Name')
    else:
        instance_status = 'Instance does not exist - inform @lowerlight'
    return instance_status
