#!/usr/bin/env python
#
# Copyright (C) 2019 Xiaoyu Wang <xwang224@buffalo.edu>
#
# This file is part of Running on the Queue Job Manager
#
#            < jobqueue.py >
# Class to manage the jobs on the cluster
#

import os
from queue import Queue
import subprocess
import sys
from threading import Thread

class Job(object):

    def __init__(self, path):
        self.path = path
        self.status = 0
        self.jobID = 0
        self.host = None

    def ssh(self, command):
        ssh = subprocess.Popen(
            ["ssh", "%s" % self.host, command],
        shell = False,


class JobQueue(object):

    def __init__(self):
        self.queue = Queue()


    def check_updates(self):
        pass
