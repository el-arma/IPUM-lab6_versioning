# import click
import pandas as pd

# Not working
# @click.command()
# @click.option(
#     "--file-path",
#     required=True,
#     type=click.Path(exists=True),
#     help="Path to the file with Ames housing data.",
# )
# def inspect_ames_data(file_path: str) -> None:
#     df = pd.read_parquet(file_path)

#     print(df.head())





if __name__ == "__main__":
    
    file_path = r"C:\Users\eligi\Desktop\inne\my_scripts\PODYPLOMOWE\sem_II\IPUM\LAB\lab_06_files\data\ames_data_2006_2008.parquet"

    df = pd.read_parquet(file_path)

    print(df.head())
