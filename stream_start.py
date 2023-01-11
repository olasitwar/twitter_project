import os
from credentials import *
os.environ["JAVA_HOME"] = JAVA_HOME_USER
os.environ["SPARK_HOME"] = SPARK_HOME_USER
os.environ["PATH"] = PATH_USER

import findspark
findspark.init(FINDSPARK_PATH)
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import desc
from collections import namedtuple

if __name__ == '__main__':
 sc = SparkContext()

 ssc = StreamingContext(sc, 10)
 sqlContext = SQLContext(sc)

 socket_stream = ssc.socketTextStream("127.0.0.1", 5555)

 lines = socket_stream.window(20)

 fields = ("tag", "count")
 Tweet = namedtuple('Tweet', fields)

 (lines.flatMap(lambda text: text.split(" "))  # Splits to a list
  .filter(lambda word: word.lower().startswith("#"))  # Checks for hashtag calls
  .map(lambda word: (word.lower(), 1))  # Lower cases the word
  .reduceByKey(lambda a, b: a + b)  # Reduces
  .map(lambda rec: Tweet(rec[0], rec[1]))  # Stores in a Tweet Object
  .foreachRDD(lambda rdd: rdd.toDF().sort(desc("count"))  # Sorts Them in a DF
  .limit(10).registerTempTable("tweets")))  # Registers to a table.

 print("START STREAMING...")
 ssc.start()


