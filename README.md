# AkariSample
Akari Sample Source Code

Intel Intrinsic関数のGCCにおける実装のテストを行うためのシステム（Akari）
その一部である、「_mm_cvtpi16_ps」のテストを行うためのソースコードです。

## 使い方
1. Dockerをインストールする
2. このリポジトリをクローンする
3. このリポジトリのルートディレクトリで、以下のコマンドを実行する
```
docker compose up -d
```

## Docker上のUbuntu環境を構築する場合
```
apt update -y && apt install git vim curl cmake build-essential -y
apt install python3 python3-pip -y
```

compute.cとcompute.pyを同じディレクトリに置き、以下のコマンドを実行する
```
python3 compute.py
```

事前に、以下のコマンドを実行しておく
```
pip3 install fastapi uvicorn
```

RISC-VのfastapiはRustを使っているため、Rustをインストールする必要がある
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## ホストマシン上でテストを実行
```
python3 test.py
```

## ライセンス
MIT License (c) 2023 Takahashi Akari
