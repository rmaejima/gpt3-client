from functions.api import create_text_by_gpt3
from functions.xlsx import get_random_text, import_xlsx


def main():
    # Import xlsx data
    input_sheet_df = import_xlsx()  # DataFrame

    # Get random text by input_sheet_df
    text_list = get_random_text(input_sheet_df, 3)

    # Create text by GPT3
    created_text_List = create_text_by_gpt3(text_list)
    print(created_text_List["choices"][0]["text"])
    print("----------------------------------")
    print(created_text_List["choices"][1]["text"])
    print("----------------------------------")
    print(created_text_List["choices"][2]["text"])


if __name__ == "__main__":
    main()
