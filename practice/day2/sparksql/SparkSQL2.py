from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("SQL2").master("local[2]").getOrCreate()

    df = spark.read.format("csv").option("header","true").option("inferSchema","true").load("C:/Users/91782/Desktop/Projects/pyspark/pyspark/practice/day2/data/sample.csv")

    df.createOrReplaceTempView("vw_sample")

    df1 = spark.sql("Select * from vw_sample where Age> 40 and treatment='Yes' ")
    # df1.show()

    df2 = df.select("*").where("Age>40 and treatment='Yes' ")
    #df2.show()

    df3 = df.groupBy("country").count()
    df3.show()


