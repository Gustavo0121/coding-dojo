"""Module dojo."""

from typing import ClassVar


class Numeros:
    """Converte numeros para romanos e arabicos."""

    nums: ClassVar = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }

    def __init__(self):
        """Init it."""

    def from_roman(self, numero_romano: str) -> int:
        """Transforma número romanos em arábicos."""
        result = 0
        qnt = len(numero_romano)
        for idx in range(qnt):
            if idx + 1 < qnt and (
                list(self.nums.keys())[
                    list(self.nums.values()).index(numero_romano[idx])
                ]
                < list(self.nums.keys())[
                    list(self.nums.values()).index(numero_romano[idx + 1])
                ]
            ):
                result -= list(self.nums.keys())[
                    list(self.nums.values()).index(numero_romano[idx])
                ]
            else:
                result += list(self.nums.keys())[
                    list(self.nums.values()).index(numero_romano[idx])
                ]

        return result

    def to_roman(self, num: int) -> str:
        """Transforma número arábico para romano."""
        result = ''
        for i in self.nums:
            while num >= i:
                num = num - i
                result = result + self.nums[i]
        return result
