from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

conf = SparkConf()

conf.setAppName("Spark Config App")
conf.setMaster("loca[*]")

# connect to spark cluster
#  conf.setMaster("spark://master:7077)

#memory settings
conf.set("spark.executor.memory","2g")
conf.set("spark.driver.memory","1g")

#core settings
conf.set("spark.executor.cores","4")
conf.set("spark.driver.cores","2")

conf.set("spark.sql.shuffle.partitions", "200")
conf.set("spark.default.parallelism", "100")

sc = SparkContext(conf=conf)

#or with SparkSession

sc = SparkSession.builder.conf(conf=conf).getOrCreate()

#accessing SparkConf Parameters

app_name = conf.get("spark.app.name")
print("{app_name}")