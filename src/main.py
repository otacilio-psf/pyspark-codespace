from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Read Az Blob Storage > Write as Delta").getOrCreate()
spark.sparkContext.setLogLevel('WARN')


# Azure storage access info
blob_account_name = "azureopendatastorage"
blob_container_name = "nyctlc"
blob_relative_path = "yellow"
blob_sas_token = "r"

# Allow SPARK to read from Blob remotely
wasbs_path = f'wasbs://{blob_container_name}@{blob_account_name}.blob.core.windows.net/{blob_relative_path}'

spark.conf.set(
    f'fs.azure.sas.{blob_container_name}.{blob_account_name}.blob.core.windows.net',
    blob_sas_token
)

print('Remote blob path: ' + wasbs_path)

# SPARK read parquet, note that it won't load any data yet by now
df = spark.read.parquet(wasbs_path)

df = df.filter("puYear = 2019")

print('Register the DataFrame as a SQL temporary view: source')
df.createOrReplaceTempView('source')

# Display top 10 rows
print('Displaying top 10 rows: ')
#spark.sql('SELECT * FROM source LIMIT 10').show()

# Write as delta
print('Write to delta')
df.write.format('delta').mode('overwrite').save('data/nyc-yellow-taxi')

spark.stop()