#!/usr/bin/env python3

import random
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("seed", help="seed for the order of the killer")
    return parser.parse_args()

def main():
    args = parse_args()
    players = ["antoine", "elisa", "lucas", "gabriel", "sabine", "benoit", "michou", "julie", "morgane", "pier", "codex", "alex", "tom", "theo", "dorian", "quentin", "etienne", "kevin"]
    random.seed(args.seed)
    random.shuffle(players)
    print(players)

if __name__ == "__main__":
    main()
