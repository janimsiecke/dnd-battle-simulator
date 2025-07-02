from datetime import datetime

import game.battle_logging as blog

def run_simulation():
    # Import Characters and Monsters
    # Populate Board
    # Fight!
    blog.log_message(f"Simulation starts at {datetime.now().strftime('%H:%M:%S - %d.%m.%Y')}!")
    blog.log_message(f"The battle begins!")
    blog.log_turn('Still battling!')
    pass

if __name__ == '__main__':
    blog.initiate_logging()
    run_simulation()