import json

def save_array_as_json(file="output.json", arr=None, is_init=True):

    """
        func:
            リストまたは辞書をJSONファイルで保存
        args:
            file: 出力ファイルのパス
            arr: リストまたは辞書
            is_init: 初期化（上書き）する（True）/しない（False）
    """

    # JSON文字列に変換
    line = (json.dumps(arr) + "\n") if (arr is not None) else ""

    # 保存: 上書き（w）/行の挿入（a）
    with open(file, mode=("w" if is_init else "a"), encoding="utf_8") as f:
        f.write(line)