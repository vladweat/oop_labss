class User:
    def __init__(self, login, password, full_name, role):
        self.login = login
        self.password = password
        self.full_name = full_name
        self.role = role

    def get_login(self):
        return self.login

    def set_login(self, login):
        self.login = login

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_full_name(self):
        return self.full_name

    def set_full_name(self, full_name):
        self.full_name = full_name

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role


class HeadOfDepartment:
    pass


class MaterialRespOfDepartment:
    pass


class Tech:
    def __init__(self, inventory_number, name, model, date_of_purchase, price, current_location):
        self.inventory_number = inventory_number
        self.name = name
        self.model = model
        self.date_of_purchase = date_of_purchase
        self.price = price
        self.current_location = current_location

    def get_inventory_number(self):
        return self.inventory_number

    def set_inventory_number(self, inventory_number):
        self.inventory_number = inventory_number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_date_of_purchase(self):
        return self.date_of_purchase

    def set_date_of_purchase(self, date_of_purchase):
        self.date_of_purchase = date_of_purchase

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_current_location(self):
        return self.current_location

    def set_current_location(self, current_location):
        self.current_location = current_location


class Department:
    def __init__(self, number_of_department, short_name, full_name, head_of_department, resp_of_department):
        self.num_of_dep = number_of_department
        self.short_name = short_name
        self.full_name = full_name
        self.head_dep = head_of_department
        self.resp_dep = resp_of_department
        self.list_of_tech = []
        self.locations = []

    def get_num_of_dep(self):
        return self.num_of_dep

    def set_num_of_dep(self, number_of_department):
        self.num_of_dep = number_of_department

    def get_short_name(self):
        return self.short_name

    def set_short_name(self, short_name):
        self.short_name = short_name

    def get_full_name(self):
        return self.full_name

    def set_full_name(self, full_name):
        self.full_name = full_name

    def get_head_dep(self):
        return self.head_dep

    def set_head_dep(self, head_of_department):
        self.head_dep = head_of_department

    def get_resp_dep(self):
        return self.resp_dep

    def set_resp_dep(self, resp_of_department):
        self.resp_dep = resp_of_department

    def get_list_of_tech(self):
        return self.list_of_tech

    def set_list_of_tech(self, tech):  # equal add_in_list_of_tech()
        self.list_of_tech.append(tech)

    def get_locations(self):
        return self.locations

    def set_locations(self, location):  # equal add_in_locations()
        self.locations.append(location)


class MoveOperation:
    def __init__(self, new_location, old_location, tech, date):
        self.new_location = new_location
        self.old_location = old_location
        self.tech = tech
        self.date = date

    def get_new_location(self):
        return self.new_location

    def set_new_location(self, new_location):
        self.new_location = new_location

    def get_old_location(self):
        return self.old_location

    def set_old_location(self, old_location):
        self.old_location = old_location

    def get_tech(self):
        return self.tech

    def set_tech(self, tech):
        self.tech = tech

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date


class Location:
    def __init__(self, num_of_room, department):
        self.num_of_room = num_of_room
        self.techs = []
        self.department = department

    def get_num_of_room(self):
        return self.num_of_room

    def set_num_of_room(self, num_of_room):
        self.num_of_room = num_of_room

    def get_techs(self):
        return self.techs

    def set_techs(self, tech):  # equal add_in_techs()
        self.techs.append(tech)

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department


class WebService:
    pass
