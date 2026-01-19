from .tokenizer import tokenizer

def test_empty_input() -> None:
    assert tokenizer() == []

def test_ignore_white_space() -> None:
    assert tokenizer("  \n\t") == []