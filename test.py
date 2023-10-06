# Intel: localhost:10080, RISC-V: localhost:10081
# IEEE浮動小数点数のランダムを生成し、
# それを入力として、/computeにPOSTリクエストを送信する。
# その結果を表示する。

import requests
import json
import random

# IEEE浮動小数点数のランダムを生成


def generate_random():
    # C言語でいわゆるshort型の範囲のランダムを生成
    return random.randint(-32768, 32767)
    # return random.uniform(-100, 100)

# メイン関数


def main():
    # POSTリクエストを送信するURL
    url_intel = "http://localhost:10080/compute"
    url_riscv = "http://localhost:10081/compute"

    # IEEE浮動小数点数のランダムを生成
    random_short1 = generate_random()
    random_short2 = generate_random()
    random_short3 = generate_random()
    random_short4 = generate_random()

    # POSTリクエストを送信
    response_intel = requests.post(url_intel, json.dumps(
        [random_short1, random_short2, random_short3, random_short4]))
    response_riscv = requests.post(url_riscv, json.dumps(
        [random_short1, random_short2, random_short3, random_short4]))

    # レスポンスをJSON形式で取得
    response_intel = response_intel.json()
    response_riscv = response_riscv.json()

    # 結果を表示
    print("random_short: " + str(random_short1) + ", " + str(random_short2) +
          ", " + str(random_short3) + ", " + str(random_short4))
    print("intel: " + str(response_intel))

    if response_intel == response_riscv:
        print("riscv: " + str(response_riscv))
        print("OK")
    else:
        print("riscv: " + str(response_riscv))
        print("NG")
        exit(1)


if __name__ == "__main__":
    while True:
        main()
