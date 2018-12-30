#!/usr/bin/env python3

import random
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("seed", help="seed for the order of the killer")
    parser.add_argument("name", help="your name")
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


def main():
    args = parse_args()
    players = ["antoine", "elisa", "lucas", "gabriel", "sabine", "benoit", "michou", "julie", "morgane", "pier", "codex", "alex", "tom", "theo", "dorian", "quentin", "etienne", "kevin"]
    players = ["antoine", "elisa", "lucas", "sabine", "michou", "julie", "morgane", "pier", "codex", "tom", "dorian", "quentin", "etienne", "kevin"]
    random.seed(args.seed)
    random.shuffle(players)

    target = get_target(players, args.name)

    print(players)
    print("{} target is {}".format(args.name, target))



if __name__ == "__main__":
    main()
