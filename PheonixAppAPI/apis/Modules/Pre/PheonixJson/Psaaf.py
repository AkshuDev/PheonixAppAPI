import pathlib
import os
import sys

class PheonixStudiosAccessFile:
    """This class allows you to create a PheonixStudiosAccessFile. This File can be used to find the path of the obj referred to or can also be used to get data of the object. For tutorial go to AkshobhyaEverything YT channel.

        Args:
            path (Any): The Path to create/read/analyze the file without the file name. DO NOT INCLUDE THE ACTUAL FILE NAME AND EXTENSION.
        """
    def __init__(self, path) -> None:
        """This class allows you to create a PheonixStudiosAccessFile. This File can be used to find the path of the obj referred to or can also be used to get data of the object. For tutorial go to AkshobhyaEverything YT channel.

        Args:
            path (Any): The Path to create/read/analyze the file. DO NOT INCLUDE THE ACTUAL FILE NAME AND EXTENSION.
        """
        self.path = path

    def _dict_to_str(self, name:str, data:dict) -> str:
        content = ""

        content = f"{name} -> {'{'}\n"

        for key, value in data.items():
            if not value == "":
                content += f'{key} -> {value},\n'
            else:
                content += f'{key}\n'

        content = content[:-2]
        content += "\n}"

        return content

    def _str_to_dict(self, data:str) -> dict:
        content:dict = {}

        data_str = data.splitlines()
        skip = False
        gather = ""
        testv = ""
        inside = False
        current_class = ""

        content["Classes"] = {}
        content["Important Variables"] = {}
        content["Data"] = {}

        for i, v in enumerate(data_str):
            if not skip and not inside:
                if v.startswith('##') or v.startswith("#$"):
                    if v.startswith("##"):
                        content[v] = ""
                        continue
                    else:
                        skip = True
                        testv = v
                        gather += v
                elif v.startswith("@"):
                    current_class = v.replace(" ", "").replace("->", "").replace("{", "").replace("@", "")
                    content["Classes"][v.replace(" ", "").replace("->", "").replace("{", "")] = current_class
                    content["Data"][current_class] = {}
                    inside = True
                    continue
                else:
                    if "->" in v:
                        v = v.replace(" ", "").split("->")
                        if v[0].islower and not "|" in v[0]:
                            content["Data"][current_class][v[0]] = v[1].replace(",", "")
                        elif v[0].isupper() and "|" in v[0]:
                            content["Data"][current_class][v[0].replace("|", "")] = v[1].replace(",", "")
                            content["Important Variables"][v[0].replace("|", "")] = v[1].replace(",", "")

            if inside:
                if v.startswith('##') or v.startswith("#$"):
                    if v.startswith("##"):
                        content["Data"][current_class][v] = ""
                        continue
                    else:
                        skip = True
                        testv = v
                        gather += v
                elif v.endswith("}"):
                    inside = False
                    continue
                else:
                    if "->" in v:
                        v = v.replace(" ", "").split("->")
                        if v[0].islower and not "|" in v[0]:
                            content["Data"][current_class][v[0]] = v[1].replace(",", "")
                        elif v[0].isupper() and "|" in v[0]:
                            content["Data"][current_class][v[0].replace("|", "")] = v[1].replace(",", "")
                            content["Important Variables"][v[0].replace("|", "")] = v[1].replace(",", "")

            if skip and not inside:
                if v.endswith("#$"):
                    skip = False
                    if not testv == v:
                        gather += v
                    content[gather] = ""
                    gather = ""
                    continue
            elif skip and inside:
                if v.endswith("#$"):
                    skip = False
                    if not testv == v:
                        gather += v
                    content["Data"][current_class][gather] = ""
                    gather = ""
                    continue

        return content

    def read(self, name_of_file:str) -> dict:
        """Reads the paaf file

        Args:
            name_of_file (str): The name of the file to read without the extension

        Returns:
            dict: The output
        """
        data = ""
        with open(os.path.join(self.path, name_of_file+".paaf")) as f:
            f.seek(0)
            data = f.read()

        #process data
        data = self._str_to_dict(data)

        return data

    def create(self, name_of_file:str, metadata:dict={"##This is the metadata class": ""}, access:dict={"##This is the access class": ""}, other_content:dict={"##Other content (OC) class": ""}) -> None:
        """This function creates a new .psaaf file.

        Args:
            name_of_file (str): The name of the file to create without the extension.
            metadata (dict, optional): The metadata class content. For comments start with ## (Normal) or #$ (Multiline) and add the value as nothing. Defaults to {'##This is the metadata class': ''}
            access (dict, optional): The access class content. For comments start with ## (Normal) or #$ (Multiline) and add the value as nothing. Defaults to {'##This is the access class': ''}
            other_conetent (dict, optional): This dictionary denotes other content required to add . For comments start with ## (Normal) or #$ (Multiline) and add the value as nothing. Defaults to {'##Other content (OC) class': ''}
        """
        content = ""
        content_dict = {}
        skip = False

        content_dict["@Metadata"] = {}

        for i, v in enumerate(metadata.keys()):
            if v.isupper():
                content_dict["@Metadata"][f'|{v}|'] = metadata[v]
            elif v.startswith("##") or v.startswith("#$"):
                if v.startswith("##"):
                    content_dict["@Metadata"][v] = ""
                    continue
                else:
                    if v.endswith("#$"):
                        content_dict["@Metadata"][v] = ""
                        continue
                    else:
                        raise ValueError(f"The multiline comment in metadata must end.")
            elif v.startswith("@") or v.startswith("%"):
                raise ValueError(f"A class cannot include another class.")
            else:
                content_dict["@Metadata"][v] = metadata[v]

        content += "\n"
        content += self._dict_to_str("@Metadata", content_dict["@Metadata"])

        content_dict["@Access"] = {}

        for i, v in enumerate(access.keys()):
            if v.isupper():
                content_dict["@Access"][f'|{v}|'] = access[v]
            elif v.startswith("##") or v.startswith("#$"):
                if v.startswith("##"):
                    content_dict["@Access"][v] = ""
                    continue
                else:
                    if v.endswith("#$"):
                        content_dict["@Access"][v] = ""
                        continue
                    else:
                        raise ValueError(f"The multiline comment in metadata must end.")
            elif v.startswith("@") or v.startswith("%"):
                raise ValueError(f"A class cannot include another class.")
            else:
                content_dict["@Access"][v] = access[v]

        content += "\n"
        content += self._dict_to_str("@Access", content_dict["@Access"])

        content_dict["@OC"] = {}

        for i, v in enumerate(other_content.keys()):
            if v.isupper():
                content_dict["@OC"][f'|{v}|'] = other_content[v]
            elif v.startswith("##") or v.startswith("#$"):
                if v.startswith("##"):
                    content_dict["@OC"][v] = ""
                    continue
                else:
                    if v.endswith("#$"):
                        content_dict["@OC"][v] = ""
                        continue
                    else:
                        raise ValueError(f"The multiline comment in metadata must end.")
            elif v.startswith("@") or v.startswith("%"):
                raise ValueError(f"A class cannot include another class.")
            else:
                content_dict["@OC"][v] = other_content[v]

        content += "\n"
        content += self._dict_to_str("@OC", content_dict["@OC"])

        with open(os.path.join(self.path, name_of_file+".paaf"), "w") as f:
            f.write(content)
