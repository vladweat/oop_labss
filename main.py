from datetime import *

from classes.MoveOperation import *
from classes.Location import *
from classes.User import *
from classes.Tech import *
from classes.Department import *
from classes.MaterialRespOfDepartment import *
from classes.HeadOfDepartment import *

if __name__ == '__main__':
    tech1 = Tech('tech #1', 'model v2', (23, 10, 2000), 2000, 'dep56')
    mo1 = MoveOperation('dep1', tech1.current_location, tech1, date=datetime.date.today())
    head1 = HeadOfDepartment('Kononov Vladislav Andreevich')
    head2 = HeadOfDepartment('TEst TESTOVICH Andreevich')
    mat_resp1 = MaterialRespOfDepartment('Ivanov Ivan Ivanovich')
    dep1 = Department('DEP #1', 'Department #1', head1, mat_resp1)
    dep1.set_head_dep(head2)
    loc1 = Location(dep1)

    loc1.add_in_techs(str(tech1))
    dep1.add_in_list_of_tech(str(tech1))
    dep1.add_in_locations(str(loc1))

    # print(head1)
    # print(mat_resp1)
    print(tech1)
    print(dep1)
    print(loc1)
    # print(mo1)