import pytest
from pathlib import Path
import os
import filecmp

INPUTCONTENT = """Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0"""

OUTPUTCONTENT = """1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pts
3. Snakes, 1 pts
5. Grouches, 0 pts
"""

INPUTCONTENT2 = """My test team 1, Another second test team 3
Another second test team 2, TeamHero 0
TeamHero 1, My test team 1"""

OUTPUTCONTENT2 = """1. Another second test team, 6 pts
2. My test team, 1 pts
2. TeamHero, 1 pts
"""

INPUTCONTENT3 = """Team1 1, Team2 1"""

OUTPUTCONTENT3 = """1. Team1, 1 pts
1. Team2, 1 pts
"""

def test_league_rank_standard():
    test_directory = Path() / "test"
    if not os.path.exists("test"):
        test_directory.mkdir()
    input_test_path = test_directory / "inputtest.txt"
    input_test_path.write_text(INPUTCONTENT, encoding="UTF8")
    output_test_path = test_directory / "outputtestcorrect.txt"
    output_test_path.write_text(OUTPUTCONTENT, encoding="UTF8")
    exit_status = os.system('league_rank -i test/inputtest.txt -o test/outputtestassert.txt')
    assert exit_status == 0
    assert filecmp.cmp('test/outputtestassert.txt', 'test/outputtestcorrect.txt')


def test_league_rank_multiple_spaces():
    test_directory = Path() / "test"
    if not os.path.exists("test"):
        test_directory.mkdir()
    input_test_path = test_directory / "inputtest.txt"
    input_test_path.write_text(INPUTCONTENT2, encoding="UTF8")
    output_test_path = test_directory / "outputtestcorrect.txt"
    output_test_path.write_text(OUTPUTCONTENT2, encoding="UTF8")
    exit_status = os.system('league_rank -i test/inputtest.txt -o test/outputtestassert.txt')
    assert exit_status == 0
    assert filecmp.cmp('test/outputtestassert.txt', 'test/outputtestcorrect.txt')


def test_league_rank_single_item():
    test_directory = Path() / "test"
    if not os.path.exists("test"):
        test_directory.mkdir()
    input_test_path = test_directory / "inputtest.txt"
    input_test_path.write_text(INPUTCONTENT2, encoding="UTF8")
    output_test_path = test_directory / "outputtestcorrect.txt"
    output_test_path.write_text(OUTPUTCONTENT2, encoding="UTF8")
    exit_status = os.system('league_rank -i test/inputtest.txt -o test/outputtestassert.txt')
    assert exit_status == 0
    assert filecmp.cmp('test/outputtestassert.txt', 'test/outputtestcorrect.txt')