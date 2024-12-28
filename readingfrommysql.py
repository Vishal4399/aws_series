#Reading the data from mysql processing using spark and stroing again in the mysql db table.
from pyspark.sql.functions import *
host = "jdbc:mysql://mysql.cfu24co4gmoo.ap-south-1.rds.amazonaws.com:3306/mysql"
df = spark.read.format("jdbc").option("url", host).option("header", "true").option("inferSchema", "true")\
.option("dbtable", "SampleDB.emp").option("user", "myuser").option("password", "mypassword!11")\
.option("driver", "com.mysql.cj.jdbc.Driver").load()

ndf = df.withColumn("date", current_date()) \
        .withColumn("hiredate", date_format(col("hiredate"), "yyyy-MM-dd")) \
        .withColumn("date", date_format(col("date"), "yyyy-MM-dd")) \
        .withColumn("date", to_date(col("date"), "yyyy-MM-dd")) \
        .withColumn("hiredate", to_date(col("hiredate"), "yyyy-MM-dd")) \
        .withColumn("diff", datediff(col("date"), col("hiredate"))/365).drop(col("date"))

ndf.write.format("jdbc").option("url", host).option("user", "myuser").option("password", "mypasdsacword!11")\
    .option("dbtable", "SampleDB.new_emp").option("driver", "com.mysql.cj.jdbc.Driver").save()
