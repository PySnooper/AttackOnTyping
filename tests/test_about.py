
from about.about  import logan, nebiyu, anthony, nick


def test_logan(capsys):
    logan()
    captured = capsys.readouterr()
    expected = 'Logan Jones'
    assert expected in captured.out
    

def test_nebiyu(capsys):
    nebiyu()
    captured = capsys.readouterr()
    expected = 'Nebiyu Kifle'
    assert expected in captured.out

def test_anthony(capsys):
    anthony()
    captured = capsys.readouterr()
    expected = 'Anthony Beaver'
    assert expected in captured.out

def test_nick(capsys):
    nick()
    captured = capsys.readouterr()
    expected = 'Nick Dorkins'
    assert expected in captured.out