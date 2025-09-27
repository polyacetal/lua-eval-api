from fastapi import FastAPI, Query
from pydantic import BaseModel
from lupa import LuaRuntime
import os

app = FastAPI()
lua = LuaRuntime(unpack_returned_tuples=True)

# Luaファイルの読み込み
base_dir = os.path.dirname(os.path.dirname(__file__))
lua_file = os.path.join(base_dir, "lua_script", "formula.lua")

with open(lua_file, "r") as f:
    lua_code = f.read()
lua.execute(lua_code)

# デフォルト関数名
DEFAULT_FUNC = "calc_default"

class InputData(BaseModel):
    x: float
    y: float

@app.post("/calc")
def calculate(
    data: InputData,
    formula: str = Query(None, description="Lua関数名")
):
    try:
        func_name = formula if formula else DEFAULT_FUNC
        func = lua.eval(func_name)
        result = func(data.x, data.y)
        return {"formula": func_name, "result": result}
    except Exception as e:
        return {"error": str(e)}
