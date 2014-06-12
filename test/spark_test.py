#!/usr/bin/env python

import time
import os

def work(x):
    start_time = time.time()
    time.sleep(x)
    end_time =  time.time()
    return {'id': os.getpid(), 'start': start_time, 'end_time': end_time}

import numpy as np

np.random.seed(1045)
job_times = np.random.uniform(0.4, 0.6, 24)

print 'Estimated serial time = {0:0.2f}'.format(job_times.sum())
print 'Amdahls parallel time = {0:0.2f}'.format(job_times.sum()/4.)

from pyspark import  SparkContext
sc = SparkContext( 'local[4]', 'pyspark')

jobs = sc.parallelize(job_times, 4)
print jobs.count()
results = jobs.map(work)
res = results.collect()
print res
