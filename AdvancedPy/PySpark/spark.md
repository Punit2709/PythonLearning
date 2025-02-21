# Spark Learning 

### Spark Session
A SparkSession is the entry point to using Apache Spark in Databricks or any other Spark environment. It provides a single point of access to Spark's functionalities, including reading data, running queries, and managing configurations.

```from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MySparkApp") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

```