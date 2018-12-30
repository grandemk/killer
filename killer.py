#!/usr/bin/env python3

import random

def main():
    players = ["antoine", "elisa", "lucas", "gabriel", "sabine", "benoit", "michou", "julie", "morgane", "pier", "codex", "alex", "tom", "theo", "dorian", "quentin", "etienne", "kevin"]
    random.seed(0)
    random.shuffle(players)
    print(players)

if __name__ == "__main__":
    main()
