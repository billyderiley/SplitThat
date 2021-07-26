# Title: Deliverable 3
# Course: COMP0015
# Author: Billy Riley
# Description: splitthat_presenter_module contains the methods responsible for relaying information from the user, to
# the object oriented code in the splitthat_classes_module


########################################################################################################################
# Initial Setup
#
# Instances of object Datafile are created here, with related datafiles being opened and set to instance
#  variable 'self.datafile'. Instances of objects User, and Split, are set to none initially here, until are required
# for use. All instances are defined as Global Objects for wide use across the program.

import splitthat_classes_module as classes_module
import random as randomiser


try:  # Try to open the following file
    users_file = classes_module.DataFile("users_file.txt")  # Filename.txt given as the parameter, create
except FileNotFoundError:  # a Global instance of Datafile. If file is not found, FileNotFoundError is thrown.
    print("User data file not found!")
try:
    projects_file = classes_module.DataFile("projects_file.txt")
except FileNotFoundError:
    print("Projects data file not found!")
try:
    bills_file = classes_module.DataFile("bills_file.txt")
except FileNotFoundError:
    print("Bill data file not found!")
try:
    rentals_file = classes_module.DataFile("rentals_file.txt")
except FileNotFoundError:
    print("Rentals data file not found!")


user_instance = None  # Future instances of objects User and Split, are set to None and are made Global here.
split_instance = None


########################################################################################################################
# Valid Menu Input
# All'valid' menu methods serve to prevent the user impossibly navigating in the program. The choices are stored as in a
# dictionary, with a short description of what they imply at a given menu screen, as the 'value' pairs

MAIN_MENU_OPTIONS = {"L": "To Login", "R": "To Register", "G": "Proceed as Guest", "Q": "Quit"}
USER_MENU_OPTIONS = {"S": "To See Splits", "C": "To Create a Split", "L": "To Logout", "Q": "Quit"}
SPLIT_MENU_OPTIONS = {"B": "Split Bill", "R": "Split Rent", "P": "Split Project Credit", "Q": "Go Back"}
VOTE_MENU_OPTIONS = {"V": "To Vote for a Member's Contribution"}


def valid_main_menu_choice(user_input):
    return user_input.upper() in MAIN_MENU_OPTIONS or user_input.lower() in MAIN_MENU_OPTIONS


def valid_user_menu_choice(user_input):
    return user_input.upper() in USER_MENU_OPTIONS or user_input.lower() in USER_MENU_OPTIONS


def valid_split_menu_choice(user_input):
    return user_input.upper() in SPLIT_MENU_OPTIONS or user_input.lower() in SPLIT_MENU_OPTIONS


def valid_vote_menu_choice(user_input):
    return user_input.upper() in VOTE_MENU_OPTIONS or user_input.lower() in VOTE_MENU_OPTIONS


########################################################################################################################
# Registration Methods
# User input for username, and password, all is validated
# Following user creation, register_user() sets a user instance sets this as the current user_instance


MIN_NAME_LENGTH = 3
MAX_NAME_LENGTH = 10
MIN_PASS_LENGTH = 3
MAX_PASS_LENGTH = 10


def valid_username(username):
    if len(username) < MIN_NAME_LENGTH or len(username) > MAX_NAME_LENGTH:  # Incorrect username lengths return false
        return False
    elif any(char.isdigit() for char in username):  # If the name contains a digit, return false
        return False
    else:
        return True


def user_exists(username):
    if users_file.file_search(username, 1) is True:  # Else, if that username already exists in file, return True
        return True  # (returning True is impassable in the While loop in splitthat_prog.py)
    else:
        return False


def valid_password(password):
    return len(password) >= MIN_PASS_LENGTH and len(password) <= MAX_PASS_LENGTH  # Wrong password lengths return false


def register_user(name, username, password):
    registered_user_instance = create_user_instance(name, username, password)  # New instance of user is created
    current_user_instance(registered_user_instance)  # Current user instance is set as this user instance
    save_progress()  # The information of this user instance is saved in the users_file


########################################################################################################################
# Login Methods
# After the user enters information in the login menu, the information is checked against what is the stored in the
# users_file.txt, via the Datafile. If correct, the users information is used to initialise instance variables in an
# instance of 'User' : instance variables, name, username, password, and previous_splits.
# This user_instance is then set as the current_user_instance

# Validation

def login_valid_username(username):
    if user_exists(username) is False or username == "":  # If user already exists, or nothing is entered
        return False


def login_valid_password(username, password):
    if users_file.file_search([username, password], [1, 2]) is False:  # incorrect combo of that username and password
        return False
    else:
        return True

# Login


def login(username):
    new_user_instance = load_user(username)  # A new user instance is created using the loaded user information
    current_user_instance(new_user_instance)  # This user instance is set as the current user instance


# When creating user instance, previous_splits by default is none, unless loading of a user with previous splits
def create_user_instance(name, username, password, previous_splits=None):
    new_user_instance = classes_module.User(name, username, password, previous_splits)
    return new_user_instance


def current_user_instance(new_user_instance):
    global user_instance  # The new user_instance is made global for access across the program
    user_instance = new_user_instance


def logout():
    current_user_instance(None)  # resets the user_instance back to None
    current_split_instance(None)  # as well as the split_instance back to none


########################################################################################################################
# Saving Methods
# The saving of information to the relevant datafiles takes place at various events of the application
# This is achieved via the following three methods. save_progress(), split_saving() and user_saving()


def save_progress():  # save_progress() is called from the splitthat_prog.py code

    user_saving()  # user_saving() is always called
    if split_instance is not None and user_instance is not None:  # whereas, if split and user instance is not None
        split_saving()  # Only then is the split_saving() method called to save the split in file
    else:
        pass


def user_saving():

    if split_instance is not None:  # If a split_instance is exist and, id_name is not in the user's previous_splits
        if split_instance.id_name not in user_instance.previous_splits:  # The id is added to attribute, previous_splits
            user_instance.add_split(split_instance.id_name)
        else:
            pass
    else:
        pass
    if user_instance.username not in users_file:  # If the username does not exist in file
        users_file.append_content(user_instance)  # i.e appending user info to the file takes place
    elif user_instance.username in users_file:  # Other is the username does exist
        old_user = users_file.get_file_line(user_instance.username)
        users_file.remove_content(old_user)  # The old user information in file is removed,
        users_file.append_content(user_instance)  # and the new user information replaces is
    else:
        pass


def split_saving():
    # isinstance() is used to check what object Split is an instance of, to direct saving to correct file.
    if isinstance(split_instance, classes_module.Bill):
        if split_instance.id_name not in bills_file:  # If the split id_name is not found in the corresponding file
            bills_file.append_content(split_instance)  # the file is appeneded (i.e a new split is created)
        elif split_instance.id_name in bills_file:   # Otherwise, if a previous split is being saved
            old_split = bills_file.get_file_line(split_instance.id_name)  # old split information is loaded from file
            bills_file.remove_content(old_split)                        # old split is removed from file
            bills_file.append_content(split_instance)                   # and the new split is appended
    if isinstance(split_instance, classes_module.Project):
        if split_instance.id_name not in projects_file:
            projects_file.append_content(split_instance)
        elif split_instance.id_name in projects_file:
            old_split = projects_file.get_file_line(split_instance.id_name)
            projects_file.remove_content(old_split)
            projects_file.append_content(split_instance)
    if isinstance(split_instance, classes_module.Rent):
        if split_instance.id_name not in rentals_file:
            rentals_file.append_content(split_instance)
        elif split_instance.id_name in rentals_file:
            old_split = rentals_file.get_file_line(split_instance.id_name)
            rentals_file.remove_content(old_split)
            rentals_file.append_content(split_instance)
    else:
        pass


########################################################################################################################
# Loading Methods
# When a user has previously saved data, the loading of information from the relevant data files takes place via
# the following loading methods.

# User Info Loading

def load_user(username):
    if users_file.get_file_line(username, 1) is not False:  # If the username exists in file, loading of user occurs
        user_info_line = users_file.get_file_line(username, 1)  # .get_file_line returns the entire user information
        user_info_list = user_info_line.split(classes_module.FILE_CONTENT_SEPARATOR)
        name = user_info_list[0]  # The user information string is then split by separator, "," into a list
        username = user_info_list[1]  # And corresponding pieces of information are given a list index number
        password = user_info_list[2]
        previous_splits = user_info_list[3]
        previous_splits = previous_splits.rstrip("\n")
        previous_splits = previous_splits.split(" ")
        if previous_splits == ['']:
            previous_splits = []
        else:
            pass
        new_user_instance = create_user_instance(name, username, password, previous_splits)
        return new_user_instance   # This information is used to create a user_instance, and this instance is returned
    else:
        return False  # If the user does not exist, False is returned


# Split Info Loading


def load_splits_info(split_identifier):  # the split id_name is used to search for a split in file
    if split_identifier in projects_file:  # Depending on where the id is found, a project/bill/rent is loaded
        loaded_split = load_project(split_identifier)  # by calling the relevant load_ method
    elif split_identifier in rentals_file:
        loaded_split = load_rental(split_identifier)
    elif split_identifier in bills_file:
        loaded_split = load_bill(split_identifier)
    else:
        loaded_split = False
    return loaded_split  # corresponding split is then returned


# Bill/Project/Rental information Loading
# Using the split id_name, the get_file_line() method gets the string line of information from the relevant file,
# and this string is split into a list, using seperator "FILE_CONTENT_SEPARATOR (",")
# A list is then returned - a string is set as index 0 containing what type of split it is - used for printing split
# type to the user

def load_bill(split_identifier):
    bill = bills_file.get_file_line(split_identifier)
    bill = bill.split(classes_module.FILE_CONTENT_SEPARATOR)
    id_name = bill[0]
    bill_name = bill[1]
    bill_price = bill[2]
    group_members = bill[3]
    votes = bill[4].rstrip("\n")  # '\n' escape character is stripped to prevent compounding incompatibility issues
    return ["Bill", id_name, bill_name, bill_price,  group_members, votes]


def load_project(split_identifier):
    project = projects_file.get_file_line(split_identifier)
    project = project.split(classes_module.FILE_CONTENT_SEPARATOR)
    id_name = project[0]
    project_name = project[1]
    group_members = project[2]
    votes = project[3].rstrip("\n")
    return ["Project Credit", id_name, project_name, group_members, votes]


def load_rental(split_identifier):
    rental = rentals_file.get_file_line(split_identifier)
    rental = rental.split(classes_module.FILE_CONTENT_SEPARATOR)
    id_name = rental[0]
    rental_name = rental[1]
    monthly_rent = rental[2]
    bedrooms = rental[3]
    group_members = rental[4]
    votes = rental[5].rstrip("\n")
    return ["Rental", id_name, rental_name, monthly_rent, bedrooms, group_members, votes]

# Creation and Setting of the Current Split Instance
# The returned split_info list from the previous load__bill/project/rental methods is then used to create a split
# instance in the following load_split_instance method, and then is set as the a global split instance via
# current_split_instance


def load_split_instance(split_info):
    if split_info[1] in bills_file:  # If the id_name is found in the bills file, this code is dispatched
        id_name = split_info[1]  # List indexes are set to corresponding attribute names
        bill_name = split_info[2]
        bill_price = split_info[3]
        group_members = split_info[4]
        votes = split_info[5]
        new_split_instance = create_bill_instance(bill_name, bill_price, group_members, votes, id_name)  # Instance of Bill created
    elif split_info[1] in projects_file:  # elif id_name in projects file, .. etc
        id_name = split_info[1]
        project_name = split_info[2]
        group_members = split_info[3]
        votes = split_info[4]
        new_split_instance = create_project_instance(project_name, group_members, votes, id_name)  # .. etc
    elif split_info[1] in rentals_file:
        id_name = split_info[1]
        rental_name = split_info[2]
        monthly_rent = split_info[3]
        bedrooms = split_info[4]
        group_members = split_info[5]
        votes = split_info[6]
        new_split_instance = create_rental_instance(rental_name, monthly_rent, bedrooms, group_members, votes, id_name)

    else:
        new_split_instance = None   # If the split_id was not found in any file, new_split_instance is None
    return new_split_instance  # new_split_instance is then returned


def current_split_instance(new_split_instance):  # new_split_instance is then set globally as the split_instance
    global split_instance
    split_instance = new_split_instance


########################################################################################################################
# Split Creation
# Validation of User Input
# The creation of splits all require validation of user input.
# Split rentals have extra validation to validate input of a sensible number of bedrooms, or the monthly price


# Valid Bill, Project and Rental creation
# Entering a split name outside of the valid name lengths returns false, or entering spaces or nothing returns false
# or entering a split name that already exists in file returns false
def valid_project_name(project_name):
    if len(project_name) < MIN_NAME_LENGTH or len(project_name) > MAX_NAME_LENGTH:
        return False  # Invalid n
    elif any(char.isdigit() for char in project_name):
        return False
    elif project_name in DISALLOWED_NAMES:  # DISALLOWED_NAMES contains ("" and " ") to prevent input of nothing
        return False
    elif projects_file.file_search(project_name, 1) is True:
        return False
    else:
        return True


def valid_bill_name(bill_name):
    if len(bill_name) < MIN_NAME_LENGTH or len(bill_name) > MAX_NAME_LENGTH:
        return False
    elif any(char.isdigit() for char in bill_name):
        return False
    elif bill_name in DISALLOWED_NAMES:
        return False
    elif bills_file.file_search(bill_name, 1) is True:
        return False
    else:
        return True


# Valid Rental Creation
MAX_BEDROOMS = 10
MIN_BEDROOMS = 2


def valid_rental_name(rental_name):
    if len(rental_name) < MIN_NAME_LENGTH or len(rental_name) > MAX_NAME_LENGTH:
        return False
    elif any(char.isdigit() for char in rental_name):
        return False
    elif rental_name in DISALLOWED_NAMES:
        return False
    elif rentals_file.file_search(rental_name, 1) is True:
        return False
    else:
        return True


def valid_monthly_rent(monthly_rent):
    if any(char.isalpha() for char in monthly_rent):  # if any character is not a digit, return false
        return False
    elif monthly_rent.find('.') != -1:  # if a decimal is entered, return false
        return False
    else:
        return True


def valid_bedrooms(bedrooms):
    if not any(char.isdigit() for char in bedrooms):
        return False
    elif bedrooms.find('.') != -1 or int(bedrooms) > MAX_BEDROOMS or int(bedrooms) < MIN_BEDROOMS:
        return False  # Entering a number of bedrooms outside of the valid number returns false
    else:
        return True


# Creation and Setting of the Current Split Instance
# Any newly created, or loaded split, is passed via the create__instance methods to initialised an instance of
# the corresponding Bill, Project, or Rent objects.


def create_project_instance(project_name, the_group, the_votes=None, id_name=None):
    new_project_instance = classes_module.Project(project_name, the_group, the_votes, id_name)
    return new_project_instance


def create_bill_instance(bill_name, bill_price, the_group, the_votes=None, id_name=None):
    new_bill_instance = classes_module.Bill(bill_name, bill_price, the_group, the_votes, id_name)
    return new_bill_instance


def create_rental_instance(rental_name, monthly_rent, bedrooms, the_group, the_votes=None, id_name=None):
    new_rental_instance = classes_module.Rent(rental_name, monthly_rent, bedrooms, the_group, the_votes, id_name)
    return new_rental_instance


########################################################################################################################
# Group Creation Methods
# Group creation is validated using the following methods, which prevent the user enter the same name twice in one group
# Or inapproriate names, or creating a group that is not between 3-5 in size
# Valid Group Members

MAX_TEAM_MEMBERS = 5
MIN_TEAM_MEMBERS = 3
MEMBER_NAMES_USED = []  # MEMBERS_NAMES_USED list grows to include members that are used in that group
DISALLOWED_NAMES = [" ", "", MEMBER_NAMES_USED]


def valid_member_name(name):
    if len(name) < MIN_NAME_LENGTH or len(name) > MAX_NAME_LENGTH:
        return False
    elif any(char.isdigit() for char in name):  # Entering a digit returns false
        return False
    elif name in DISALLOWED_NAMES:  # If name is entered twice, or just "" or " "
        return False
    else:
        MEMBER_NAMES_USED.append(name)
        return True


def correct_num_members(group_members_list):
    return len(group_members_list) >= MIN_TEAM_MEMBERS and len(group_members_list) <= MAX_TEAM_MEMBERS
    # returns false if the number of members in a group is outside of 3-5


########################################################################################################################
# Votes Methods
# When entering votes from, the following validation methods prevent the user from entering the same person for both
# the from_member and toward_member aspect of the vote. valid_vote() limits the vote to no greater than 100,
# and no less than 0.
# When voting, the 'from_member' refers to the member who making the vote, whilst 'towards_vote' is who that vote is
# against


# Vote Validation
MAX_VOTE = 100


def valid_from_member_vote(from_member):
    if from_member not in split_instance.group_members:  # if from_member is not in the group, return false
        return False


def valid_towards_member_vote(from_member, towards_member):
    if str(towards_member) == str(from_member):  # If from member is the same as towards member, return false
        return False
    elif towards_member not in split_instance.group_members:  # if towards member is not in the group, return false

        return False
    else:
        return True


def valid_vote(the_vote):
        if any(char.isalpha() for char in the_vote):  # if any character in the vote is a letter, return false
            return False
        elif the_vote.find('.') != -1:  # if the user enters a decimal, return false
            return False
        elif the_vote.isdigit and int(the_vote) > MAX_VOTE or int(the_vote) < 0:  # enter a vote above or below the
            return False                                                      # the minimum returns false
        else:
            return True


# Vote Creation
# The enter_vote() method takes the information inputted by the user, and uses it to update the Split instance
# variables, all_votes, via the split_instance.new_vote method
# get_members_votes is method utilised by the vote_menu to display who has voted, and what


def enter_vote(from_member, towards_member, the_vote):
    split_instance.new_vote(from_member, towards_member, the_vote)


def valid_scale(from_member):
    if split_instance.sum_votes(from_member) is False:
        pass
    else:
        if split_instance.sum_votes(from_member) != 100:
            return False
        else:
            return True


def rescale_votes(from_member):
    split_instance.rescale_vote(from_member)

# Deliverable 3 Update #
# Auto Vote allows automatic vote entering in the vote menu. This was originally used for convenient testing purposes,
# - it is useful for quickly passing the time-consuming phase of entering individual votes, speeding up the time it
# takes to reach the calculated contributions page
def auto_vote():
    all_votes = []
    full_votes = False
    for member in split_instance.group_members:
        vote_list = split_instance.get_vote(member).values()
        for vote in vote_list:
            all_votes.append(vote)
    if classes_module.NO_VOTE not in all_votes:
        full_votes = True
    vote = randomiser.randrange(1, 100)
    num_members = len(split_instance.group_members)
    from_member = ""
    toward_member = ""
    while from_member == toward_member or split_instance.get_vote(from_member, toward_member) != classes_module.NO_VOTE:
        from_number = randomiser.randrange(0, num_members)
        toward_number = randomiser.randrange(0, num_members)
        from_member = str(split_instance.group_members[from_number])
        toward_member = str(split_instance.group_members[toward_number])
        if full_votes is True and from_member != toward_member:
            split_instance.new_vote(from_member, toward_member, classes_module.NO_VOTE)
    else:
        split_instance.new_vote(from_member, toward_member, vote)
        vote_dict = split_instance.get_vote(from_member)
        if classes_module.NO_VOTE not in vote_dict.values():
           rescale_votes(from_member)
