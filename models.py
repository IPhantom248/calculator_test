from typing import Type

from pydantic import BaseModel, validator

ALLOWED_SYMBOLS = "1234567890+-*/()."


class Expression(BaseModel):
    phrase: str

    @validator('phrase')
    def only_numbers_or_math_symbols(cls: Type['Expression'], value: str) -> 'Expression':
        print(value)
        if extra_symbols := set(value) - set(ALLOWED_SYMBOLS):
            raise ValueError(f'Only numbers and math symbols. Extra symbols: {extra_symbols}')
        else:
            return value

    def calculate(self):
        try:
            return eval(self.phrase)
        except SyntaxError:
            raise SyntaxError("Incorrect expression.")
        except ZeroDivisionError:
            raise ZeroDivisionError("Zero division.")
