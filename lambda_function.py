# -*- coding: utf-8 -*-
import slackpy
import os
import json

INCOMING_WEB_HOOK = os.environ['INCOMING_WEB_HOOK']
logger = slackpy.SlackLogger(INCOMING_WEB_HOOK)
logger.set_log_level(slackpy.LogLv.DEBUG)

def lambda_handler(event, context):
    cloudwatch_event = json.dumps(event)
    logger.info(
        title=cloudwatch_event['detail-type'],
        message="",
        fields=cloudwatch_event['detail']
    )
