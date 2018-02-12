import os, boto3
from urllib2 import Request, urlopen, URLError
from time import sleep
import urllib, ssl, json, logging,cfn_resource

handler = cfn_resource.Resource()

@handler.create
def test(event,context):
    logging.basicConfig(filename="./aviatrix.log",level="INFO")
    #logging configuration
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logging.info('EventData:' + str(event))
    logger.info("EventData:" + str(event))

    return {
        "PhysicalResourceId": "arn:aws:fake:myID"
    }
