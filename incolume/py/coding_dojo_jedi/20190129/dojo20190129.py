"""# Problema: Notas e Moedas.

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1021
"""
from typing import Any, List, Tuple, Union

MOEDAS = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
NOTAS = [100, 50, 20, 10, 5, 2]


def moedas(valor: float) -> Tuple[List[float], List[float]]:
    """Contabiliza a quantidade de notas e moedas."""
    vnotas: List[float] = [0, 0, 0, 0, 0, 0]
    vmoedas: List[float] = [0, 0, 0, 0, 0, 0]

    valor = calcula(NOTAS, vnotas, valor)
    valor = calcula(MOEDAS, vmoedas, valor)

    return vnotas, vmoedas


def calcula(monetario: float, lista: list, valor: float) -> List[float]:
    """Fatora o valor de acordo com a base monetária fornecida."""
    for i, moeda in enumerate(monetario):
        while valor >= moeda:
            lista[i] += 1
            valor -= moeda
            valor = round(valor, 2)
    return valor


# A solução abaixo demonstra alguns dos conceitos que
# comentamos no final do dojo e foi adicionada para fins
# didáticos sobre python


def moedas2(valor: float) -> Tuple[List[float], List[float]]:
    """Contabiliza a quantidade de notas e moedas."""
    (vnotas, valor) = calcula2(valor, NOTAS)
    (vmoedas, valor) = calcula2(valor, MOEDAS)

    return vnotas, vmoedas


def calcula2(
    valor: float,
    cedulas: list,
) -> Tuple[List[int], Union[float, Any]]:
    """Fatora o valor de acordo com a base monetária fornecida."""
    quantidades = [0] * len(cedulas)
    for (i, cedula) in enumerate(cedulas):
        # poderíamos usar divmod() também
        quantidades[i] = int(valor / cedula)
        valor = round(valor % cedula, 2)
    return (quantidades, valor)
