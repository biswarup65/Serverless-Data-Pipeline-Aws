import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1776601119992 = glueContext.create_dynamic_frame.from_catalog(database="csv-glue-catalog-db", table_name="spend_analysis_dataset_csv", transformation_ctx="AWSGlueDataCatalog_node1776601119992")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1776599364268 = glueContext.create_dynamic_frame.from_catalog(database="csv-glue-catalog-db", table_name="ecommerce_sales_data_csv", transformation_ctx="AWSGlueDataCatalog_node1776599364268")

# Script generated for node Change Schema
ChangeSchema_node1776601143308 = ApplyMapping.apply(frame=AWSGlueDataCatalog_node1776601119992, mappings=[("transactionid", "string", "transactionid", "string"), ("itemname", "string", "itemname", "string"), ("category", "string", "category", "string"), ("quantity", "long", "quantity", "long"), ("unitprice", "double", "unitprice", "double"), ("totalcost", "double", "totalcost", "double"), ("purchasedate", "string", "purchasedate", "string"), ("supplier", "string", "supplier", "string")], transformation_ctx="ChangeSchema_node1776601143308")

# Script generated for node Change Schema
ChangeSchema_node1776599503294 = ApplyMapping.apply(frame=AWSGlueDataCatalog_node1776599364268, mappings=[("order date", "string", "order date", "string"), ("product name", "string", "product name", "string"), ("category", "string", "category", "string"), ("region", "string", "region_area", "string"), ("quantity", "long", "quantity", "long"), ("sales", "long", "sales", "long"), ("profit", "double", "total_profit", "double")], transformation_ctx="ChangeSchema_node1776599503294")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=ChangeSchema_node1776601143308, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1776600074513", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1776601198750 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1776601143308, connection_type="s3", format="csv", connection_options={"path": "s3://csv-final-data-2026", "compression": "gzip", "partitionKeys": []}, transformation_ctx="AmazonS3_node1776601198750")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=ChangeSchema_node1776599503294, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1776599071936", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1776599674795 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1776599503294, connection_type="s3", format="csv", connection_options={"path": "s3://csv-final-data-2026", "compression": "gzip", "partitionKeys": []}, transformation_ctx="AmazonS3_node1776599674795")

job.commit()