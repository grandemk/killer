#!/usr/bin/env python3

import random
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("seed", help="seed for the order of the killer")
    parser.add_argument("name", help="your name")
    parser.add_argument("players_file", help="file with the name of the player (one per line)")
    return parser.parse_args()

def get_target(players, player_name):
    player_num = 0
    target = "unknown"
    for name in players:
        if player_name == name:
            target_num = player_num - 1
            target = players[target_num]
            break
        player_num += 1
    return target

def get_players(players_file):
    players = []
    with open(players_file, "r") as fp:
        for line in fp.read().splitlines():
            players += [line]
    return players

def main():
    args = parse_args()

    players = get_players(args.players_file)
    random.seed(args.seed)
    random.shuffle(players)

    target = get_target(players, args.name)

    print(players)
    print("{} target is {}".format(args.name, target))



if __name__ == "__main__":
    main()
