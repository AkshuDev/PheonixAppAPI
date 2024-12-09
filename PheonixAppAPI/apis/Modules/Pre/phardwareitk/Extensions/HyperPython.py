"""
HyperPython is a Extension in PHardwareITK created by one teen. (Pheonix Studios (Akshobhya)).
This converts Python code to C/ASM.

Working on -> Compiler

Next Update -> C to Executable without GCC/Clang/....


NOTES:

1. Under Development.

2. Made because I wanted to.

3. Difference between Cython and HyperPython is as follows.

3.a. Hyper Python generates a Pure C file that can't communitcate with python, but cython does.

3.b. Cython generates a .c file from .pyx that needs to be compiled via gcc/clang/.... whereas HyperPython generates a .c file from .py that needs to be compiled via gcc/clang/.... FOR NOW. HyperPython.ToExecutable class under development.

4. You can use this but remember, this is under development.

5. This might give a huge benifit of file size.
"""

MAXBUFFER = 1024
MAXLINES = 50000

from typing import *

class bltin:
    def __init__(self, *value):
        self.isbltin:bool = True
        self.value = value

    @property
    def buitlin(self):
        return self.isbltin
    
    def __str__(self):
        return str(self.value)

class HyperList:
    def __init__(self, list1:list, list2:list, *args:list) -> None:
        self.list1 = list1
        self.list2 = list2
        self.lists = args

        self.hyperList = self.MHyperList(list1, list2, self.lists)

    @property
    def list_(self) -> list[tuple[list]]:
        return self.hyperList
    
    def MHyperList(self, list1:list, list2:list, *lists:list) -> list[tuple[list]]:
        lists_ = [list1, list2]
        for list in lists:
            lists_.append(list)

        if len(lists_) % 2 == 0:
            pass
        else:
            lists_.append([])

        hyperList = []

        skipTo = -1
        for i, v in enumerate(lists_):
            if i != skipTo:
                tuple_ = (v, lists_[i + 1])
                skipTo = i + 1
                hyperList.append(tuple_)

        return hyperList

    def append(self, list1:list, list2:list):
        list_ = list1

        for i, v in enumerate(list2):
            list_.append(v)

        self.hyperList.append(tuple(list_))

class buffer(bltin):
    def __init__(self, *args) -> None:
        self.args:tuple = args
        self.len:int = None
        self.buffer_:list = None

        buffer_:list = []

        if self.args and len(self.args) >= 1:
            for i, v in enumerate(self.args):
                for char in v:
                    buffer_.append(char)

        self.len = len(buffer_)
        self.buffer_ = buffer_

        super().__init__(self.buffer_)

    def __list__(self):
        return str(self.buffer_)
    
    @property
    def value(self) -> list:
        return self.buffer_
    
    @property
    def length(self) -> int:
        return self.len
    
class Generator_C:
    def __init__(self, InfTyp:HyperList.list_, includeHeaders:list):
        self.InfTyp = InfTyp
        self.includeHeaders = includeHeaders

        self.code = "#include <stdlib.h>\n#include <stdio.h>\n"

        self.finalCode = ""

        self.funcs:dict = {}

        print(InfTyp)
        print(includeHeaders)

    def MakeMainFunc(self):
        self.code += "\nint main(int argc, char** argv){\n"
        self.funcs["main"] = ""

    def Generate(self):
        if len(self.includeHeaders) > 0:
            for header in self.includeHeaders:
                self.code += "#include <" + str(header) + ">\n"
        
        self.MakeMainFunc()

        beautify = "\t"

        for i, v in enumerate(self.InfTyp):
            type_, class_, name, value = v

            type_ = beautify + str(type_)

            finalVar = type_ + " " + str(name) + " = " + str(value) + ";\n"

            self.funcs["main"] += "\n" + finalVar

        self.code += self.funcs["main"] + "}\n"

        print(self.code)

class Tokenizer_C:
    def __init__(self, code:str):
        # Tokenizer
        self.code = code

    def tokenize(self):
        import tokenize
        from io import BytesIO


        return tokenize.tokenize(BytesIO(self.code.encode()).readline())
    
    def infer_types(self):
        import ast
        tree = ast.parse(self.code)

        InfrTyp:HyperList = HyperList([], [])

        includeHeaders:list = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                # Handle variable assignment
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        var_name = target.id
                        value = node.value
                        var_type = "unknown"
                        var_typeClass = None

                        if isinstance(value, ast.Constant):
                            if isinstance(value.value, int): #int
                                if str(value.value) == "True" or str(value.value) == "False":
                                    var_type = "bool"
                                    var_typeClass = bool
                                    InfrTyp.append([var_type, var_typeClass], [var_name, str(value.value).lower()])
                                    includeHeaders.append("stdbool.h")
                                else: 
                                    var_type = "int"
                                    var_typeClass = int
                                    InfrTyp.append([var_type, var_typeClass], [var_name, value.value])
                            elif isinstance(value.value, float): # float
                                var_type = "float"
                                var_typeClass = float
                                InfrTyp.append([var_type, var_typeClass], [var_name, value.value])
                            elif isinstance(value.value, str): # String
                                if len(value.value) >= 1:
                                    if len(value.value) == 1:
                                        var_type = "char"
                                        var_typeClass = buffer
                                        InfrTyp.append([var_type, var_typeClass], [var_name, value.value])
                                    else:
                                        var_type = "char*"
                                        var_typeClass = str
                                        InfrTyp.append([var_type, var_typeClass], [var_name, value.value])
                                else:
                                    var_type = "null"
                                    var_typeClass = None
                                    InfrTyp.append([var_type, var_typeClass], [var_name, value.value])
                            elif isinstance(value.value, bool): # Bool
                                var_type = "bool"
                                var_typeClass = bool
                                InfrTyp.append([var_type, var_typeClass], [var_name, str(value.value).lower()])
                                includeHeaders.append("stdbool.h")

        return InfrTyp.list_, includeHeaders
                            

# 0 -> C
# 1 -> ASM
# 2 -> EXE
# 3 -> ELF
# 4 -> AEF
# 5 -> CAEF
def Convert(to:int=0, code:str="", file:str="") -> int:
    """_summary_

    Args:
        to (int, optional): Which type to convert to. Defaults to 0.
        Available Types ->
            # 0 -> C
            # 1 -> ASM
            # 2 -> EXE
            # 3 -> ELF
            # 4 -> AEF
            # 5 -> CAEF

        code (str, optional): If code is in string form, pass here.
        file (str, optional): If code in inside a file, pass file path here.

    Returns:
        int: 0 for success, 1 for failure, -11 for OSError.
    """
    if code and code != "":
        if to == 0:
            tokenizer = Tokenizer_C(code)
            tokens = tokenizer.tokenize()
            print(tokens)
            ifr, headers = tokenizer.infer_types()
            ifr.pop(0)
            ifr.pop(0)
            generator = Generator_C(ifr, headers)
            generator.Generate()
    else:
        if not file or file == "":
            raise ValueError("Neither File nor Code Arguments have been passes")
    
        else:
            code = ""
            with open(file, "r") as f:
                code = f.read()
                f.close()

            if to == 0:
                tokenizer = Tokenizer_C(code)
                tokens = tokenizer.tokenize()
                ifr, headers = tokenizer.infer_types(tokens)

                ifr.pop(0)
                ifr.pop(0)

                generator = Generator_C(ifr, headers)
                generator.Generate()
    return 0