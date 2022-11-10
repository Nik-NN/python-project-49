#!/usr/bin/env python3

from brain_games.games import game_calc
from brain_games.logic import games_logic

def main():
    games_logic.engine(game_calc)

if __name__ == '__main__':
    main()
