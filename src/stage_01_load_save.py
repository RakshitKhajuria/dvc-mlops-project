#from src.utils.all_utils import read_yaml, create_directory
#IT was throwing an error importing my own modules so i added the functions that i created in utils here
import argparse
import pandas as pd
'''
********************************************************************
********************************************************************
'''
import yaml
import os
import json


def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content


def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"directory is created at {dir_path}")


def save_local_df(data, data_path, index_status=False):
    data.to_csv(data_path, index=index_status)
    print(f"data is saved at {data_path}")


def save_reports(report: dict, report_path: str, indentation=4):
    with open(report_path, "w") as f:
        json.dump(report, f, indent=indentation)
    print(f"reports are saved at {report_path}")

'''
********************************************************************
********************************************************************
'''


def get_data(config_path):
    config = read_yaml(config_path)

    remote_data_path = config["data_source"]
    df = pd.read_csv(remote_data_path, sep=";")

    # save dataset in the local directory
    # create path to directory: artifacts/raw_local_dir/data.csv
    artifacts_dir = config["artifacts"]['artifacts_dir']
    raw_local_dir = config["artifacts"]['raw_local_dir']
    raw_local_file = config["artifacts"]['raw_local_file']

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)

    create_directory(dirs= [raw_local_dir_path])

    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
    
    df.to_csv(raw_local_file_path, sep=",", index=False)



if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)