from datetime import datetime

import simualtor_core.game.sim_logging as blog
from simualtor_core.game.game import Game

def run_simulation():
    # Import Characters and Monsters
    # Populate Board
    # Fight!
    blog.log_message(f"Simulation starts at {datetime.now().strftime('%H:%M:%S - %d.%m.%Y')}!")
    game = Game()
    pass

if __name__ == '__main__':
    blog.initiate_logging()
    #blog.initiate_battle_logging()
    run_simulation()
