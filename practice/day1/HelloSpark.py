from pyspark.sql import SparkSession 
import shutil 
import os



temp_dir = "C:/Users/91782/Desktop/Projects/pyspark/sparktemp"

if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

spark = SparkSession.builder\
    .appName("Hello Spark")\
    .config("spark.local.dir",temp_dir)\
    .getOrCreate()

print("Spack Connection is successful!")

spark.stop()