"""Test module."""

from incolume.py.coding_dojo_jedi.dojo20240515 import (
    translate_deepl,
    translate_deepl_api,
)
import pytest
from typing import ClassVar


class CheckDeepl:
    """Check API de tradução."""

    tests0: ClassVar = [
        ('IT', 'Buona sera'),
        ('EN-US', 'Good evening'),
        ('DE', 'Guten Abend'),
        ('ES', 'Buenas noches'),
        ('FR', 'Bonsoir à tous'),
    ]

    @pytest.mark.skip
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        tests0,
    )
    def test_tranlate_deepl_api(self, entrance, expected):
        """Test tranlate deepl."""
        result = translate_deepl_api('Boa Noite', entrance)
        assert result['translations'][0]['text'] == expected

    @pytest.mark.skip
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        tests0,
    )
    def test_tranlate_deepl(self, entrance, expected):
        """Test tranlate deepl."""
        assert translate_deepl('Boa Noite', entrance) == expected
