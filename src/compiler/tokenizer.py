import re

def tokenizer(source_code: str="") -> list[str]:
    r = re.compile(r"[1-9]*")

    unfiltered_tokens: list[str] = r.findall(source_code)
    tokens = list(filter(bool, unfiltered_tokens))
    return tokens
