from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession.builder.appName("Spark SQL").master("local[2]").getOrCreate()

    df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("C:/Users/91782/Desktop/Projects/pyspark/pyspark/practice/day2/data/sample.csv")

    df.createOrReplaceTempView("tbl_sample")

    countDf = spark.sql("select * from tbl_sample")

    countDf.show()



