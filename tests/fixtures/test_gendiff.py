import pytest

from gendiff.scripts.gendiff import main


def test_gendiff():
    with pytest.raises(SystemExit):
        main()
