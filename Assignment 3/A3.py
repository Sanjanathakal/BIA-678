from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import IntegerType,FloatType

def calculate_total(row_dict):
    tmp_val = float(row_dict['ANNUAL\xa0'])
    cities = int(row_dict['# CITIES\xa0'])
    return (row_dict['Alberta'],(tmp_val*cities,cities))

def calculate_total_temp_cities(row1,row2):
    return(row1[0]+row2[0],row1[1]+row2[1] )

def temp_calc(row):
    return(row[0],row[1][0]/row[1][1])

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)
df = sqlContext.read.format('csv').options(header=True).load('data.csv')
data_df = data_df.dropna()

avg_tmp = data_df.filter(data_df['Alberta'] == 'Average Temperature (F)').rdd.map(lambda row: row.asDict())
avg_high = data_df.filter(data_df['Alberta'] == 'Average High Temperature (F)').rdd.map(lambda row: row.asDict())
avg_low = data_df.filter(data_df['Alberta'] == 'Average Low Temperature (F)').rdd.map(lambda row: row.asDict())
avg_pcp = data_df.filter(data_df['Alberta'] == 'Average Precipitation (in)').rdd.map(lambda row: row.asDict())

avg_tmp = avg_tmp.map(calculate_total)
avg_tmp =avg_tmp.reduceByKey(calculate_total_temp_cities)
avg_tmp = avg_tmp.map(temp_calc)
avg_tmp.collect()

avg_high = avg_high.map(calculate_total)
avg_high =avg_high.reduceByKey(calculate_total_temp_cities)
avg_high = avg_high.map(temp_calc)
avg_high.collect()

avg_low = avg_low.map(calculate_total)
avg_low =avg_low.reduceByKey(calculate_total_temp_cities)
avg_low = avg_low.map(temp_calc)
avg_low.collect()

avg_pcp = avg_pcp.map(calculate_total)
avg_pcp =avg_pcp.reduceByKey(calculate_total_temp_cities)
avg_pcp = avg_pcp.map(temp_calc)
avg_pcp.collect()

