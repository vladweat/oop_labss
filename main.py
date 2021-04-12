from datetime import *

from classes import *

if __name__ == '__main__':

    #  Class MoveOperation testing
    move1 = MoveOperation('Dep2', 'Dep1', 'tech1', datetime.now())
    print('\n--- Class MoveOperation testing ---\n')

    print(f"new_location - {move1.get_new_location()}")
    move1.set_new_location('Dep123')
    print(f"new_location - {move1.get_new_location()}")

    print(f"old_location - {move1.get_old_location()}")
    move1.set_old_location('Dep321')
    print(f"old_location - {move1.get_old_location()}")

    print(f"tech - {move1.get_tech()}")
    move1.set_tech('tech2')
    print(f"tech - {move1.get_tech()}")

    print(f"data - {move1.get_date()}")
    move1.set_date(date(year=2000, month=3, day=23))
    print(f"data - {move1.get_date()}")

    #  Class Location testing
    location1 = Location(1, 'Department1')
    print('\n--- Class Location testing ---\n')

    print(f"num_of_room - {location1.get_num_of_room()}")
    location1.set_num_of_room(2)
    print(f"num_of_room - {location1.get_num_of_room()}")

    print(f"techs - {location1.get_techs()}")
    location1.set_techs(1)
    print(f"techs - {location1.get_techs()}")
    location1.set_techs([2, 3])
    print(f"techs - {location1.get_techs()}")

    print(f"department - {location1.get_department()}")
    location1.set_department('Dep2')
    print(f"department - {location1.get_department()}")
