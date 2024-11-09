import os
import json

LangSetPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DEF_LanguageSET.json")
DEF_LANG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DEF_lang.json")

AVAIL_types = ["elf", "exe", "aef", "caef"]
AVAIL_modes = ["x64", "x86"]

def CompileLangSET() -> dict:
    data  = {}

    with open(LangSetPath, "r") as f:
        data = json.load(f)
        f.close()

    return data

def Compile_LANG(CompiledLangSET: dict, langPath: str=DEF_LANG) -> tuple[dict, dict, list]:
    data:dict = {}

    if langPath == "":
        langPath = DEF_LANG

    with open(langPath, "r") as f:
        data = json.load(f)

    mode = "elf|x86"

    for i, v in enumerate(data.keys()):
        v = v.lower()

        if v in AVAIL_types:
            mode = mode.replace("elf", v)
        
        if v in AVAIL_modes:
            mode = mode.replace("x86", v)

    mode = mode.split("|")

    output_lang = data
    output_langSET = CompiledLangSET[mode[0]][mode[1]]

    return output_lang, output_langSET, mode