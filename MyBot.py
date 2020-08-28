#!/usr/bin/env python3
# Python 3.6

# Import the Halite SDK, which will let you interact with the game.
import hlt
poziti = {}
# This library contains constant values.
from hlt import constants
# This library contains direction metadata to better interface with the game.
from hlt.positionals import Direction

# This library allows you to generate random numbers.
import random

# Logging allows you to save messages for yourself. This is required because the regular STDOUT
#   (print statements) are reserved for the engine-bot communication.
import logging

""" <<<Game Begin>>> """

# This game object contains the initial game state.
game = hlt.Game()
# At this point "game" variable is populated with initial map data.
# This is a good place to do computationally expensive start-up pre-processing.
# As soon as you call "ready" function below, the 2 second per turn timer will start.
game.ready("SSJ2")

# Now that your bot is initialized, save a message to yourself in the log file with some important information.
#   Here, you log here your id, which you can always fetch from the game object by using my_id.
logging.info("Successfully created bot! My Player ID is {}.".format(game.my_id))

""" <<<Game Loop>>> """

def set_terminate():
    return constants.MAX_TURNS - 25

terminate = set_terminate()

while True:
    turn = game.turn_number
    apar = []
    game.update_frame()
    me = game.me
    game_map = game.game_map
    command_queue = []
    l = me.get_ships()
    for ship in me.get_ships():
        poziti[ship.id] = ship.position
    for i in poziti:
        apar.append(poziti[i])
    for ship in me.get_ships():
        posibilitati = ship.position.get_surrounding_cardinals() + [ship.position]
        posibilitati_halite = [game_map[elem].halite_amount for elem in posibilitati]

        if ship.halite_amount >= 950:
            ship.to_do = 1

        if ship.to_do == 1: 
            if ship.position == me.shipyard.position and game.turn_number < terminate:
                ship.to_do = 0
            else:
                move = ship.move(game_map.naive_navigate(ship, me.shipyard.position,turn,terminate))
        
        if ship.to_do == 0:
            if constants.WIDTH == 56:
                x = 1.80
            else:
                x = 1.50
            for i in range (len(posibilitati_halite)):
                for j in range (i, len(posibilitati_halite)):
                    if posibilitati_halite[i] < posibilitati_halite[j]:
                        posibilitati[i] , posibilitati[j] = posibilitati[j], posibilitati[i]
                        posibilitati_halite[i], posibilitati_halite[j] = posibilitati_halite[j], posibilitati_halite[i]

            for i in range (len(posibilitati)):
                if posibilitati[i] not in apar:
                    if game_map[posibilitati[i]].halite_amount > x * game_map[ship.position].halite_amount or game_map[posibilitati[i]].halite_amount == 0:
                        best = posibilitati[i]
                        apar.append(posibilitati[i])
                        break
                    else:
                        best = ship.position
                        apar.append(ship.position)
                        break    

            if game_map[ship.position].halite_amount < constants.MAX_HALITE / 10:
                move = ship.move(game_map.naive_navigate(ship, best, turn, terminate))
            else:
                move = ship.stay_still()

        if game.turn_number > terminate:
            for ship in me.get_ships():
                ship.to_do = 1
        command_queue.append(move)


    if  len(l) < 20 and me.halite_amount >= constants.SHIP_COST and not game_map[me.shipyard].is_occupied and game.turn_number < terminate:
        command_queue.append(me.shipyard.spawn())
        l = me.get_ships()
    game.end_turn(command_queue)

