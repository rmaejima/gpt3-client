from util.api import create_text_by_gpt3
from util.kaldi import export_dataframe_to_kaldi
from util.xlsx import get_random_text, import_xlsx


def main():
    # Import xlsx data
    input_sheet_df = import_xlsx()  # DataFrame

    # Export dataFrame data to kaldi data
    export_dataframe_to_kaldi(input_sheet_df)

    # Get random text by input_sheet_df
    text_list = get_random_text(input_sheet_df, 5)

    # Create text by GPT3
    created_text_List = create_text_by_gpt3(text_list)
    print(created_text_List["choices"][0]["text"] + "。")
    print("----------------------------------")
    print(created_text_List["choices"][1]["text"] + "。")
    print("----------------------------------")
    print(created_text_List["choices"][2]["text"] + "。")


if __name__ == "__main__":
    main()
