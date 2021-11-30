from util.api import create_text_by_gpt3
from util.kaldi import export_list_to_kaldi
from util.xlsx import get_random_text, import_xlsx


def main():
    number_of_request: int = 100

    # Import xlsx data
    input_sheet_df = import_xlsx()  # DataFrame

    # Export list data to kaldi data
    export_list_to_kaldi(input_sheet_df["文章"])

    # Get random text by input_sheet_df
    text_list = get_random_text(input_sheet_df, 5)

    # Create text by GPT3
    created_data = create_text_by_gpt3(text_list)

    # Convert to list[str]
    created_text_list: list[str] = []
    for i in range(len(created_data["choices"])):
        created_text_list.append(created_data["choices"][i]["text"])

    # Export list data to kaldi data
    export_list_to_kaldi(created_text_list)


if __name__ == "__main__":
    main()
