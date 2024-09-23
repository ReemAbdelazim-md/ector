class Config:

    """
    Config class for Ector data pipeline. This class contains:
    - Predefined regions and their corresponding schemas.
    - Database catalog for tables and their workflows (surgeon, patient).
    - Workflow filtering based on region and dynamic workflows (e.g., surgeon, patient).
    """


    # Reference to master db that contains schemas and tables
    CATALOG_MASTER = "hive_metastore"

    # Predefined Regions
    REGIONS = {
        "ae": "ae_cosmos_origin_s1",
        "ca": "ca_cosmos_origin_s1",
        "qa": "qa_cosmos_origin_s1",
        "sa": "sa_ca_cosmos_origin_s1"
    }
    # Database Catalog (schemas, tables, and subjects by region)
    DB_CATALOG = {
        REGIONS["ae"]: {
            "calibration_monitoring": ["surgeon", "patient"],  # Used for both surgeon and patient
            "measurement_processed": ["surgeon", "patient"]   
        },
        REGIONS["ca"]: {
            "calibration_monitoring": ["surgeon", "patient"],
            "measurement_processed": ["surgeon", "patient"]
        },
        REGIONS["qa"]: {
            "calibration_monitoring": ["surgeon", "patient"],
            "measurement_processed": ["surgeon", "patient"]
        },
        REGIONS["sa"]: {
            "calibration_monitoring": ["surgeon", "patient"],
            "measurement_processed": ["surgeon", "patient"]
        }
    }
     # Workflow filter based on region (short code like 'ae', 'ca', etc.) and dynamic args (e.g., site, surgeon, patient)
    @staticmethod
    def filter_workflow(region_code, *args):

        """
        Dynamically assigns data from tables to workflows based on region code and args.

        Args:
            region_code (str): The short code for the region (e.g., 'ae', 'ca').
            *args: Dynamic workflow categories (e.g., 'surgeon', 'patient').

        Returns:
            dict: A dictionary with the workflow assignments.
        """

        # Lookup the full region schema name from the short code (e.g., 'ae' -> 'ae_cosmos_origin_s1')
        region = Config.REGIONS.get(region_code)
        
        # If the region code is not valid, raise an error
        if not region:
            raise ValueError(f"Region code '{region_code}' is not valid.")
        
        # Get the tables for the full region name (like 'ae_cosmos_origin_s1')
        tables = Config.DB_CATALOG.get(region)
        
        # Raise an error if the region is not found in the DB_CATALOG
        if not tables:
            raise ValueError(f"Region '{region}' not found in the configuration.")
        
        # Initialize an empty dictionary to store the filtered data for each workflow
        filtered_data = {}

        # Process dynamically based on the arguments (like 'surgeon', 'patient', etc.)
        for table, labels in tables.items():
            # Loop through all the provided args
            for arg in args:
                # If the table is labeled for the given argument (surgeon, patient, etc.), assign it
                if arg in labels:
                    if arg not in filtered_data:
                        filtered_data[arg] = []
                    # Add the table to the appropriate workflow
                    filtered_data[arg].append(f"Processing {arg} data from '{table}' for region {region_code}")
        
        # If no args are provided or no processing happens, return a message
        if not filtered_data:
            filtered_data['message'] = f"No specific args provided for region {region_code}. No processing done."
        
        return filtered_data