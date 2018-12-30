#!/usr/bin/env python3

import random
import argparse

def vprint(line):
    if verbose:
        print(line)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("seed", help="seed for the order of the killer")
    parser.add_argument("name", help="your name")
    parser.add_argument("players_file", help="file with the name of the player (one per line)")
    parser.add_argument("--verbose", help="show debug warnings")
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

def get_player_killer_way(player):
    killer_ways = []
    try:
        with open(player + ".txt", "r") as fp:
            for line in fp.read().splitlines():
                killer_ways += [line]
    except:
        vprint("{} didn't provide a way to kill someone".format(player))
    return killer_ways

def how_will_target_be_killed(killer_ways, player_name, target_name, already_selected):
    filtered = []
    for key, value in killer_ways.items():
        if key != player_name and key != target_name:
            for v in value:
                if not v in already_selected:
                    filtered += [v]

    if len(filtered) < 1:
        raise Exception("There must be at least one way to kill someone")

    return filtered[0]

def main():
    args = parse_args()
    global verbose
    verbose = args.verbose

    players = get_players(args.players_file)
    random.seed(args.seed)
    random.shuffle(players)

    killer_ways = dict()

    for player in players:
        killer_ways[player] = get_player_killer_way(player)

    already_selected = []

    for player in players:
        target = get_target(players, player)
        target_kill_way = how_will_target_be_killed(killer_ways, args.name, target, already_selected)
        already_selected += [target_kill_way]
        print("La cible de {} est {}.\nPour tuer {}, il faut {}".format(player, target, target, target_kill_way))

if __name__ == "__main__":
    main()
