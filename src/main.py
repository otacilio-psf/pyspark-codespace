from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Sample App").getOrCreate()

qtd = spark.range(1000).count()

print(qtd)

spark.stop()