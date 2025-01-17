"""Test dojo."""

from http import HTTPStatus
from os import environ
from sys import version_info
from typing import ClassVar
from unittest import mock

from incolume.py.coding_dojo_jedi.utils import genfile
import pytest

from incolume.py.coding_dojo_jedi.dojo20220730.dojo20220730 import research


class TestCase:
    """Test case."""

    test_case_1: ClassVar = [
        (
            'Obi-Wan Kenobi',
            [
                {
                    'birth_year': '57BBY',
                    'created': '2014-12-10T16:16:29.192000Z',
                    'edited': '2014-12-20T21:17:50.325000Z',
                    'eye_color': 'blue-gray',
                    'films': [
                        'https://swapi.dev/api/films/1/',
                        'https://swapi.dev/api/films/2/',
                        'https://swapi.dev/api/films/3/',
                        'https://swapi.dev/api/films/4/',
                        'https://swapi.dev/api/films/5/',
                        'https://swapi.dev/api/films/6/',
                    ],
                    'gender': 'male',
                    'hair_color': 'auburn, white',
                    'height': '182',
                    'homeworld': 'https://swapi.dev/api/planets/20/',
                    'mass': '77',
                    'name': 'Obi-Wan Kenobi',
                    'skin_color': 'fair',
                    'species': [],
                    'starships': [
                        'https://swapi.dev/api/starships/48/',
                        'https://swapi.dev/api/starships/59/',
                        'https://swapi.dev/api/starships/64/',
                        'https://swapi.dev/api/starships/65/',
                        'https://swapi.dev/api/starships/74/',
                    ],
                    'url': 'https://swapi.dev/api/people/10/',
                    'vehicles': ['https://swapi.dev/api/vehicles/38/'],
                },
            ],
        ),
        (
            'Luke Skywalker',
            [
                {
                    'birth_year': '19BBY',
                    'created': '2014-12-09T13:50:51.644000Z',
                    'edited': '2014-12-20T21:17:56.891000Z',
                    'eye_color': 'blue',
                    'films': [
                        'https://swapi.dev/api/films/1/',
                        'https://swapi.dev/api/films/2/',
                        'https://swapi.dev/api/films/3/',
                        'https://swapi.dev/api/films/6/',
                    ],
                    'gender': 'male',
                    'hair_color': 'blond',
                    'height': '172',
                    'homeworld': 'https://swapi.dev/api/planets/1/',
                    'mass': '77',
                    'name': 'Luke Skywalker',
                    'skin_color': 'fair',
                    'species': [],
                    'starships': [
                        'https://swapi.dev/api/starships/12/',
                        'https://swapi.dev/api/starships/22/',
                    ],
                    'url': 'https://swapi.dev/api/people/1/',
                    'vehicles': [
                        'https://swapi.dev/api/vehicles/14/',
                        'https://swapi.dev/api/vehicles/30/',
                    ],
                },
            ],
        ),
        (
            'Tion Medon',
            [
                {
                    'birth_year': 'unknown',
                    'created': '2014-12-20T20:35:04.260000Z',
                    'edited': '2014-12-20T21:17:50.498000Z',
                    'eye_color': 'black',
                    'films': ['https://swapi.dev/api/films/6/'],
                    'gender': 'male',
                    'hair_color': 'none',
                    'height': '206',
                    'homeworld': 'https://swapi.dev/api/planets/12/',
                    'mass': '80',
                    'name': 'Tion Medon',
                    'skin_color': 'grey',
                    'species': ['https://swapi.dev/api/species/37/'],
                    'starships': [],
                    'url': 'https://swapi.dev/api/people/83/',
                    'vehicles': [],
                },
            ],
        ),
        (
            'luke skywalker',
            [
                {
                    'birth_year': '19BBY',
                    'created': '2014-12-09T13:50:51.644000Z',
                    'edited': '2014-12-20T21:17:56.891000Z',
                    'eye_color': 'blue',
                    'films': [
                        'https://swapi.dev/api/films/1/',
                        'https://swapi.dev/api/films/2/',
                        'https://swapi.dev/api/films/3/',
                        'https://swapi.dev/api/films/6/',
                    ],
                    'gender': 'male',
                    'hair_color': 'blond',
                    'height': '172',
                    'homeworld': 'https://swapi.dev/api/planets/1/',
                    'mass': '77',
                    'name': 'Luke Skywalker',
                    'skin_color': 'fair',
                    'species': [],
                    'starships': [
                        'https://swapi.dev/api/starships/12/',
                        'https://swapi.dev/api/starships/22/',
                    ],
                    'url': 'https://swapi.dev/api/people/1/',
                    'vehicles': [
                        'https://swapi.dev/api/vehicles/14/',
                        'https://swapi.dev/api/vehicles/30/',
                    ],
                },
            ],
        ),
        ('xpto', []),
        (
            'jinn',
            [
                {
                    'birth_year': '92BBY',
                    'created': '2014-12-19T16:54:53.618000Z',
                    'edited': '2014-12-20T21:17:50.375000Z',
                    'eye_color': 'blue',
                    'films': ['https://swapi.dev/api/films/4/'],
                    'gender': 'male',
                    'hair_color': 'brown',
                    'height': '193',
                    'homeworld': 'https://swapi.dev/api/planets/28/',
                    'mass': '89',
                    'name': 'Qui-Gon Jinn',
                    'skin_color': 'fair',
                    'species': [],
                    'starships': [],
                    'url': 'https://swapi.dev/api/people/32/',
                    'vehicles': ['https://swapi.dev/api/vehicles/38/'],
                },
            ],
        ),
        ('skyw', ['Luke Skywalker', 'Anakin Skywalker', 'Shmi Skywalker']),
    ]

    @pytest.mark.skipif(
        version_info < (3, 9, 0),
        reason='This run only Python 3.9+',
    )
    @pytest.mark.skip(reason='Replaced for test_research_mock')
    @pytest.mark.webtest()
    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        test_case_1,
    )
    def test_research(self, entrance, expected) -> None:
        """Test research."""
        timeout = float(environ.get('TIMEOUT', 0.8))
        assert research(entrance, timeout=timeout) == expected

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        test_case_1,
    )
    def test_research_mock(self, entrance, expected) -> None:
        """Test research."""
        cache_file = genfile().with_name('personagens-20220730.json')
        cache_file.unlink(missing_ok=True)

        with mock.patch('requests.get') as m_req:
            objreq = mock.MagicMock()
            objreq.status_code = HTTPStatus.OK
            objreq.json.return_value = {
                'count': 0,
                'next': None,
                'previus': None,
                'results': expected
                if (not expected or isinstance(expected[0], dict))
                else [{'name': x} for x in expected if x],
            }

            objreq2 = mock.MagicMock()
            objreq2.status_code = HTTPStatus.NOT_FOUND
            objreq2.json.return_value = {'detail': 'Not found'}

            m_req.side_effect = [objreq, objreq2]
            assert research(entrance) == expected
