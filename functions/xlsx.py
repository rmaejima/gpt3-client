import pandas as pd
import random


def import_xlsx():
    # input_file_name = "assets/input.xlsx"
    input_file_name = "assets/input_sample.xlsx"

    input_book = pd.ExcelFile(input_file_name)

    # Input sheet1 as DataFrame
    input_sheet_df = input_book.parse(input_book.sheet_names[0])

    return input_sheet_df  # DataFrame


def get_random_text(input_sheet_df, create_num):
    input_len = len(input_sheet_df)

    random_int = []
    for i in range(0, create_num, 1):
        random_int.append(random.randint(0, input_len - 1))

    print(random_int)

    text_list = []
    for key in random_int:
        print(key)
        text_list.append(input_sheet_df.iloc[key, 0])  # 0行目, key列目の値を追加

    return text_list
