
from pyspark.sql import SparkSession
import glob
import os

def load_csv_from_cleaned_folder(spark, base_path):
    
    # Find directories matching 'cleaned_*' pattern
    search_pattern = os.path.join(base_path, "cleaned_*")
    directories = glob.glob(search_pattern)

    if not directories:
        raise FileNotFoundError("No Clean Data Found. Please Run 'update_clean_data.ipynb' before")

    # Assuming you want to process the first directory found
    first_dir = directories[0]
    csv_file_pattern = os.path.join(first_dir, "*.csv")
    csv_files = glob.glob(csv_file_pattern)

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in directory {first_dir}")

    # Read the first CSV file into a PySpark DataFrame
    # Adjust this part if you need to handle multiple CSV files
    dataframe = spark.read.csv(csv_files[0], header=True, inferSchema=True)

    return dataframe