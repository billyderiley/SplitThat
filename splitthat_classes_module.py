# Title: Deliverable 3
# Course: COMP0015
# Author: Billy Riley
# Description: The splitthat_classes_module contains the various Objects that are used as instances throughout the
# application

import splitthat_presenter_module as presenter
import fileinput
import random

########################################################################################################################
# Classes Overview
#
# @Property - Getters and Setters are employed used @Property to manipulate the values of various instance attribute
# Special Methods:
# __str__ method: used to return a string representation of an objects instance
# __eq__  method: when equality operator '==' is used, two objects can be compared, e.g Persons object
# __contains__ method: when statement 'in' is used, the contents of a object can be checked for a specified content
# to return a boolean about the presence of that content, e.g DataFile object, self.datafile


########################################################################################################################
# Person object
# In the Group object, the instance attribute group_members stores instances of the Person object, initialised with
# instance variable person_name, corresponding to the group members name.
# User objects also inherit from Person, thereby inheriting the person_name instance attribute from the Person object.


class Person:
    def __init__(self, person_name):   # Person objects initialised with person_name
        self.person_name = person_name  # Instance attribute set to person_name from the init method argument

    def __str__(self):       # Special method - called when a Person is printed, or a str(Person) used
        return self.person_name  # self.person_name is returned

    def __eq__(self, other):       # Special method
        if str(other) == str(self):  # __str__ methods of each object are called, returned strings are compared
            return True    # if strings are equal, return True

    @property  # Getter used to get the values of this instance attribute
    def person_name(self):
            return self._person_name

    @person_name.setter  # Setter used to alter the values of this instance attribute, using arguments, 'name'
    def person_name(self, name):
            self._person_name = name


########################################################################################################################
# User object
# User objects inherits from Person, thereby inheriting the person_name instance attribute from the Person object.
# Then, extending Person's functionality to include other instance attrivute, username, password, and previously_splits
# When a user creates a registered user, they create an instance of User
#


class User(Person):
    def __init__(self, person_name, username, password, previous_splits=None):  # previous_splits are none by default
        super().__init__(person_name)  # Initialises the parent class. Person, instance, with person_name
        self.username = username  # User instance attributes are defined
        self.password = password
        if previous_splits is not None and isinstance(previous_splits, list):  # i.e User with previous_splits is loaded
            self.previous_splits = previous_splits
        else:  # else when previous_splits is none - when a user registers
                previous_splits = self.empty_split_list()
        self.previous_splits = previous_splits

    def __str__(self):  # When saving progress, __str__ method of User is called
        return f"{self.person_name},{self._username},{self._password},{self.previous_splits_str()}"

    @property  # Getter / Setters used to manage instance attribute
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        self._username = new_username

    @property  # Getter / Setters used to manage instance attribute
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property  # Getter / Setters used to manage instance attribute
    def previous_splits(self):
        return self._previous_splits

    @previous_splits.setter
    def previous_splits(self, previous_splits):
        self._previous_splits = previous_splits

    def previous_splits_str(self):  # Returns a simple str of previous split id_names for saving user progress
        split_string = ''
        for split in self.previous_splits:
            if split_string == '':
                split_string = f"{split}"
            else:
                split_string = f"{split_string} {split}"  # Indexes of previous_split list, joined into one string
        return split_string

    def add_split(self, id_name):  # Called when a user creates a new split
        if not isinstance(id_name, str):
            raise TypeError("Split ID is invalid")
        else:
            pass
        previous_splits = self.previous_splits
        previous_splits.append(id_name)
        self.previous_splits = previous_splits

    @staticmethod  # Creation of an empty_split_list is required when a new user registers
    def empty_split_list():
        previous_splits = []
        return previous_splits


########################################################################################################################
# Group object
# Group objects store the members of a group in a split, in instance attribute group_members. Objects, Split, and
# Types of Splits (Bill/Rent/Project) all inherit instances attributes and methods from Group
# Group does not have a __str__ method, due to inheriting child classes having priority of a redefined __str__ method


class Group:
    def __init__(self, group_members):

        if isinstance(group_members, str):  # Invoked when group members from saved splits in file
            group_members = group_members.split(" ")
        else:
            pass
        if isinstance(group_members, list):  # Invoked when group members returned from create_split() menu
            index = 0
            for member in group_members:  # Person objects initialised using member's name as person_name attribute
                if isinstance(member, Person):  # If the member is already a Person object
                    index += 1
                    pass   # Pass
                elif isinstance(member, str):  # Else, if not a Person object
                    group_members[index] = Person(member)  # Set current index number of list to become a Person object
                    index += 1
                else:  # For any other reason member is not a string or Person, raise an error
                    raise TypeError("A group with those members could not be created")
        self.group_members = group_members

    @property  # Getter / Setters used to manage instance attribute
    def group_members(self):
        return self._group_members

    @group_members.setter
    def group_members(self, group_members):
        self._group_members = group_members

    def group_str(self):  # group_str returns a neatly formatted string of group_members, i.e for saving a split in file
        group_string = ''
        for member in self.group_members:
            if group_string == '':
                group_string = f"{str(member)}"
            else:
                group_string = f"{group_string} {str(member)}"
        return group_string

    # (Feature will be implemented in future versions) - Group members can be added or removed from a group
    def add_member(self, new_member):
        the_group = self.group_members
        the_group.append(new_member)  # By appending the list group_members
        self.group_members = the_group

    def remove_member(self, removed_member):
        the_group = self.group_members
        the_group.remove(removed_member)
        self.group_members = the_group

########################################################################################################################
# Split object
# Split is inherited by objects, Bill, Rental and Project, therefore creation of an instance of these inherit
# the General methods and instance attributes of a Split, split_name, all_votes, and id_name.


NO_VOTE = "N"


class Split(Group):
    def _init__(self, split_name, all_votes=None, id_name=None):
        self.split_name = split_name
        if all_votes is None:  # i.e in the creation of a new split without any votes yet
            all_votes = self.create_empty_votes()  # Dictionary containing members names is returned ready for voting
        elif isinstance(all_votes, str):  # i.e when a split is loaded from file
            all_votes = self.votes_from_str(all_votes)  # loaded split's vote dictionary is returned by vote_from_str
        if id_name is None:  # i.e when a new split is created
            id_name = self.create_id_name()  # static method create_id_name creates a unique id_name
        self.all_votes = all_votes
        self.id_name = id_name

    @property
    def split_name(self):
        return self._split_name

    @split_name.setter
    def split_name(self, split_name):
        self._split_name = split_name

    @property  # Getter / Setters used to manage instance attribute
    def all_votes(self):
        return self._all_votes

    @all_votes.setter
    def all_votes(self, all_votes):
        self._all_votes = all_votes

    # When a user enters a new vote in vote_menu(), new_vote is called
    def new_vote(self, from_member, towards_member, the_vote=NO_VOTE):  # from_member, towards_member specified by user
        all_votes = self.all_votes
        all_votes[str(from_member)][str(towards_member)] = the_vote  # Entered member's vote updates the vote dictionary
        self.all_votes = all_votes

    ######################
    # Deliverable 3 Update
    ######################
    def rescale_vote(self, from_member):
        all_votes = self.all_votes
        sum_of_votes = self.sum_votes(from_member)
        while self.sum_votes(from_member) != 100:
            rescale_factor = sum_of_votes / 100
            for towards_member in all_votes[str(from_member)]:
                old_vote = int(all_votes[str(from_member)][str(towards_member)])
                new_vote = old_vote / rescale_factor
                new_vote = round(new_vote)
                self.new_vote(from_member, towards_member, str(new_vote))
            sum_of_votes = self.sum_votes(from_member)
            difference = 100 - sum_of_votes
            if difference <= 1 and sum_of_votes != 100:
                self.new_vote(from_member, towards_member, str(new_vote+difference))

    def sum_votes(self, from_member):
        all_votes = self.all_votes
        sum_of_votes = 0
        for towards_member in all_votes[str(from_member)]:
            if self.get_vote(from_member, towards_member) == NO_VOTE:
                return False
            else:
                vote = int(all_votes[str(from_member)][str(towards_member)])
                sum_of_votes = sum_of_votes + vote
        return sum_of_votes

    # When a print a vote from a user in vote_menu() get_vote is called
    def get_vote(self, from_member, towards_member=None):
        all_votes = self.all_votes
        if towards_member is not None:
            return all_votes[str(from_member)][str(towards_member)]
        else:
            return all_votes[str(from_member)]

    def vote_str(self):  # When a split is saved, vote_str returns a neat simple string of all votes
        all_votes = self.all_votes
        vote_string = ''
        for from_member in all_votes:  # iterate 'from_members' in all_votes dictionary
            from_members_votes = ''
            for towards_member in all_votes[from_member]:  # inside all_votes[from_member] iterate over towards_members
                the_vote = all_votes[from_member][towards_member]  # get the vote for each towards_member
                if from_members_votes == '':
                    from_members_votes = f"{towards_member} {the_vote}"  # add towards members, and vote, to a string
                    continue
                else:
                    from_members_votes = f"{from_members_votes} {towards_member} {the_vote}"
                    continue
            members_string = f"{from_member} {from_members_votes}"
            if vote_string == '':
                vote_string = f"{members_string}"
            else:
                vote_string = f"{vote_string} {members_string}"  # then add from_members votes, to overall vote string
        return vote_string  # return this entire vote string

    # When loading a split from file - votes_from_str interprets the votes, returning them as a dictionary
    # vote_from_str does so usung an algorithm where the number of group members, times 2, minus 1,
    # is equal to the number of iterated indexes in the split vote string, for 'from_member's' votes.
    #  This allows the application to to account for groups of any size greater than 3, oppose to setting a minimum
    #  and maximum limit to a group to say, 3 or 4 members
    def votes_from_str(self, votes_string):
        all_votes = self.create_empty_votes()  # First, empty vote dictionary is formed containing members
        votes_list = votes_string.split(" ")  # Loaded vote string is split into a list
        split_number = len(self.group_members)*2  # Necessary for vote string interpretation Algorithm
        content_indexes_per_member = split_number-1  # The total number of indexes per member
        indexes_read = 0  # Indexes iterated over is initially 0
        for str_content in votes_list:  # Iterate over content in votes_list
            indexes_read += 1   # Indexes iterated becomes 1
            if indexes_read == 1:    # First read index is the from_member
                from_member = str_content
                continue
            elif indexes_read % 2 == 0:  # Any even numbers indexes are the towards_member
                towards_member = str_content
                continue
            elif indexes_read % 2 != 0 and indexes_read != 1:  # Odd number indexes that are not 1 are the votes
                the_vote = str_content
                all_votes[from_member].update({towards_member: the_vote})  # dictionary is updated with this information
            else:
                pass
            if indexes_read == content_indexes_per_member:  # When a from_member reaches maximum number of indexes
                indexes_read = 0  # Reset read indexes back to 0
            else:
                pass
        return all_votes  # Newly formed vote dictionary is returned

    def create_empty_votes(self):  # Creates dictionary containing members, initially with NO_VOTE ("N")
        all_votes = {}
        for from_member in self.group_members:  # For each group member
            all_votes.update({str(from_member): {}})  # Add a key 'from_member' with a dictionary within the value pair
            for towards_member in self.group_members:
                if towards_member == from_member:  # To prevent members having a vote field for themselves
                    continue
                else:
                    all_votes[str(from_member)].update({str(towards_member): NO_VOTE})  # Update from_member's dict
        return all_votes                                         # with towards_member : NO_VOTE

    @property  # Getter / Setters used to manage instance attribute
    def id_name(self):
        return self._id_name

    @id_name.setter
    def id_name(self, new_id_name):
        self._id_name = new_id_name

    @staticmethod
    def create_id_name():  # Generates a unique integer, converted to a string, using random module
        id_number = random.randint(0, 10000)
        id_name = "ID" + str(id_number)
        while id_name in presenter.bills_file or id_name in presenter.projects_file \
                 or id_name in presenter.rentals_file:
            id_number = random.randint(0, 10000)
            id_name = "ID" + str(id_number)
        return id_name

######################
# Deliverable 3 Update

    # Individual members contributions are calculated from a combination of every other members votes about that member
    # contributions() either returns all contributions as a dictionary, or individual contributions for a specified
    # member
    def contributions(self, member=None):
        contributions = self.calculate_all_contributions()
        if member is not None: # If member specified
            return contributions[str(member)] # Return that members contribution
        else:
            return contributions # Else return everyone's contribution

    # calculate_all_contributions co-ordinates the various calculation methods, returning the contributions as a dict
    def calculate_all_contributions(self):
        contributions = {} # Initialise contributions dictionary
        total_contributions = 0
        for member in self.group_members:
            members_contribution = self.members_contribution(str(member)) # For each member, get their contribution
            if members_contribution is None: # If voting for all members is incomplete
                return None # return nothing
            else:
                contributions.update({str(member): members_contribution})  # Otherwise, update contributions dict
                total_contributions = total_contributions + members_contribution # Summate contribution total
        if total_contributions != 100: # If the contribution does not add up to 100
            contributions = self.rescale_contribution(total_contributions, contributions) # Rescale the contributions
        return contributions

    # rescale_contribution manipulates the contributions so they add up to 100
    @staticmethod
    def rescale_contribution(total_contributions, contributions):
        while total_contributions != 100: # While the total of contributions is not equal to 100, continue to rescale
            rescale_factor = total_contributions / 100 # division of total by 100 gives correct factor
            total_contributions = 0
            for member in contributions:
                contributions[member] = contributions[member] / rescale_factor # New member's contribution created
                contributions[member] = round(contributions[member]) # Contribution is rounded
                total_contributions = total_contributions + contributions[member] # New contributions are summated
            difference = 100 - total_contributions # Calculates any potential difference of contribution from 100
            if total_contributions != 100 and difference <= 1: # If the difference is less than 1
                contributions[member] = contributions[member]+difference # Add the difference to the member contribution
                total_contributions += difference # Add this difference to total_contributions to exit while loop
            elif difference == 0: # Otherwise if the difference is 0, pass
                pass
        return contributions # return the scaled contributions

    def members_contribution(self, member):
        compared_votes = self.compare_votes(str(member)) # Gets all the votes of from other members, minus votes from
        if compared_votes is False:                      #  this specified member
            return None # If a 'no vote' is found in votes, return nothing
        else:
            vote_ratios = self.calculate_vote_ratios(compared_votes, str(member))
            members_contribution = self.calculate_members_contribution(vote_ratios)
            members_contribution = round(members_contribution, 2) * 100
            members_contribution = int(members_contribution)
            return members_contribution

    def compare_votes(self, member):
        all_votes_towards = {}
        for from_member in self.group_members:
            if str(from_member) == member:
                pass
            else:
                all_votes_towards.update({str(from_member): {}})
                from_members_votes = self.get_vote(from_member)
                for towards_member in from_members_votes:
                    members_vote = from_members_votes[str(towards_member)]
                    if members_vote == NO_VOTE:
                        return False
                    else:
                        members_vote = float(members_vote)
                        all_votes_towards[str(from_member)].update({str(towards_member): members_vote})
        return all_votes_towards

    @staticmethod
    def calculate_vote_ratios(compared_votes, towards_member):
        vote_ratios = {}
        for from_member in compared_votes:
            if str(from_member) == str(towards_member):
                pass
            else:
                for other_members in compared_votes[str(from_member)]:
                    if str(other_members) == str(towards_member):
                        pass
                    else:
                        ratio = compared_votes[str(from_member)][str(other_members)] / compared_votes[str(from_member)][str(towards_member)]
                        vote_ratios.update({str(from_member): ratio})
        return vote_ratios

    @staticmethod
    def calculate_members_contribution(vote_ratios):
        summed_ratios = 0
        for members_vote_ratio in vote_ratios:
            summed_ratios = summed_ratios + vote_ratios[members_vote_ratio]
        members_contribution = 1 / (1 + summed_ratios)
        return members_contribution


########################################################################################################################
# Datafile
# Classes Project, Bill and Rental
# Instances of these objects representation the splits the user creates. All inherit from Split and Group objects,
# thereby having instance attributes of methods of these objects. But add additional functionality depending on what
# is being split. For example, Bill/Project/Rental have 'names', Rental objects have additional attributes, 'bedrooms'
# and 'monthly price


class Project(Split, Group):
    def __init__(self, project_name, group_members, all_votes=None, id_name=None):
        super().__init__(group_members)
        super()._init__(project_name, all_votes, id_name)
        self.project_name = project_name

    def __str__(self):  # When saving progress, __str__ method of Project is called to create a saveable string
        return f"{self.id_name},{self._project_name},{self.group_str()},{self.vote_str()}"

    @property  # Getter / Setters used to manage instance attribute
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        self._project_name = project_name

    def split_name(self):
        return self.project_name


class Bill(Split, Group):
    def __init__(self, bill_name, bill_price, group_members, all_votes=None, id_name=None):
        super().__init__(group_members)
        super()._init__(bill_name, all_votes, id_name)
        self.bill_name = bill_name
        self.bill_price = bill_price

    def __str__(self):  # When saving progress, __str__ method of Bill is called to create a saveable string
        return f"{self.id_name},{self._bill_name},{self._bill_price},{self.group_str()},{self.vote_str()}"

    @property  # Getter / Setters used to manage instance attribute
    def bill_name(self):
        return self._bill_name

    @bill_name.setter
    def bill_name(self, bill_name):
        self._bill_name = bill_name

    @property
    def bill_price(self):
        return self._bill_price

    @bill_price.setter
    def bill_price(self, bill_price):
        self._bill_price = bill_price

    def members_bill(self, member):
        members_bill = (int(self.bill_price) / 100) * self.contributions(member)
        members_bill = round(members_bill)
        return members_bill

    def split_name(self):
        return self.bill_name


class Rent(Split, Group):
    def __init__(self, rental_name, monthly_rent, bedrooms, group_members, all_votes=None,
                 id_name=None):
        super().__init__(group_members)
        super()._init__(rental_name, all_votes, id_name)
        self.rental_name = rental_name
        self.monthly_rent = monthly_rent
        self.bedrooms = bedrooms

    def __str__(self):  # When saving progress, __str__ method of Rental is called to create a saveable string
        return f"{self.id_name},{self._rental_name},{self._monthly_rent},{self._bedrooms}," \
               f"{self.group_str()},{self.vote_str()}"

    @property  # Getter / Setters used to manage instance attribute
    def rental_name(self):
        return self._rental_name

    @rental_name.setter
    def rental_name(self, rental_name):
        self._rental_name = rental_name

    def split_name(self):
        return self.rental_name

    @property  # Getter / Setters used to manage instance attribute
    def monthly_rent(self):
        return self._monthly_rent

    @monthly_rent.setter
    def monthly_rent(self, monthly_rent):
        self._monthly_rent = monthly_rent

    @property  # Getter / Setters used to manage instance attribute
    def bedrooms(self):
        return self._bedrooms

    @bedrooms.setter
    def bedrooms(self, bedrooms):
        self._bedrooms = bedrooms

    def rent_contribution(self, member):
        members_rent = (int(self.monthly_rent) / 100 ) * self.contributions(member)
        members_rent = round(members_rent)
        return members_rent


########################################################################################################################
# Datafile object
# Datafile instances are responsible for handling information in files that store user created information: for example
# users in the users_file, or bills in the bills_file. This is achieved by each file having its own Datafile instance
# where instance attribute, self.datafile, is set to open the corresponding file.
# Datafile object has other methods required for comparing stored information with user input, for example checking
# a username exists at login. Additionally, methods required for creating or removing information from these files,
# using append_content() and remove_content() respectively


FILE_CONTENT_SEPARATOR = ","


class DataFile:
    def __init__(self, data_file):
        self.data_file = data_file

    def __contains__(self, content):  # Special Method __contains__ called when checking if content is 'in' a file
        return self.file_search(content, search_index=None, return_content=False)

    # search_for corresponds to the content to be searched for
    # search_index correspond to the indexes of a line of information with will be searched - default is None
    # returned_content is False by default, if it were true, a succesfully content in a line will return that line
    # If argument, search_for, is a list - specific code for comparing file to a list is dispatched -Type-Based dispatch
    # Else If argument, search_for, is a str - specific code for comparing file to a string is dispatched
    def file_search(self, search_for, search_index=None, return_content=False):
        list_dispatch = False
        str_dispatch = False
        any_position = False
        if isinstance(search_for, Person) or isinstance(search_for, Bill) or isinstance(search_for, Rent) \
                or isinstance(search_for, Project):
            search_for = str(search_for)  # str method of the objects are called, allowing comparison of strings
        if isinstance(search_for, list) and isinstance(search_index, list):  # Type-based Dispatch
            list_dispatch = True
        elif isinstance(search_for, str) and isinstance(search_index, int):  # Type-based Dispatch
            str_dispatch = True
        elif isinstance(search_for, str) and search_index is None:
            any_position = True  # If search_index not specified, content in any_position is compared against the file
        file_content = fileinput.input(self._data_file)
        for line in file_content:  # For each line in the file
            if search_for == line or search_for == line.rstrip("\n"):  # If that line is already equal to the content
                file_content.close()                                # with or without escape character \n, return true
                return True
            else:
                line = line.rstrip("\n")  # \n escape characters are stripped from lines for accurate comparison
                split_list = line.split(FILE_CONTENT_SEPARATOR)  # Line is split, into split_list
                if any_position is True:  # Content to be searched for can be in any position of line
                    if search_for not in split_list:
                        continue
                    else:
                        file_content.close()
                        if return_content is True:
                            return line
                        else:
                            return True
                elif search_index is not None:  # If the content to be searched for has a specified position
                    if list_dispatch is True:  # Type-based Dispatch - list_dispatch
                        matching_indexes = 0  # Matching indexes initially set to 0
                        required_matches = len(search_for)  # Number of matching indexes required to return True
                        index = 0
                        for content in search_for:  # For each content in the search_for list
                            if content != split_list[search_index[index]]:
                                break
                            elif content == split_list[
                                search_index[index]]:  # If the content matches content in position[i]
                                matching_indexes += 1  # 1 matching indexes is added
                                if matching_indexes != required_matches:  # If the required matching indexes are met
                                    index += 1
                                    continue
                                elif matching_indexes == required_matches:  # If the required matching indexes are met
                                    file_content.close()
                                    if return_content is True:
                                        return line  # Return whole line
                                    else:
                                        return True  # or just return true

                    elif str_dispatch is True:  # Type-based Dispatch - str_dispatch
                        if search_for == split_list[search_index]:  # If a position specified and content matches
                            file_content.close()
                            if return_content is True:
                                return line
                            else:
                                return True
                        else:
                            continue
        file_content.close()  # Fileinput closed regardless of outcome of search
        return False  # If nothing is found, return false

    def get_file_line(self, content, position=None, get_line=True):
        contents = self.file_search(content, position, get_line)  # calls file_search with get_line True
        return contents                                        # to get the content of a searched line

    @property  # Getter / Setters used to manage instance attribute
    def data_file(self):  # set to one of the data files, users_file.txt, bills_file.txt etc
        return self._data_file

    @data_file.setter
    def data_file(self, data_file):
        self._data_file = data_file

    def append_content(self, new_content):  # Content will be added to the file at the end of the file
        new_content = f"{new_content}\n"
        with open(self.data_file, 'a') as content_appender:  # opened in 'append' mode
            content_appender.write(new_content)  # content is written

    def remove_content(self, removed_contents):  # If content needs to be removed
        new_datafile = ''
        removed_contents = f"{removed_contents}\n"
        file_content = fileinput.input(self._data_file)
        for line in file_content:  # All lines in the file are read
            if removed_contents == line:  # If the line has content that matches specified content, continue
                continue
            else:  # Otherwise, add the content to a new_datafile string
                if new_datafile == '':
                    new_datafile = line
                else:
                    new_datafile = f"{new_datafile}{line}"
        file_content.close()
        self.overwrite_content(new_datafile)  # Overwrite the file with new_data string, with removed content

    def overwrite_content(self, new_datafile):
        with open(self.data_file, 'w') as content_overwriter:  # File open in write mode - will overwrite the contents
                content_overwriter.write(new_datafile)
