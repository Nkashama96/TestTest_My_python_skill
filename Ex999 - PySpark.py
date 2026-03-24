from pyspark.sql import SparkSession

# 1. Initialize SparkSession with JDBC Driver
# Ensure the JDBC driver JAR is in the classpath
spark = SparkSession.builder \
    .appName("PySpark JDBC Example") \
    .config("spark.jars", "/path/to/postgresql-42.x.x.jar") \
    .getOrCreate()

# 2. Define JDBC Connection Properties
url = "jdbc:postgresql://localhost:5432/mydatabase"
properties = {
    "user": "username",
    "password": "password",
    "driver": "org.postgresql.Driver"
}

# 3. Read Data from Database
df = spark.read.jdbc(url=url, table="source_table", properties=properties)
df.show()

# 4. Transform Data (Optional)
processed_df = df.filter(df["age"] > 21)

# 5. Write Data back to Database (Commit)
# Mode "append" or "overwrite" commits data immediately in JDBC
processed_df.write.jdbc(
    url=url,
    table="target_table",
    mode="append",
    properties=properties
)

print("Data written and committed successfully.")

# 6. Close Session
spark.stop()
