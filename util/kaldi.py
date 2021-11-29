import pandas as pd


def export_dataframe_to_kaldi(input_sheet_df: pd.DataFrame):
    text_list: list[str] = input_sheet_df["文章"]

    id: str = "nurse_lang"
    file_path: str = "export/kaldi"
    f_obj = open(file_path, "a")

    for text in text_list:
        print(f"{id} {text}", file=f_obj)
