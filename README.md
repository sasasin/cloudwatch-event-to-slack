# cloudwatch-events-to-slack

Any Event -> CloudWatch Event -> Lambda -> Slack

のLambdaファンクションのソースコードです。

# create lambda function by python 3.7

てきとーにLambdaファンクションを作成する。Python 3.7で作る。

環境変数 `INCOMING_WEB_HOOK` にSlack Incoming Webhook URL を設定しておく。

# build source zip file

```
$ git clone git@github.com:sasasin/cloudwatch-events-to-slack.git
$ cd cloudwatch-events-to-slack
$ ./build.sh
```

build.sh でカレントディレクトリに作成された src.zip を、Lambdaファンクションの管理ページでアップロードする。

# configure lambda event source

CloudWatch Eventsの通知先を、Lambdaファンクションに設定する。

# 参考

* https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
* https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html
* https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html
* https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/EventTypes.html
* https://github.com/iktakahiro/slackpy
