"""Module."""

from typing import NoReturn
from unittest import mock

import pytest

# !/usr/bin/env python
# -*- coding: utf-8 -*-

from . import random, gen_cpf0, gen_cpf1

__author__ = '@britodfbr'  # pragma: no cover


class CheckDojoGenCPF:
    """class test."""

    @pytest.mark.parametrize(
        'seed expected'.split(),
        [
            (0, '66048764707'),
            (7, '52601815906'),
            (11, '78778932807'),
        ],
    )
    def test_gen_pdf0(self, seed, expected) -> NoReturn:
        """Test it."""
        random.seed(seed)
        assert gen_cpf0() == expected
