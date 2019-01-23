# -*- coding: utf-8 -*-

from __future__ import absolute_import
from jiniapis.celery import app


@app.task
def world(num):
    for x in range(num):
        print("**************Do work out***************")
    return num


@app.task
def callable_task():
    for x in range(5):
        print("------------------spawn by user-------------------")