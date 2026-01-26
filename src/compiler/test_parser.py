import pytest
from compiler.tokenizer import Token, SourceLocation
from compiler.parser import parse 
import compiler.custom_ast as ast

t = ["int_literal", "identifier"]

def create_tokens(*token_args: list[str | int]):
    tokens = [] 
    for args in token_args:
        token = Token(args[0], args[1], SourceLocation(0, 0))
        token.location._testing = True
        tokens.append(token)
    return tokens

def get_tokens():
    tokens = [
        Token("1", "int_literal", SourceLocation(0, 0)),
        Token("+", "identifier", SourceLocation(0, 0)),
        Token("1", "int_literal", SourceLocation(0, 0)),
    ]
    for token in tokens:
        token.location._testing = True
    return tokens

def test_parse_plus_operation():
    one = ast.Literal(1)
    expression = ast.BinaryOp(one, "+", one )
    tokens = create_tokens([1, t[0]], ["+", t[1]], [1, t[0]])
    print(tokens)
    parsed = parse(tokens)
    assert parsed == expression

