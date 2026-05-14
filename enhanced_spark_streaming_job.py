from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("EcommerceStreamingAnalytics") \
    .getOrCreate()

# =========================
# STREAMING SCHEMA
# =========================

schema = StructType([
    StructField("order_id", IntegerType()),
    StructField("product_id", IntegerType()),
    StructField("quantity", IntegerType()),
    StructField("price", DoubleType())
])

# =========================
# READ STREAM FROM KAFKA
# =========================

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "ecommerce-orders") \
    .load()

parsed = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

parsed = parsed.withColumn(
    "event_time",
    current_timestamp()
)

# =========================
# STATIC PRODUCT DATASET
# =========================

products_df = spark.read.csv(
    "product_catalog.csv",
    header=True,
    inferSchema=True
)

# =========================
# REGISTER TEMP VIEWS
# =========================

parsed.createOrReplaceTempView("orders_stream")
products_df.createOrReplaceTempView("products")

# =========================
# SPARK SQL JOIN
# =========================

joined_df = spark.sql("""
SELECT
    o.order_id,
    o.product_id,
    p.product_name,
    p.category,
    p.brand,
    o.quantity,
    o.price,
    (o.quantity * o.price) AS total_amount,
    o.event_time
FROM orders_stream o
LEFT JOIN products p
ON o.product_id = p.product_id
""")

# =========================
# WRITE STREAM
# =========================

query = joined_df.writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", "hive_output") \
    .option("checkpointLocation", "checkpoint_hive") \
    .start()

query.awaitTermination()