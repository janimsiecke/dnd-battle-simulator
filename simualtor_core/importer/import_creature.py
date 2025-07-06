import json
from copy import deepcopy as dc

from simualtor_core.game.sim_logging import LOGGER
from simualtor_core.actors.base_actor import Actor
from simualtor_core.actors.monster_library import MONSTER_LIBRARY

def get_monster_from_library(monster_name: str) -> Actor | None:
    try:
        return dc(MONSTER_LIBRARY[monster_name])
    except ValueError:
        LOGGER.warning(f'Monster with name {monster_name} was not found in monster library')
        return None

def import_creature(import_file: str) -> [(str, Actor)]:
    with open(import_file, 'r') as file:
        import_dict = json.load(file)

    list_of_actors = []
    for key, value in import_dict.items():
        match value['type']:
            case 'character':
                pass
            case 'monster_preset':
                monster = get_monster_from_library(value['name'])
                if monster:
                    list_of_actors.append((key, monster))
            case 'monster_raw':
                pass
            case _:
                pass
    return list_of_actors
