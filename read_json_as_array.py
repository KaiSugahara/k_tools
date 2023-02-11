import json

def read_json_as_array(file=""):

    """
        func:
            JSONファイルで保存されたリストまたは辞書を読み込み
        args:
            file: JSONファイルのパス
        returns:
            - リストまたは辞書 or 複数行の場合はそのリスト
    """

    # 読み込み
    with open(file, mode="r", encoding="utf_8") as f:
        lines = [line for line in f.readlines()]

    # JSONに変換
    arrays = [json.loads(line) for line in lines]

    return arrays[0] if len(arrays) == 1 else arrays