"""
Main:
Write a menu to select with map and with algorithm to implement.
"""
import os

from Utility import *
from BFS import *
from DFS import *
from GBFS import *
from A_star import *
from Search_star import *
from Search_t import *


def algo_no_bonus(bonus_points, matrix):
    start, end = extract_point(matrix)
    while 1:
        print('Enter a number to select a option')
        print('<1> DFS')
        print('<2> BFS')
        print('<3> GBFS')
        print('<4> A*')
        print('<0> Return')
        choice = int(input('Your option:'))
        cost = None
        route = None
        visited = None
        if choice == 1:
            cost, route, visited = dfs_no_bonus(start, end, matrix)
        elif choice == 2:
            cost, route, visited = bfs_no_bonus(start, end, matrix)
        elif choice == 3:
            print('Choose Heuristic')
            print('<1> Manhattan Norm')
            print('<2> Euclid Norm')
            t = int(input('Your option:'))
            if t == 1:
                cost, route, visited = gbfs_no_bonus(start, end, matrix, manhattan)
            elif t == 2:
                cost, route, visited = gbfs_no_bonus(start, end, matrix, euclid_norm)
        elif choice == 4:
            print('Choose Heuristic')
            print('<1> Manhattan Norm')
            print('<2> Euclid Norm')
            t = int(input('Your option:'))
            if t == 1:
                cost, route, visited = A_star_no_bonus(start, end, matrix, manhattan)
            elif t == 2:
                cost, route, visited = A_star_no_bonus(start, end, matrix, euclid_norm)
        else:
            break
        print('Cost=', cost)
        visualize_maze(matrix, bonus_points, start, end, route, visited)
        input()
        os.system('cls')


def algo_bonus(bonus_points, matrix):
    start, end = extract_point(matrix)
    cost = None
    route = None
    visited = None
    while 1:
        print('Enter a number to select a option')
        print('<1> Search T')
        print('<2> Search *')
        print('<0> Return')
        choice = int(input('Your option:'))
        if choice == 1:
            cost, route, visited = search_t(start, end, matrix, bonus_points)
        elif choice == 2:
            print('Choose Heuristic')
            print('<1> Manhattan Norm')
            print('<2> Euclid Norm')
            t = int(input('Your option:'))
            if t == 1:
                cost, route, visited = search_star(start, end, matrix, manhattan, bonus_points)
            elif t == 2:
                cost, route, visited = search_star(start, end, matrix, euclid_norm, bonus_points)
        else:
            break
        print('Cost=', cost)
        visualize_maze(matrix, bonus_points, start, end, route, visited)
        input()
        os.system('cls')


def map_no_bonus():
    while 1:
        print('Enter a number to select a option')
        print('<1> Map 01')
        print('<2> Map 02')
        print('<3> Map 03')
        print('<4> Map 04')
        print('<5> Map 05')
        print('<0> Return')
        choice = int(input('Your option:'))
        if choice == 1:
            bonus_points, matrix = read_file('map/map_no_bonus01.txt')
        elif choice == 2:
            bonus_points, matrix = read_file('map/map_no_bonus02.txt')
        elif choice == 3:
            bonus_points, matrix = read_file('map/map_no_bonus03.txt')
        elif choice == 4:
            bonus_points, matrix = read_file('map/map_no_bonus04.txt')
        elif choice == 5:
            bonus_points, matrix = read_file('map/map_no_bonus05.txt')
        else:
            break
        os.system('cls')
        algo_no_bonus(bonus_points, matrix)
        os.system('cls')


def map_bonus():
    while 1:
        print('Enter a number to select a option')
        print('<1> Map 01')
        print('<2> Map 02')
        print('<0> Return')
        choice = int(input('Your option:'))
        if choice == 1:
            bonus_points, matrix = read_file('map/map_bonus01.txt')
        elif choice == 2:
            bonus_points, matrix = read_file('map/map_bonus02.txt')
        else:
            break
        os.system('cls')
        algo_bonus(bonus_points, matrix)
        os.system('cls')


if __name__ == '__main__':
    while True:
        print('Enter a number to select a option')
        print('<1> Map no bonus')
        print('<2> Map bonus')
        print('<0> Quit')
        choice = int(input('Your option:'))
        if choice == 1:
            os.system('cls')
            map_no_bonus()
            os.system('cls')
        elif choice == 2:
            os.system('cls')
            map_bonus()
            os.system('cls')
        else:
            break
        os.system('cls')
