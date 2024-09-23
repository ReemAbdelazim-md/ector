from pyspark.sql import SparkSession
from config.config import Config

class IgraineIngestor:
    """
    Handles data ingestion from the Igraine Gold layer into the Ector pipeline.
    This script pulls data based on the region and labels (surgeon, patient).
    """

    def __init__(self):
        # Initialize a Spark session (works well in Databricks environment)
        self.spark = SparkSession.builder.appName("IgraineDataIngestion").getOrCreate()

    def ingest_data(self, region_codes):
        """
        Ingests data from the specified regions in the Igraine Gold layer.

        Args:
            region_codes (list): List of short codes of regions (e.g., ['ae', 'ca', 'qa', 'sa']).

        Returns:
            dict: Dictionary with DataFrames labeled as 'surgeon' or 'patient' based on Config for each region.
        """
        # Initialize a dictionary to store ingested data for all regions
        ingested_data = {
            "surgeon": [],
            "patient": []
        }

        # Loop through the provided region codes
        for region_code in region_codes:
            # Validate region code and get corresponding schema
            region_schema = Config.REGIONS.get(region_code)
            if not region_schema:
                raise ValueError(f"Invalid region code: {region_code}")

            # Get the tables for the region from the DB_CATALOG in Config
            tables = Config.DB_CATALOG.get(region_schema)
            if not tables:
                raise ValueError(f"No tables found for region: {region_code}")

            # Loop through tables and ingest data
            for table, labels in tables.items():
                # Read table data into a Spark DataFrame
                df = self.spark.read.table(f"{Config.CATALOG_MASTER}.{region_schema}.{table}")

                # For each label (e.g., 'surgeon', 'patient'), store the DataFrame in the corresponding list
                for label in labels:
                    ingested_data[label].append(df)

        return ingested_data

# Example usage (if needed for testing)
# if __name__ == "__main__":
#     region_codes = ['ae', 'ca', 'qa', 'sa']  # Example region codes
#     ingestor = IgraineIngestor()
#     data = ingestor.ingest_data(region_codes)
