# Title: Deliverable 3
# Course: COMP0015
# Author: Billy Riley
# Description: splitthat_prog contains the methods responsible for taking user input, and displaying information to
# the user

import splitthat_presenter_module as presenter

# Commonly used navigation options
NAV_QUIT = "Q To Return to Main Menu"
NAV_FORWARD = "X to Continue"
NAV_REJECT = "Z to Cancel"
USER_BACK = ["Q", "q"]           # The user can enter Q at most times if they wish to Quit to the Main Menu
USER_PROCEED = ["X", "x"]       # The user can enter X at most times if they wish to Continue in the Application
USER_REJECT = ["Z", "z"]        # If inputted information is no longer wanted, the user can enter Z to reject
USER_SCROLL = [""]     # When previous splits are loaded in split_menu, the user can tap enter to go load another splits

########################################################################################################################
# Main Menu
# Main_menu() is first screen that the user sees, allowing navigation to
# different areas of the application.
# The user can proceed to login, register, or proceed as a Guest (use without login/registration)


def main_menu():
    if presenter.user_instance is None:  # If the user is not logged in, this menu is shown (opposed to the user_menu)
        # User input will take the user to corresponding Menu pages
        print("\nWelcome to SplitThat. The Fair Splitting Application.")
        print("\n\nL To Login")
        print("R To Register")
        print("G To Proceed as a Guest")
        print("Q To Quit")
        print("Enter one of the following options: ")
        user_input = input()
        while presenter.valid_main_menu_choice(user_input) is False:  # User must enter one of the correct options to
            user_input = input("\nEnter one of the above options: ")  # pass the while loop -
        if user_input in ('L', 'l'):
            login_menu()
        elif user_input in ('R', 'r'):
            register_menu()
        elif user_input in ('G', 'g'):
            split_menu()
        elif user_input in ('Q', 'q'):
            quit()

    else:
        user_menu()  # Instead, if the user is  logged in, they are taken to the user_menu


########################################################################################################################
# User Menu
# If logged in, the user sees this menu, where they are given the option to view previously created splits, or logout
# if they wish to do so


def user_menu():
        print("\nWelcome to SplitThat. The Fair Splitting Application.")
        print("\n\nS To See Previous Splits")
        print("C To Create New Splits")
        print("L To Logout")
        print("Enter one of the above options: ")
        user_input = input()
        while presenter.valid_user_menu_choice(user_input) is False:
            user_input = input("Enter one of the above options: ")  # Invalid menu options cannot be entered
        if user_input in ('S', 's'):
            split_menu()
        elif user_input in ('C', 'c'):
            create_split()
        elif user_input in ('L', 'l'):
            presenter.logout()  # Logging out sets the user_instance back to None, and takes the user back to main menu
            main_menu()

########################################################################################################################
# Register Menu
# register_menu() is where the user inputs information required for registering themselves. Entering their name,
# username, and password, all of which are validated.
# Following user creation, the current user_instance is set to the newly registered user - and the user is taken to the
# user_menu


def register_menu():
    name = input(f"Enter your name\t\t\t\t\t{NAV_QUIT}")
    if name in USER_BACK:  # As mentioned previously, at most times the user can enter Q to return to main_menu
        main_menu()
    while presenter.valid_username(name) is False:  # If the name is too short/long/etc While loop is impassable
        print("Your name must contain only letters, and be a length between 3 and 10 characters")
        name = input(f"That name is invalid\t\t\t\t\t{NAV_QUIT}")
        if name in USER_BACK:
            main_menu()
    username = input(f"Choose your username\t\t\t\t\t{NAV_QUIT}")
    while presenter.valid_username(username) is False:  # If the username is wrong length - While loop is impassable
        print("Your name must contain only letters, and be a length between 3 and 10 characters")
        username = input(f"That username is invalid\t\t\t\t\t{NAV_QUIT}")
        if username in USER_BACK:
            main_menu()
    while presenter.user_exists(username) is True:  # If the user name already exists, etc While loop is impassable
        username = input(f"That username already exists, choose another\t\t\t\t\t{NAV_QUIT}")
        if username in USER_BACK:
            main_menu()
    password = input(f"Choose your password\t\t\t\t\t{NAV_QUIT}")
    while presenter.valid_password(password) is False:  # If password is wrong length - While loop is impassable
        print(f"Your password must be a length between 3 and 10 characters\t\t\t\t\t{NAV_QUIT}")
        password = input(f"That password is invalid\t\t\t\t\t{NAV_QUIT}")
        if password in USER_BACK:
            main_menu()
        else:
            pass
    presenter.register_user(name, username, password)  # User information is stored in the users_file, and a Global
    user_menu()  # instance of User is created in splitthat_presenter_module.py AKA 'presenter'
    # User is then taken to the user_menu


########################################################################################################################
# Login Menu
# During login, the information the user enters is validated against the information stored
# in the files: ‘users_file.txt.
# Registering, and logging in, both result in the creation of a global instance of the User object, named user_instances
# in the splitthat_presenter_module.py file,


def login_menu():
    username = input(f"Enter your username\t\t\t\t\t{NAV_QUIT}")
    if username in USER_BACK:
        main_menu()
    else:
        while presenter.user_exists(username) is False and username not in USER_BACK:  # False if user does not exist
            username = input(f"Hmmm... I cant find that username, try another\t\t\t\t\t{NAV_QUIT}")
            if username in USER_BACK:
                main_menu()
                break
        password = input(f"Enter your password\t\t\t\t\t{NAV_QUIT}")
        while presenter.login_valid_password(username, password) is False:  # False if username and password incorrect
            password = input(f"That password doesn't seem to be correct, try again\t\t\t\t\t{NAV_QUIT}")
            if password in USER_BACK:
                main_menu()
                break
        else:
            presenter.login(username)  # Else, if username and password are correct, user is logged in
            split_menu()


########################################################################################################################
# Split Menu
# A logged in user is able to see Splits they have made previously from the split_menu
# Alternatively, if the player is not logged in, user is automatically  directed to creating a ‘Split’


def split_menu():
    if presenter.user_instance is not None:  # user_instance is not none, i.e, if the user is logged in
        if presenter.user_instance.previous_splits == []:  # If the user has no previous splits
            print("\n\nYou haven't created any splits yet, would you like to create one?")
            print(f"\n{NAV_QUIT}")
            print(f"{NAV_FORWARD}")
            user_input = input("")
            while user_input not in USER_PROCEED and user_input not in USER_BACK:
                print(f"\n{NAV_QUIT}")
                print(f"{NAV_FORWARD}")  # User is given choice to proceed with creating a new split
                user_input = input("")
            if user_input in USER_PROCEED:  # If input in USER_PROCEED, they are taken to create_split
                create_split()
            elif user_input in USER_BACK:
                main_menu()
        elif presenter.user_instance.previous_splits != []:  # If the user has previous splits
            user_input = ''
            split_info = ''
            while user_input not in USER_PROCEED:  # While input is not in USER_PROCEED, user cannot pass
                for split_id in presenter.user_instance.previous_splits:  # For each split_id stored in user_instance
                    split_info = presenter.load_splits_info(split_id)      # split_info is loaded using that id
                    print(f"\nPrevious splits: ")                         # Previous splits are printed to the user
                    print(f"\nSplit Type is a: {split_info[0]}")  # Types of Split being, a Bill, a Project, or Rental
                    print(f"Named: {split_info[2]}")
                    if split_info[0] == "Rental":            # Rental splits, have extra information (bedrooms, price),
                        print(f"Team Members are: {split_info[5]}")  # therefore have more split_info indexes to print
                    elif split_info[0] == "Bill":            # Bill splits, have extra information (price),
                        print(f"Team Members are: {split_info[4]}")
                    else:
                        print(f"Team Members are: {split_info[3]}")
                    print(f"\n{NAV_QUIT}")
                    print("Z to Create a New Split")
                    print(f"{NAV_FORWARD} to Split")
                    print(f"<> To Load A Different Split Press Enter")
                    user_input = input()
                    if user_input in USER_PROCEED:
                        break
                    elif user_input in USER_SCROLL:  # User can load another split by pressing enter repetitively
                        continue  # which repeat load_splits_info with the next iteration of user stored split_ids
                    elif user_input in USER_REJECT:  # If the user wishes to create a split instead
                        create_split()              # they are taken to create_split
                        break                       # and the while loop is broken
                    elif user_input in USER_BACK:
                        main_menu()
                        break
            else:  # Other, when user_input is in USER_PROCEED, a new split_instance is created with the loaded info
                new_split_instance = presenter.load_split_instance(split_info)
                presenter.current_split_instance(new_split_instance)  # And that split is set as the current split
                if presenter.split_instance.contributions() is not None:
                    show_contributions()
                else:
                    vote_menu()  # User is then taken to the vote menu, where they can enter votes

    else:
        create_split()

########################################################################################################################
# Create Split
# Split creation consists of 3 primary parts, the selecting of a split type – either a Bill, or Project Credit,
# or a Rental, followed by the entering of split information such as the name,
# and the creation of a Group object instance,   -- again all information is validated


def create_split():
    print("\n\nB To Split a Bill")
    print("P To Split Project Contribution")
    print("R To Split Rent")
    user_input = input(f"Enter one of the above options: \t\t\t\t\t{NAV_QUIT}")
    if user_input in USER_BACK:
        main_menu()
    else:
        # Below, users are prompted to enter one of the following options to be lead to methods responsible for
        # creation of a Bill, Project Credit, or a Rental. All of which return a 'new_split'
        new_split = None  # The newly created split is initially set to none here
        while presenter.valid_split_menu_choice(user_input) is False:
            user_input = input(f"Enter a valid option\t\t\t\t\t{NAV_QUIT}")
        if user_input in ('B', 'b'):
            new_split = split_bill()
        elif user_input in ('P', 'p'):
            new_split = split_project_credit()
        elif user_input in ('R', 'r'):
            new_split = split_rent()
        if new_split is not None:
            print(f"\nSplit Name: {new_split.split_name}")  # Newly created split name is then printed
            try: # Try statement used in case split is a rent, in which case has extra attributes bedrooms, monthly_rent
                print(f"Bedrooms: {new_split.bedrooms}")
                print(f"Monthly Rent: {new_split.monthly_rent}")
            except AttributeError: # If split is not a rental, AttributeError is excepted
                pass
            finally: # Finally, always print the members names regardless
                member_counter = 1
                print("")
                for member in new_split.group_members:
                    print(f"Member {member_counter}: {member}")  # As well as the newly created members
                    member_counter += 1
            print(f"\n\n{NAV_QUIT}")
            print(f"{NAV_REJECT}")
            print(f"{NAV_FORWARD}")
            print("Does this look correct?")  # The user is prompted to confirm is this looks correct
            user_input = input()
            while user_input not in USER_BACK and user_input not in USER_PROCEED and user_input not in USER_REJECT:
                print(f"{NAV_QUIT}")
                print(f"{NAV_REJECT}")
                print(f"{NAV_FORWARD}")
                user_input = input()
            if user_input in USER_BACK:
                main_menu()
            elif user_input in USER_REJECT:  # If the user decides this is not correct, they can start again
                create_split()
            elif user_input in USER_PROCEED:  # Otherwise when user_input is in USER_PROCEED
                presenter.current_split_instance(new_split)  # The current split instance is set to the new split
                if presenter.user_instance is not None:  # If user is logged in
                    presenter.save_progress()  # then the split and split_id is saved in the splits and users files
                else:
                    pass
                vote_menu()  # Following split creation user is taken to the vote menu()
        else:
            pass

########################################################################################################################
# Split Bill, Split Project Credit, Split Rent
# User input during Split creation is validated. Splits names shorter than 3 characters, longer than 10 characters,
#  names containing digits, all return False during the While loop


def split_bill():
    bill_name = input(f"Enter the name of the bill you want to split \t\t\t\t\t{NAV_QUIT}")
    if bill_name in USER_BACK:
        main_menu()
    while presenter.valid_bill_name(bill_name) is False:
        bill_name = input(f"That name is not valid, enter another \t\t\t\t\t{NAV_QUIT}")
        if bill_name in USER_BACK:
            main_menu()
    bill_price = input(f"Enter the price of the bill\t\t\t\t\t{NAV_QUIT}")
    while bill_price == '' or presenter.valid_monthly_rent(bill_price) is False \
            or bill_price.isdigit() is False:
        bill_price = input(f"That bill price is not a valid input, enter another\t\t\t\t\t{NAV_QUIT}")
        if bill_price in USER_BACK:
            main_menu()
    the_group = create_group()
    bill_instance = presenter.create_bill_instance(bill_name, bill_price, the_group)
    return bill_instance


def split_project_credit():
    project_name = input(f"Enter the name of the project you want to split\t\t\t\t\t{NAV_QUIT}")
    if project_name in USER_BACK:
        main_menu()
    while presenter.valid_project_name(project_name) is False:
        project_name = input(f"That name is not valid, enter another\t\t\t\t\t{NAV_QUIT}")
        if project_name in USER_BACK:
            main_menu()
    the_group = create_group()
    project_instance = presenter.create_project_instance(project_name, the_group)
    return project_instance


# Rentals, having additional instance attributes, require additional validation to prevent user from entering less than
# 2 bedrooms, and no more than 10 (should they wish to rent a property with twice as many bedrooms as there are people)
# as well only being allowed to enter numbers for bedrooms and the monthly price
def split_rent():
    rental_name = input(f"Enter the name of the rental property you want to split rent with\t\t\t\t\t{NAV_QUIT}")
    if rental_name in USER_BACK:
        main_menu()
    while presenter.valid_rental_name(rental_name) is False:
        rental_name = input(f"That name is not valid, enter another\t\t\t\t\t{NAV_QUIT}")
        if rental_name in USER_BACK:
            main_menu()
    monthly_rent = input(f"Enter the monthly rental price\t\t\t\t\t{NAV_QUIT}")
    while monthly_rent == '' or presenter.valid_monthly_rent(monthly_rent) is False \
            or monthly_rent.isdigit() is False:
        monthly_rent = input(f"That rental price is not a valid input, enter another\t\t\t\t\t{NAV_QUIT}")
        if monthly_rent in USER_BACK:
            main_menu()
    bedrooms = input(f"Enter the number of bedrooms\t\t\t\t\t{NAV_QUIT}")
    while bedrooms == '' or presenter.valid_bedrooms(bedrooms) is False \
            or bedrooms.isdigit() is False:
        bedrooms = input(f"That number of bedrooms is invalid\t\t\t\t\t{NAV_QUIT}")
        if bedrooms in USER_BACK:
            main_menu()
    the_group = create_group()
    rental_instance = presenter.create_rental_instance(rental_name, monthly_rent, bedrooms, the_group)
    return rental_instance

########################################################################################################################
# Create Group
# When creating a split, create_group is called. If the user has previously made a split during that session,
# they are given the choice to reuse the same group as before. or alternatively create a new group.
# The number of members to be added is a choice between 3 and 5 members, but any other number of members does not pass
# validation, and prevents passing of a While loop


def create_group():
    if presenter.split_instance is not None:  # If a current split_instance already exists
        member_counter = 1
        for member in presenter.split_instance.group_members:  # members from this split are printed to the screen
            print(f"Member: {member_counter} {member}")
            member_counter += 1
        print(f"\n{NAV_REJECT}")
        print(f"{NAV_FORWARD}")  # And the user is given the option to reuse these group members
        print(f"Use the same group as before? (X to Continue) \t\t\t\t\t{NAV_QUIT}")
        user_input = input()
        while user_input not in USER_BACK and user_input not in USER_PROCEED and user_input not in USER_REJECT:
            print(f"\n\n{NAV_QUIT}")
            print(f"{NAV_REJECT}")
            print(f"{NAV_FORWARD}")
            user_input = input()
        if user_input in USER_BACK:
            main_menu()
        elif user_input in USER_REJECT:
            presenter.current_split_instance(None)  # If user rejects this, the split_instance is set to none,
            return create_group()  # create_group() is called again to return a new group list
        elif user_input in USER_PROCEED:
            the_group = presenter.split_instance.group_members  # Otherwise, the_group is set the previous split's group
            return the_group
    else:
        group_members = []  # Group member list is initialised
        print(f"Start adding members to the group. You can enter a total of "
              f"{presenter.MAX_TEAM_MEMBERS} members")  # The limit to the number of members is printed
        finished = False  # finished group creation is initialised to False
        while finished is not True:  # while finished is False, more members can be added
            member = input(f"\nEnter a group member's name\t\t\t\t\t{NAV_QUIT}")
            if member in USER_BACK:
                main_menu()
            while presenter.valid_member_name(member) is False and member != "":
                member = input(f"That name is not valid, please enter another\t\t\t\t\t{NAV_QUIT}")
                if member in USER_BACK:
                    main_menu()
            if member != '':
                group_members.append(member)  # After passing validation, that member is added to the group_member list
            else:
                pass
            if len(group_members) < presenter.MIN_TEAM_MEMBERS:  # If the number of group members is less than minimum
                finished = False  # Return False
            elif member != "" and len(group_members) < presenter.MAX_TEAM_MEMBERS:  # If the user has not finished
                finished = False  # adding members, whist they number of members is still less than the maximum
            elif len(group_members) == presenter.MAX_TEAM_MEMBERS:  # Otherwise, if the maximum is reached
                finished = True  # User is finished
            elif member == "" and len(group_members) <= presenter.MAX_TEAM_MEMBERS \
                    and len(group_members) >= presenter.MIN_TEAM_MEMBERS:  # The user is able to finish group creation
                finished = True                                           # when the group size is between 3-5 members
            else:
                finished = False
            continue
        return group_members  # The newly created group is then returned to the split creation proces

########################################################################################################################
# Vote Menu
# In vote_menu, a user or guest can view, or enter their votes of contribution.
# The process of entering a vote is such: they input the group member’s name that is voting,
# then the member they are voting for, and then the vote.
# All of which is validated - members cannot vote for themselves, or enter letters or nothing for a vote.


def vote_menu():
    print(f"\n\nHere you can enter the contribution votes from yourself, and other group members")
    if presenter.user_instance is not None:  # If the user logged in, they can view previous votes of a previous split
        print(f"You can also view the previous votes from other group members")
    for from_member in presenter.split_instance.group_members:  # For loop is used to get all group members
        print(f"\n{from_member}'s votes:")  # Then print the members name who the vote belongs to, 'from_member'
        for towards_member in presenter.split_instance.group_members:  # For loop used to get the towards_member
            if from_member == towards_member:  # If the from_member and towards_member are the same member, pass
                pass
            else:
                if presenter.split_instance.get_vote(from_member, towards_member) == "N":
                    print(
                        f"{towards_member}: ...")  # If no vote has been entered, "No Vote" is printed as the vote
                else:
                    print(f"{towards_member}: "
                          f"{presenter.split_instance.get_vote(from_member, towards_member)} "
                          f"// 100")  # The vote is always out of 100
    if presenter.split_instance.contributions() is not None:
        print(f"View Calculated Contributions? {NAV_FORWARD}")
    print(f"*A to Add an Automatic Vote*")
    from_member = input(f"Enter a Member's Name to Add/Update Their Votes\t\t\t\t\t{NAV_QUIT}")
    if from_member in USER_BACK:
        main_menu()
    elif from_member in USER_PROCEED and presenter.split_instance.contributions() is not None:
        show_contributions()
    elif from_member in ["A", "a"]:
        presenter.auto_vote()
        vote_menu()
    else:
        enter_vote(from_member)


def enter_vote(from_member):
    while presenter.valid_from_member_vote(from_member) is False and from_member not in USER_BACK:  # Invalid members
        from_member = input(f"That's not a valid member voting\t\t\t\t\t{NAV_QUIT}\t *(A to Auto Vote)*")              # returns false
        if from_member in USER_BACK:
            main_menu()
        elif from_member in ["A", "a"]:
            presenter.auto_vote()
            vote_menu()
    towards_member = input(f"Whose the vote for? \t\t\t\t\t{NAV_QUIT}")
    if towards_member in USER_BACK:
        vote_menu()
    while presenter.valid_towards_member_vote(from_member, towards_member) is False:  # Voting for yourself, or invalid
        towards_member = input(f"Thats not a valid member voting\t\t\t\t\t{NAV_QUIT}")  # members returns false
        if towards_member in USER_BACK:
            vote_menu()
    the_vote = input(f"Enter the vote, out of 100 \t\t\t\t\t{NAV_QUIT}")
    if the_vote in USER_BACK:
        vote_menu()
    while the_vote == '' or presenter.valid_vote(the_vote) is False or the_vote.isdigit() is False:  # Entering nothing
        the_vote = input(f"Thats not a valid vote\t\t\t\t\t{NAV_QUIT}")  # or anything that is not a digit returns false
        if the_vote in USER_BACK:
            vote_menu()
        else:
            pass
    print(f"\n{from_member}'s vote:")           # User is shown their newly enter voted, and asked to confirm it
    print(f"{towards_member}: {the_vote} // 100")
    print(f"\n{NAV_REJECT}")
    print(f"{NAV_FORWARD}")
    user_input = input(f"Confirm this correct by pressing Continue\t\t\t\t\t{NAV_QUIT}")
    while user_input not in USER_BACK and user_input not in USER_PROCEED and user_input not in USER_REJECT:
        print(f"{NAV_QUIT}")
        print(f"{NAV_REJECT}")
        print(f"{NAV_FORWARD}")
        user_input = input()
    if user_input in USER_BACK:
        main_menu()
    elif user_input in USER_REJECT:  # A user rejecting a vote will take them back to the vote menu
        vote_menu()
    elif user_input in USER_PROCEED:
        presenter.enter_vote(from_member, towards_member, the_vote)  # Otherwise the users vote is added to the
        ######################
        # Deliverable 3 Update
        ######################
        if presenter.valid_scale(from_member) is False:
            print(f"\n{NAV_REJECT}")
            print(f"{NAV_FORWARD}")
            print(f"The votes didn't add up to 100, would you like to rescale them?")
            user_input = input(f"Confirm this by pressing Continue, or Reject to reenter Votes\t\t\t\t\t{NAV_QUIT}")
            if user_input in USER_REJECT:  # A user rejecting a rescale will take them back to voting
                enter_vote(from_member)
            elif user_input in USER_PROCEED:
                presenter.rescale_votes(from_member)
        if presenter.user_instance is not None:  # users votes added to Split instance's all_votes instance variable
            presenter.save_progress()  # Again, if the user is logged in, this progress is saved in file
        else:
            pass
        vote_menu()

######################
# Deliverable 3 Update
########################################################################################################################
# Show Contributions
# In vote_menu, a user or guest can view, or enter their votes of contribution.


def show_contributions():
    print(f"\nBased on previous voting:")
    contributions = presenter.split_instance.contributions()
    try:
        print(f"Total Monthly Rent: £{presenter.split_instance.monthly_rent}")
    except AttributeError:
        pass
    try:
        print(f"Total Bill Price: £{presenter.split_instance.bill_price}")
    except AttributeError:
        pass
    for member in contributions:
        print(f"{member}'s contribution: {contributions[member]}%:  ", end="")
        try:
            print(f"£{presenter.split_instance.rent_contribution(member)}", end="")
        except AttributeError:
            pass
        try:
            print(f"£{presenter.split_instance.members_bill(member)}", end="")
        except AttributeError:
            pass
        finally:
            print("")
    user_input = input(f"View Votes? {NAV_FORWARD} \t\t{NAV_QUIT}")
    while user_input not in USER_BACK and user_input not in USER_PROCEED:
        user_input = input(f"{NAV_QUIT}")
    if user_input in USER_BACK:
        main_menu()
    elif user_input in USER_PROCEED:
        vote_menu()


def main():
    main_menu()


if __name__ == '__main__':
    main()
