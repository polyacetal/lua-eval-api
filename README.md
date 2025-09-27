# lua-eval-api

U-16プログラミングコンテスト進行管理ツールCHroSのスコア計算部分のテスト

## 環境構築
使用した言語とツールは以下の通りです.
- python: 3.12.2
- poetry: 2.1.3

ライブラリをインストールするために, 以下のコマンドを実行してください.
```
poetry install
```

## 実行方法
APIサーバーの起動には以下のコマンドを使用します.
```
poetry run uvicorn lua_eval_api.main:app --reload --port 8000
```

以下のコマンドでAPIのテストをすることができます.
```
curl -X POST 'http://127.0.0.1:8000/calc' -H 'Content-Type: application/json' -d '{"x":3,"y":4}'
```
