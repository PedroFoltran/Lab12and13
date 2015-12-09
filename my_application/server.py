import urllib2
import boto
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import os
import json
from subprocess import Popen, PIPE
from flask import Flask, Response, render_template , request, redirect, url_for
from werkzeug import secure_filename
from tempfile import mkdtemp

app = Flask(__name__)

def get_conn():
	key_id,secret_access_key = urllib2.urlopen("http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key").read().slip(':')
        return boto.sqs.connect_to_region("eu-west-1",aws_access_key_id=key_id,aws_secret_access_key=secret_access_key)

@app.route("/", methods=["GET"])
def index():
        return Response(response=json.dumps(boto.Version), mimetype="application/json")



@app.route("/queues", methods=["GET"])
def list_queues():
  all = []
  conn = get_conn()
  for q in conn.get_all_queues():
      all.append(q.name)
      resp = json.dumps(all)
	return Response(response=json.dumps(resp), mimetype="application/json")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
