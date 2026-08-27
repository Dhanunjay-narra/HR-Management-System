"""
Domain-Specific Language (DSL) Abstract Syntax Tree (AST) Parser & Evaluator
Evaluates complex enterprise business conditions, date logic, and workflow triggers.
"""
import re
import math
from datetime import datetime, date, timedelta
from typing import Any, Dict, List, Optional, Union
from enum import Enum


class TokenType(Enum):
    NUMBER = "NUMBER"
    STRING = "STRING"
    BOOLEAN = "BOOLEAN"
    IDENTIFIER = "IDENTIFIER"
    OPERATOR = "OPERATOR"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    COMMA = "COMMA"
    EOF = "EOF"


class Token:
    def __init__(self, token_type: TokenType, value: Any, position: int):
        self.type = token_type
        self.value = value
        self.position = position

    def __repr__(self):
        return f"Token({self.type.name}, {self.value})"


class Lexer:
    OPERATORS = {
        "==", "!=", ">=", "<=", ">", "<",
        "&&", "||", "!", "+", "-", "*", "/", "%",
        "IN", "NOT_IN", "CONTAINS", "MATCHES", "STARTS_WITH", "ENDS_WITH"
    }

    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[0] if text else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def number(self) -> Token:
        start_pos = self.pos
        result = ""
        has_dot = False
        while self.current_char and (self.current_char.isdigit() or self.current_char == "."):
            if self.current_char == ".":
                if has_dot:
                    break
                has_dot = True
            result += self.current_char
            self.advance()
        val = float(result) if has_dot else int(result)
        return Token(TokenType.NUMBER, val, start_pos)

    def string(self, quote_char: str) -> Token:
        start_pos = self.pos
        self.advance()  # skip opening quote
        result = ""
        while self.current_char and self.current_char != quote_char:
            if self.current_char == "\\":
                self.advance()
                if self.current_char:
                    result += self.current_char
                    self.advance()
            else:
                result += self.current_char
                self.advance()
        if self.current_char == quote_char:
            self.advance()
        return Token(TokenType.STRING, result, start_pos)

    def identifier_or_keyword(self) -> Token:
        start_pos = self.pos
        result = ""
        while self.current_char and (self.current_char.isalnum() or self.current_char in ("_", ".", "$", "@")):
            result += self.current_char
            self.advance()

        upper = result.upper()
        if upper in ("TRUE", "FALSE"):
            return Token(TokenType.BOOLEAN, upper == "TRUE", start_pos)
        if upper in ("AND", "&&"):
            return Token(TokenType.OPERATOR, "&&", start_pos)
        if upper in ("OR", "||"):
            return Token(TokenType.OPERATOR, "||", start_pos)
        if upper in ("NOT", "!"):
            return Token(TokenType.OPERATOR, "!", start_pos)
        if upper in self.OPERATORS:
            return Token(TokenType.OPERATOR, upper, start_pos)

        return Token(TokenType.IDENTIFIER, result, start_pos)

    def get_next_token(self) -> Token:
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self.number()

            if self.current_char in ("'", '"'):
                return self.string(self.current_char)

            if self.current_char == "(":
                pos = self.pos
                self.advance()
                return Token(TokenType.LPAREN, "(", pos)

            if self.current_char == ")":
                pos = self.pos
                self.advance()
                return Token(TokenType.RPAREN, ")", pos)

            if self.current_char == ",":
                pos = self.pos
                self.advance()
                return Token(TokenType.COMMA, ",", pos)

            # Two char operators
            two = self.text[self.pos:self.pos + 2]
            if two in ("==", "!=", ">=", "<=", "&&", "||"):
                pos = self.pos
                self.advance()
                self.advance()
                return Token(TokenType.OPERATOR, two, pos)

            # Single char operators
            if self.current_char in (">", "<", "!", "+", "-", "*", "/", "%"):
                pos = self.pos
                ch = self.current_char
                self.advance()
                return Token(TokenType.OPERATOR, ch, pos)

            if self.current_char.isalpha() or self.current_char in ("_", "$", "@"):
                return self.identifier_or_keyword()

            # Unknown char skip
            self.advance()

        return Token(TokenType.EOF, None, self.pos)


class ASTNode:
    pass


class LiteralNode(ASTNode):
    def __init__(self, value: Any):
        self.value = value

    def __repr__(self):
        return f"Literal({self.value})"


class VariableNode(ASTNode):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Var({self.name})"


class UnaryOpNode(ASTNode):
    def __init__(self, op: str, operand: ASTNode):
        self.op = op
        self.operand = operand


class BinaryOpNode(ASTNode):
    def __init__(self, left: ASTNode, op: str, right: ASTNode):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinaryOp({self.left} {self.op} {self.right})"


class FunctionCallNode(ASTNode):
    def __init__(self, name: str, args: List[ASTNode]):
        self.name = name
        self.args = args


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type: TokenType):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise SyntaxError(f"Expected token {token_type}, got {self.current_token.type} at {self.current_token.position}")

    def factor(self) -> ASTNode:
        token = self.current_token
        if token.type in (TokenType.NUMBER, TokenType.STRING, TokenType.BOOLEAN):
            self.eat(token.type)
            return LiteralNode(token.value)
        elif token.type == TokenType.IDENTIFIER:
            name = token.value
            self.eat(TokenType.IDENTIFIER)
            # Check function call
            if self.current_token.type == TokenType.LPAREN:
                self.eat(TokenType.LPAREN)
                args = []
                if self.current_token.type != TokenType.RPAREN:
                    args.append(self.expr())
                    while self.current_token.type == TokenType.COMMA:
                        self.eat(TokenType.COMMA)
                        args.append(self.expr())
                self.eat(TokenType.RPAREN)
                return FunctionCallNode(name, args)
            return VariableNode(name)
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node
        elif token.type == TokenType.OPERATOR and token.value in ("!", "-", "+"):
            op = token.value
            self.eat(TokenType.OPERATOR)
            return UnaryOpNode(op, self.factor())
        raise SyntaxError(f"Unexpected token in factor: {token}")

    def term(self) -> ASTNode:
        node = self.factor()
        while self.current_token.type == TokenType.OPERATOR and self.current_token.value in ("*", "/", "%"):
            op = self.current_token.value
            self.eat(TokenType.OPERATOR)
            node = BinaryOpNode(node, op, self.factor())
        return node

    def arithmetic_expr(self) -> ASTNode:
        node = self.term()
        while self.current_token.type == TokenType.OPERATOR and self.current_token.value in ("+", "-"):
            op = self.current_token.value
            self.eat(TokenType.OPERATOR)
            node = BinaryOpNode(node, op, self.term())
        return node

    def comparison_expr(self) -> ASTNode:
        node = self.arithmetic_expr()
        cmp_ops = ("==", "!=", ">=", "<=", ">", "<", "IN", "NOT_IN", "CONTAINS", "MATCHES", "STARTS_WITH", "ENDS_WITH")
        while self.current_token.type == TokenType.OPERATOR and self.current_token.value in cmp_ops:
            op = self.current_token.value
            self.eat(TokenType.OPERATOR)
            node = BinaryOpNode(node, op, self.arithmetic_expr())
        return node

    def logical_and_expr(self) -> ASTNode:
        node = self.comparison_expr()
        while self.current_token.type == TokenType.OPERATOR and self.current_token.value == "&&":
            self.eat(TokenType.OPERATOR)
            node = BinaryOpNode(node, "&&", self.comparison_expr())
        return node

    def expr(self) -> ASTNode:
        node = self.logical_and_expr()
        while self.current_token.type == TokenType.OPERATOR and self.current_token.value == "||":
            self.eat(TokenType.OPERATOR)
            node = BinaryOpNode(node, "||", self.logical_and_expr())
        return node

    def parse(self) -> ASTNode:
        return self.expr()


class ASTEvaluator:
    @staticmethod
    def resolve_var(name: str, context: Dict[str, Any]) -> Any:
        # Resolve dot notation, e.g. employee.department.name
        parts = name.split(".")
        val = context
        for p in parts:
            if isinstance(val, dict):
                val = val.get(p)
            elif hasattr(val, p):
                val = getattr(val, p)
            else:
                return None
        return val

    @classmethod
    def evaluate(cls, node: ASTNode, context: Dict[str, Any]) -> Any:
        if isinstance(node, LiteralNode):
            return node.value

        if isinstance(node, VariableNode):
            return cls.resolve_var(node.name, context)

        if isinstance(node, UnaryOpNode):
            val = cls.evaluate(node.operand, context)
            if node.op in ("!", "NOT"):
                return not bool(val)
            if node.op == "-":
                return -val
            if node.op == "+":
                return +val

        if isinstance(node, BinaryOpNode):
            left = cls.evaluate(node.left, context)
            right = cls.evaluate(node.right, context)

            if node.op == "&&":
                return bool(left) and bool(right)
            if node.op == "||":
                return bool(left) or bool(right)
            if node.op == "==":
                return left == right
            if node.op == "!=":
                return left != right
            if node.op == ">":
                return (left or 0) > (right or 0)
            if node.op == "<":
                return (left or 0) < (right or 0)
            if node.op == ">=":
                return (left or 0) >= (right or 0)
            if node.op == "<=":
                return (left or 0) <= (right or 0)
            if node.op == "+":
                return (left or 0) + (right or 0)
            if node.op == "-":
                return (left or 0) - (right or 0)
            if node.op == "*":
                return (left or 0) * (right or 0)
            if node.op == "/":
                return (left or 0) / (right or 1)
            if node.op == "CONTAINS":
                return str(right).lower() in str(left).lower() if left is not None else False
            if node.op == "STARTS_WITH":
                return str(left).startswith(str(right)) if left is not None else False
            if node.op == "ENDS_WITH":
                return str(left).endswith(str(right)) if left is not None else False
            if node.op == "MATCHES":
                return bool(re.search(str(right), str(left))) if left is not None else False

        if isinstance(node, FunctionCallNode):
            args = [cls.evaluate(a, context) for a in node.args]
            fname = node.name.lower()
            if fname == "len":
                return len(args[0]) if args[0] is not None else 0
            if fname == "days_between":
                d1 = datetime.fromisoformat(str(args[0])) if isinstance(args[0], str) else args[0]
                d2 = datetime.fromisoformat(str(args[1])) if isinstance(args[1], str) else args[1]
                return abs((d1 - d2).days)
            if fname == "upper":
                return str(args[0]).upper()
            if fname == "lower":
                return str(args[0]).lower()
            if fname == "round":
                return round(args[0], int(args[1]) if len(args) > 1 else 0)

        return None

    @classmethod
    def execute_rule(cls, expression: str, context: Dict[str, Any]) -> bool:
        if not expression or not expression.strip():
            return True
        lexer = Lexer(expression)
        parser = Parser(lexer)
        ast = parser.parse()
        result = cls.evaluate(ast, context)
        return bool(result)
