from classes.Department import *
from classes.Location import *
from classes.Tech import *
from classes.MoveOperation import *

if __name__ == '__main__':
    """department test"""
    # dep1 = Department(short_name='first')
    # dep2 = Department(short_name='second')
    # dep3 = Department(short_name='3st')
    #
    # print(f"num_of_dep {dep1.get_short_name()} - {dep1.get_num_of_dep()}")
    # print(f"num_of_dep {dep2.get_short_name()} - {dep2.get_num_of_dep()}")
    # print(f"num_of_dep {dep3.get_short_name()} - {dep3.get_num_of_dep()}")
    #
    # dep3.set_num_of_dep(number_of_department=228)
    #
    # print(f"num_of_dep {dep1.get_short_name()} - {dep1.get_num_of_dep()}")
    # print(f"num_of_dep {dep2.get_short_name()} - {dep2.get_num_of_dep()}")
    # print(f"num_of_dep {dep3.get_short_name()} - {dep3.get_num_of_dep()}")
    #
    # print(dep1.__str__())
    # print(dep2.__str__())
    # print(dep3.__str__())
    """construct test"""
    #
    # dep1 = Department(short_name='first')
    # dep2 = Department(short_name='second')
    #
    # test_department(dep1)
    #
    # print(dep1.__str__())
    # print(dep2.__str__())


    """location test"""
    # loc1 = Location(department='dep1')
    # loc2 = Location(department='dep2')
    # #
    # # print(loc1.__str__())
    # # print(loc2.__str__())
    # #
    # # print(f"num_of_loc {loc1.get_num_of_room()}")
    # # print(f"num_of_loc {loc2.get_num_of_room()}")
    #
    # test_location(loc1)
    # print(loc1.__str__())
    # print(loc2.__str__())

    """tech test"""

    tech1 = Tech(name='tech1')
    tech2 = Tech(name='tech2')

    test_tech(tech1)

    print(tech1.__str__())
    print(tech2.__str__())

    """move operation construct test"""
    # move1 = MoveOperation()
    # move2 = MoveOperation()
    #
    # test_move_operation(move1)
    #
    # print(move1.__str__())
    # print(move2.__str__())

