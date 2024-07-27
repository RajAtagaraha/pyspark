from pyspark import SparkContext, SparkConf

confg = SparkConf().setAppName("rdd programs").setMaster("local[2]")

sc = SparkContext(conf=confg)

data = [1,2,3,4,5]

distData = sc.parallelize(data)

number = distData.count()

newData = distData.map(lambda x: x*2)

doubleData = newData.collect() # will collect all rdd from all partitions

filterData = newData.filter(lambda x: x!=2).collect()


print(doubleData)
print(number)
print(filterData)
#or break into number of partitions

# distData = sc.parallelize(data,5)

#distFile = sc.textFile("")