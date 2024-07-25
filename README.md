# pyspark

1. What is Apache Spark?
   Apache spark is a real time analytical processing framework, it was developed to overcome MapReduce challenges like slow processing and was only batch processing. It is lightning fast , can do stream processing as well as batch processing. Unline MapReduce , spark can perform in memory operation to analyze data.
   Spark has its own cluster manager as well as it can run in Yarn. It leverages HDFS for storage.
   Spark is written in scala programming language.

   PySpark, users can unlock unparalleled scalability, faster processing times, and enhanced performance, making it an indispensable tool for modern data-driven applications.
   Spark is 100 times faster than traditional approach.
   Efficient processing of large dataset.

2. What are supported languages for Spark?
   Scala, Java, Python , R

3. What is Py4j?
   Py4j is a python library that enables python to run spark programming

4. What is the latest verion of spark?
   It may very time to time, as of 2024 July, latest release version is 3.5.1

5. What are basic environment setup required to run Pyspark?

   1. Minimum Java 8 is required
   2. Python
   3. Py4j library
   4. And following environment configuration is required :
      SPARK_HOME = /home/hadoop/spark-x.y.z-bin-hadoopX.Y
      PATH = $PATH:/home/hadoop/spark-x.y.z-bin-hadoopX.Y/bin
      PYTHONPATH = $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.x.y-src.zip:$PYTHONPATH
      PATH = $SPARK_HOME/python:$PATH

6. Why PySpark dataframe and not Python Pandas?
   In case if we are working on sinlge node in that case there are not much of a difference. But in a multicluster environment pyspark can speed up the processing by distributed computing unline python pandas which do not support distributed processing.

7. What is PySpark?
   PySpark is Python API for spark libraries.

8. Why is Spark faster than MapReduce?
   Spark does in memory processing unlike MapReduce. Spark can reuse the in-memroy cache data for processing, this lowers the latency and hence performs faster than MapReduce.

9. What type of streaming is supported by Spark?

   1. Batch Streaming and 2. Real time Streaming

10. What version of Python does PySpark support?
    PySpark 3.5 supports python 3.8.

11. What are main feautres of pyspark?
    There are 9 features :
    a) inmemory computation b) Lazy Evaluation c) inbuild optimization d) cache & persistence e) immmutable
    f) ANSI SQL Support g)Fault Tolerant h) Supports YARN, Mesos Cluster, Kubernetes i) distributed processing

12. Fault Tolerance:
    Spark handles fault tolerance by maintaining RDD ( resilient distributed dataset) , which allows it to recover from failures gracefully.

13. Lazy Evolution:
    Spark does not compute until an action is triggered. Spark stores the operation in DAG ( Directed Acyclic Graph)

14. What are the advantages of PySpark?
    a) Scalable b) Performance c) Easy of use d) Fault Tolerant e) Unified platform g) Real-time processing
    h) Machine learning capabilities i) Community and ecosystem

15.
