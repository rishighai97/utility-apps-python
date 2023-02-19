import pandas as pd


def write_to_excel(json_data, excel_file_path):
    try:
        with pd.ExcelWriter(excel_file_path) as writer:
            for key in json_data.keys():
                df = pd.DataFrame(json_data[key])
                df.to_excel(writer, sheet_name=key, index=False)
        print("Data exported successfully")
    except Exception as e:
        print("Exception occurred while converting response difference to excel")
        raise e
