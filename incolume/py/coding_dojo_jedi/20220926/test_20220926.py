import pytest
from dojo20220926 import protein


@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        ('UGCGAUGAAUGGGCUCGCUCC', 'CDEWARS'),
        ('AUG', 'M'),
        ('AUGUGA', 'M'),
        ('AUGGUUAGUUGA', 'MVS'),
        ('AUGUCCUUCCAUCAAGGAAACCAUGCGCGUUCAGCUUUCUGA', 'MSFHQGNHARSAF'),
        ('AUGCUUCAAGUGCACUGGAAAAGGAGAGGGAAAACCAGUUGA', 'MLQVHWKRRGKTS'),
        ('AUGGCGUUCAGCUUUCUAUGGAGGGUAGUGUACCCAUGCUGA', 'MAFSFLWRVVYPC'),
        ('AUGCAGCUUUCUAUGGAGGGUAGUGUUAACUACCACGCCUGA', 'MQLSMEGSVNYHA'),
        ('AUGCUAUGGAGGGUAGUGUUAACUACCACGCCCAGUACUUGA', 'MLWRVVLTTTPST'),
        (
            'AUGUAUCCUUCCAUCAAGGAAACCAUGCGCGUUCAGCUUUCUAU'
            'GGAGGGUAGUGUUAACUACCACGCCUUCAAGUGCACUGGAAAAG'
            'GAGAGGGAAAACCAUACGAAGGCACCCAAAGCCUGAAUAUUACA'
            'AUAACUGAAGGAGGUCCUCUGCCAUUUGCUUUUGACAUUCUGUC'
            'ACACGCCUUUCAGUAUGGCAUCAAGGUCUUCGCCAAGUACCCCA'
            'AAGAAAUUCCUGACUUCUUUAAGCAGUCUCUACCUGGUGGUUUU'
            'UCUUGGGAAAGAGUAAGCACCUAUGAAGAUGGAGGAGUGCUUUC'
            'AGCUACCCAAGAAACAAGUUUGCAGGGUGAUUGCAUCAUCUGCA'
            'AAGUUAAAGUCCUUGGCACCAAUUUUCCCGCAAACGGUCCAGUG'
            'AUGCAAAAGAAGACCUGUGGAUGGGAGCCAUCAACUGAAACAGU'
            'CAUCCCACGAGAUGGUGGACUUCUGCUUCGCGAUACCCCCGCAC'
            'UUAUGCUGGCUGACGGAGGUCAUCUUUCUUGCUUCAUGGAAACA'
            'ACUUACAAGUCGAAGAAAGAGGUAAAGCUUCCAGAACUUCACUU'
            'UCAUCAUUUGCGUAUGGAAAAGCUGAACAUAAGUGACGAUUGGA'
            'AGACCGUUGAGCAGCACGAGUCUGUGGUGGCUAGCUACUCCCAA'
            'GUGCCUUCGAAAUUAGGACAUAACUGA',
            'MYPSIKETMRVQLSMEGSVNYHAFKCTGKGEGKPYEGTQSLNITITEGGPLPFAFDILSHAFQYG'
            'IKVFAKYPKEIPDFFKQSLPGGFSWERVSTYEDGGVLSATQETSLQGDCIICKVKVLGTNFPANG'
            'PVMQKKTCGWEPSTETVIPRDGGLLLRDTPALMLADGGHLSCFMETTYKSKKEVKLPELHFHHLR'
            'MEKLNISDDWKTVEQHESVVASYSQVPSKLGHN',
        ),  # This gene encodes for a
        # protein that fluoresces green in the Snakelocks anemone!
    ),
)
def test_protein(entrance, expected):
    assert protein(entrance) == expected
