import pandas as pd


def export_list_to_kaldi(text_list: list[str]):
    id: str = "nurse_lang"
    file_path: str = "export/kaldi"
    f_obj = open(file_path, "a")

    for text in text_list:
        print(f"{id} {text.strip()}", file=f_obj)
