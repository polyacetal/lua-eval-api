# lua-eval-api

U-16プログラミングコンテスト進行管理ツールCHroSのスコア計算部分のテスト

## 実行方法
APIサーバーの起動には以下のコマンドを使用します.
```
poetry run uvicorn lua_eval_api.main:app --reload --port 8000
```

以下のコマンドでAPIのテストをすることができます.
```
curl -X POST 'http://127.0.0.1:8000/calc' -H 'Content-Type: application/json' -d '{"x":3,"y":4}'
```
