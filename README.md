 <img width="451" alt="image" src="https://user-images.githubusercontent.com/74537403/126957352-fac147a9-062f-48e9-b459-c140fdce7056.png">

Throughout the design process, the PEP8 style guide was used

Brief instructions on how to run the program:
Run the program to the be taken to the main_menu() method. From there, you have the choice of registering an account as a new user, logging into a previously created account, or simply continue as a guest without registering.

Files:

<img width="229" alt="image" src="https://user-images.githubusercontent.com/74537403/126957547-2f59cf91-9b3b-4bf5-8024-ba1607bc11d4.png">

Splitthatprog.py is the interface the user interacts with. It is responsible for taking user input, allowing the user to engage with the controller splitthat_controller_module.py, which in turn engages with the splitthat_classes_module.py. splitthatprog.py contributes to the ‘View’ aspect of a Model, View, Presenter (MVP) code design format.


<img width="234" alt="image" src="https://user-images.githubusercontent.com/74537403/126957870-2d53fbd2-4792-46c7-ab22-c00a18048e9d.png">

As mentioned, splitthat_controller_module.py directly engages with the splitthat classes, found in the splitthat_classes.module.py file. It behaves as the “Presenter” in an MVP design.


<img width="233" alt="image" src="https://user-images.githubusercontent.com/74537403/126957997-db541ad6-7b50-4040-813c-b61ad9c01722.png">

Splitthat_classes.py file is where the majority of the object-oriented code lies. It allows the storage of information in the form of instance variables, in a few different classes
<img width="185" alt="image" src="https://user-images.githubusercontent.com/74537403/126958141-985f06a7-abab-421e-9e5c-fbe802d36871.png">
<img width="194" alt="image" src="https://user-images.githubusercontent.com/74537403/126958158-2361573a-437a-4b1f-9259-45e767b51f92.png">
<img width="191" alt="image" src="https://user-images.githubusercontent.com/74537403/126958171-cf4ffde8-6611-41fb-83f0-b4ac96a3a907.png">
<img width="188" alt="image" src="https://user-images.githubusercontent.com/74537403/126958179-cae04ad8-6ab2-4835-9e14-b7ca8c359d40.png">

    
The bills, rentals and project text files are required to store the ‘splits ‘created by the user, whilst the users file stores the user information. This allows logging in, saving of progress, and reloading of information where the user previously left the application


The Code:
<img width="170" alt="image" src="https://user-images.githubusercontent.com/74537403/126958390-51bdb57d-236c-4b7c-b4f6-5269edeae638.png">

Main_menu() is the first method to called and the first screen that the user sees, allowing navigation to different areas of the application. The user can proceed to login, register, or proceed as a Guest (use without login/registration)

 <img width="173" alt="image" src="https://user-images.githubusercontent.com/74537403/126958428-b4ca15fb-7d02-4264-ab92-26460d23267f.png">

Following login/registration, the user is taken to a user_menu() – where they can choose to view previous ‘Splits’ or create a new ‘Split’
(In this application, ‘Splits’ a term that includes the splitting of a Bill, Project Credit, or Monthly Rent, all of which are possible with the Splitthat application)

<img width="205" alt="image" src="https://user-images.githubusercontent.com/74537403/126958473-5fc37624-fcef-4e6a-a2d9-282ea6ff9f6b.png">

Register_menu() is where the user inputs information required for registering themselves. Entering their name, username, and password, all of which are validated.

The user is able to login in login_menu(), the information they enter is validated against the information stored in the files: ‘users_file.txt. Registering, and logging in, both result in the creation of a users_instance, an instance of the User object <img width="146" alt="image" src="https://user-images.githubusercontent.com/74537403/126958913-f2371815-5e54-4c36-8d5c-b2fd1391981b.png">, found in the splitthat_classes module.py file.  
The user is able to login in login_menu(), the information they enter is validated against the information stored in the files: ‘users_file.txt. Registering, and logging in, both result in the creation of a users_instance, an instance of the User object , found in the splitthat_classes module.py file.  

<img width="191" alt="image" src="https://user-images.githubusercontent.com/74537403/126958955-57db3113-13ec-4f64-b8c8-27e1231774e3.png">

If the user is logged in (splitthat.presenter_module.user_instance is not None) <img width="382" alt="image" src="https://user-images.githubusercontent.com/74537403/126959072-92a08c0e-60ca-45ea-b492-65c6c1bb204c.png">, the user is able to see Splits they have made previously, even from a previous session. Alternatively, if the player is not logged in, they are directed to creating a ‘Split’ automatically

 
<img width="199" alt="image" src="https://user-images.githubusercontent.com/74537403/126959182-9ccce3f7-51ba-496c-8bdd-f379eba64937.png">

In create_split() users are able to begin the split creation process. Split creation consists of 3 primary parts, the selecting of a split type – either a Bill, or Project Credit, or a Rental, the entering of split information such as the name, and the creation of a Group member list. Following split creation, a split instance is created - of which is an instance of either Bill object, Project object, or Rental object.
<img width="144" alt="image" src="https://user-images.githubusercontent.com/74537403/126959638-d7c51fc0-c41d-4d07-9c98-35d9383d4fff.png">
<img width="192" alt="image" src="https://user-images.githubusercontent.com/74537403/126959650-b5461649-1ccb-44c0-ab9b-b559ad9975c2.png">
<img width="148" alt="image" src="https://user-images.githubusercontent.com/74537403/126959664-b39d71a5-b266-41c3-ae0f-6ceeb8ff039c.png">

                   
<img width="168" alt="image" src="https://user-images.githubusercontent.com/74537403/126959781-842c37fe-32c3-4e42-a7a5-8507c380f777.png">
<img width="289" alt="image" src="https://user-images.githubusercontent.com/74537403/126959873-b73efeea-4c84-4f70-a232-c6d4efd64abf.png">


After creating a split, a user or guest can interact with the vote_menu() page and enter their votes of contribution, and view the contributions via the show_contributions() page. Instruction: input the group member’s name that is voting, then the member they are voting for, and then the vote number (which will be validated)
<img width="453" alt="image" src="https://user-images.githubusercontent.com/74537403/126959815-da6826ea-11f3-41ef-882f-26fbe8feb49a.png">

 <img width="451" alt="image" src="https://user-images.githubusercontent.com/74537403/126960487-5cab022f-535f-456f-8225-628cc4544cef.png">
 <img width="171" alt="image" src="https://user-images.githubusercontent.com/74537403/126960461-53a55acd-f4cb-4083-b5e0-e00cdfdf8b7b.png">

 <img width="387" alt="image" src="https://user-images.githubusercontent.com/74537403/126960366-db7d4d53-e8f5-424a-857c-511ae45dd7ea.png">

In the initial running of splitthat_presenter_module.py, instances of object Datafile are created here, with related datafiles being opened with a ‘Try/Except’ clause and taking the related datafiles as arguments. Instances of objects User and Split are set to None initially here, until are required for use. All instances are defined as Global objects for wide use across the program
 



 
 
<img width="216" alt="image" src="https://user-images.githubusercontent.com/74537403/126960603-21bab8ca-ca6f-4424-8eb3-694735162758.png">
<img width="437" alt="image" src="https://user-images.githubusercontent.com/74537403/126960614-d3349e3f-3f23-49c8-b6ee-e6616523cc5c.png">

All of the def valid__menu_choice methods serve to validate the input from the user at various menu screens, preventing impossible navigation in the program
<img width="451" alt="image" src="https://user-images.githubusercontent.com/74537403/126960630-c5dd6d2e-9c47-44ba-b3b2-3584b69af779.png">

<img width="162" alt="image" src="https://user-images.githubusercontent.com/74537403/126960648-738789d7-70d9-4be9-94e5-67781f718972.png">

If the user wishes to login as a previous user, they do so via the login_menu 
<img width="247" alt="image" src="https://user-images.githubusercontent.com/74537403/126960665-35104024-f27f-4b7f-971a-76e85ee26771.png">
<img width="324" alt="image" src="https://user-images.githubusercontent.com/74537403/126960672-f7508978-9a6e-42fe-a952-94233d840d7a.png">
 
The information the user inputs is validated for factors such as whether that user exists, and if the username and password are a correct match. 

<img width="155" alt="image" src="https://user-images.githubusercontent.com/74537403/126960686-589651c7-2536-4e69-b41f-bb70d4702f8a.png">
<img width="451" alt="image" src="https://user-images.githubusercontent.com/74537403/126960700-43427a58-0932-47d3-921f-f97f78df6a47.png">
 
If successful, the information stored in the users_file is drawn, and an instance of the User object is created with instance variables set to the information the user.
<img width="333" alt="image" src="https://user-images.githubusercontent.com/74537403/126960767-69bb9dd8-277e-49e4-bab8-5a9c77261f03.png">
This user_instance is then set to the become current_user_instance. 
 
<img width="88" alt="image" src="https://user-images.githubusercontent.com/74537403/126960812-f2b0cce9-2eda-497d-89c0-efca96c6390c.png">

If the user chooses to logout, they do so via logout():, which sets the user_instance back to None

<img width="262" alt="image" src="https://user-images.githubusercontent.com/74537403/126960840-c98744f3-bb45-4cf1-bac9-3827150a4c74.png">

When registering, the information the user enters is validated. They are unable to enter a username that already exists, or an inappropriate name length or password, or a name containing numbers. 
<img width="213" alt="image" src="https://user-images.githubusercontent.com/74537403/126960876-db9f7fe5-699f-402c-8f4b-0960c072b8b5.png">
<img width="183" alt="image" src="https://user-images.githubusercontent.com/74537403/126960886-e4f16843-d05f-4762-a882-2d7e87598d46.png">
<img width="203" alt="image" src="https://user-images.githubusercontent.com/74537403/126960900-539ac323-379e-46bd-87bf-a70adce82d51.png">
<img width="318" alt="image" src="https://user-images.githubusercontent.com/74537403/126960978-c796eb8e-4890-4c7c-af1a-538e7f8cbcd0.png">

If successful, an instance of User object is created with the corresponding information, and is set to the become current_user_instance, as with logging in.

<img width="199" alt="image" src="https://user-images.githubusercontent.com/74537403/126961002-6bef3d42-7bb0-474e-a806-37a1b86fef86.png">
<img width="146" alt="image" src="https://user-images.githubusercontent.com/74537403/126961049-72c08680-c28f-4f6e-a3a9-bed04ddbed5e.png">
<img width="133" alt="image" src="https://user-images.githubusercontent.com/74537403/126961075-96293a20-4499-4da7-b995-c4585f53eae3.png">
<img width="139" alt="image" src="https://user-images.githubusercontent.com/74537403/126961081-9415bba5-d486-4b8a-b539-530c96cd0643.png">

The saving of information to the relevant datafiles takes place at various events of the application -- for example, after registering as a user, or creating a split whilst being logged in. 
This is achieved via the following three methods. save_progress() is a more general method which deciphers whether an instance of Split object is present, and therefore needs to be saved via split_saving(). Whereas user_saving() is always called upon ( it is implied that only a registered user can save progress)
 
<img width="207" alt="image" src="https://user-images.githubusercontent.com/74537403/126961118-d1910673-8abb-443d-8706-f27560d22708.png">
<img width="210" alt="image" src="https://user-images.githubusercontent.com/74537403/126961136-bdf2375a-e021-49a0-b2ef-107cbe88645d.png">

If the user has previously saved data, the loading of information from the relevant data files takes place via the loading methods. Information is relayed from the DataFile object instances, to the user regarding their previously stored user and split information
  
<img width="355" alt="image" src="https://user-images.githubusercontent.com/74537403/126961164-9ac3f9f0-02b9-4312-925c-60b08dc62fa7.png">
<img width="285" alt="image" src="https://user-images.githubusercontent.com/74537403/126961173-16595bbc-e09e-4a3b-978d-f4b26bae271b.png">
<img width="248" alt="image" src="https://user-images.githubusercontent.com/74537403/126961182-a163e728-7189-4aea-8475-fe7a0af6ad7d.png">
<img width="280" alt="image" src="https://user-images.githubusercontent.com/74537403/126961192-4fa29029-5b6a-49af-970f-fb5843def680.png">
 
Split information loading is initiated by the load_splits_info method, which calls the corresponding load_bill, load_project, or load_rental_methods - depending on which file contains the associated split id_name - to get the line of text in the data file

<img width="300" alt="image" src="https://user-images.githubusercontent.com/74537403/126961230-19dfaa52-df8e-4c76-9abd-88abbddb7a77.png">

load_split_instance then takes split_info list as an argument, and the relevent create_split_instance method is called 

<img width="366" alt="image" src="https://user-images.githubusercontent.com/74537403/126961246-20028b5b-caf8-4b65-a112-1a5fa362d73f.png">

The current instance of split is then set to newly created/or loaded split instance
 
<img width="240" alt="image" src="https://user-images.githubusercontent.com/74537403/126961268-a202e8a3-8c59-4b91-af95-b8e74a895e8f.png">

<img width="255" alt="image" src="https://user-images.githubusercontent.com/74537403/126961314-d611aa53-61d5-46d3-baad-b22041dbf772.png">
<img width="506" alt="image" src="https://user-images.githubusercontent.com/74537403/126961323-a0550017-e716-4d4d-9bc5-af4f4088c47a.png">

The creation of splits include a Bill, Project, and a Rental. They all follow the same format of code as described above for a Project. The name the user enters is validated (cannot enter that name if that Split name already exists)
An instance of that split is then create via the create___instance (name, the_group, the_votes, id_name, etc) method 
*A rental is a special case, having extra validation to validate a sensible number of bedrooms inputted by the user, or the monthly rental price
  
<img width="327" alt="image" src="https://user-images.githubusercontent.com/74537403/126961376-77e3a755-c13d-418a-a6ae-46520f8b31ad.png">
<img width="339" alt="image" src="https://user-images.githubusercontent.com/74537403/126961388-17f1379f-ff1d-4352-a71b-54bdc749d3e1.png">
<img width="205" alt="image" src="https://user-images.githubusercontent.com/74537403/126961413-32acbd58-b6c4-4c3e-a125-acde92b2d4f6.png">
<img width="313" alt="image" src="https://user-images.githubusercontent.com/74537403/126961418-af855e96-c7e0-4f57-a30f-42f43537efe9.png">
<img width="261" alt="image" src="https://user-images.githubusercontent.com/74537403/126961432-7241a74f-6a3d-46b0-b11c-c86a64ce6070.png">

During the creation of a split, the user is asked to enter the group members. Valid of the names entered takes place in the validation methods: 
valid_member_name(name)     - returns False when the names are an invalid length, and if the name has already been entered once.
correct_num_memvers(group_member_list) -  returns False is the number of members is equal to the maximum (default of 5), or if there are less members than the minimum
After passing validation, an instance of the Group object is created,  of which is used to create another Group storing the group members in an instance variable of the relevant Split object

<img width="193" alt="image" src="https://user-images.githubusercontent.com/74537403/126961462-1f9d0850-fd0c-483a-afaf-55679ced1e7c.png">
<img width="117" alt="image" src="https://user-images.githubusercontent.com/74537403/126961479-16e140e2-8614-467f-9281-c4d3a27b72b1.png">
<img width="290" alt="image" src="https://user-images.githubusercontent.com/74537403/126961488-8f10c0c2-c2f6-47f8-9662-8260a4d2c01e.png">
<img width="416" alt="image" src="https://user-images.githubusercontent.com/74537403/126961493-d14f633c-d058-4b54-9eac-9054b7f1c250.png">
<img width="183" alt="image" src="https://user-images.githubusercontent.com/74537403/126961500-3cbea3e5-a132-41da-a9d0-c7ed72ec9bab.png">

When entering votes from, validations methods prevent the user from entering the same person for both the from_member and toward_member aspect of the vote. valid_vote() limits the vote to no greater than 100, and no less than 0.

<img width="385" alt="image" src="https://user-images.githubusercontent.com/74537403/126961544-49d6692a-051c-4cea-b327-29a7649a6f13.png">

The enter_vote() method takes the information inputted by the user, and uses it to update the Split instance variables, all_votes, via the split_instance.new_vote method
<img width="264" alt="image" src="https://user-images.githubusercontent.com/74537403/126961572-ba55717e-9c92-4f30-89d4-114e5efe6eaf.png">
<img width="253" alt="image" src="https://user-images.githubusercontent.com/74537403/126961574-e14292da-32db-43a8-a0e4-df55e9bdd3e6.png">

<img width="420" alt="image" src="https://user-images.githubusercontent.com/74537403/126961592-e4761114-d134-46b2-b093-608a3028346c.png">
<img width="178" alt="image" src="https://user-images.githubusercontent.com/74537403/126961603-20b6970f-7806-40e1-a6eb-1d545b2abc30.png">
<img width="247" alt="image" src="https://user-images.githubusercontent.com/74537403/126961616-2bd18cea-039f-4e18-bc72-e34fd722a057.png">

‘All group members are instances of the Person object – User objects also inherit from Person, thereby including the person_name in the User object

<img width="218" alt="image" src="https://user-images.githubusercontent.com/74537403/126961638-a3ee310d-28f1-4457-ae0d-c91e53fb7582.png">
<img width="497" alt="image" src="https://user-images.githubusercontent.com/74537403/126961647-2960914b-158f-4e35-95fb-0799e7bee3d9.png">
<img width="222" alt="image" src="https://user-images.githubusercontent.com/74537403/126961660-dca4d1c9-a0ca-4cb1-aa36-d7b44be7d5fe.png">
<img width="278" alt="image" src="https://user-images.githubusercontent.com/74537403/126961663-297ea123-ce03-41e0-b1a7-bf0d8f017993.png">

As previously mentioned, User inherits the person name instance variable from the Person object.
User extends the functionality of Person by including instance variables such as username, and password, and previous splits.
Initialisation of the User object can either take place at registration or loading of a user from the users file. 

<img width="197" alt="image" src="https://user-images.githubusercontent.com/74537403/126961698-d99b21b1-7e02-4675-a2c6-e1b152d6863d.png">

User has the custom method __str__ which returns a neat, save-friendly format of the User information – allowing efficient loading and saving of information. 

<img width="162" alt="image" src="https://user-images.githubusercontent.com/74537403/126961730-6c673f5a-0c75-4f69-990f-7658a9bc7e77.png">
<img width="270" alt="image" src="https://user-images.githubusercontent.com/74537403/126961752-66fb5cec-c75f-4b41-a45d-38e042f714a3.png">
<img width="261" alt="image" src="https://user-images.githubusercontent.com/74537403/126961766-9afc88ea-9c4d-46cf-b5dc-b7cf4a4e1ca0.png">

The group members are stored in the instance variable group members, in an instance of the object Group.
Group is inherited by Split, and Bill, Rent and Project objects, these child classes extending the functionality of Group. 

<img width="265" alt="image" src="https://user-images.githubusercontent.com/74537403/126961822-5350c5f5-1a45-4c14-b7bc-f991c4ab0857.png"> 
<img width="451" alt="image" src="https://user-images.githubusercontent.com/74537403/126961853-d8f2e4c1-95ca-4ce2-8e75-ef17a0f86706.png">
<img width="257" alt="image" src="https://user-images.githubusercontent.com/74537403/126961860-cd7fd1ff-e305-49fc-a1a4-53f1045f80ff.png">

The Split object stores the data of votes in the instance variable all_votes. 
All Split instances also have attributes:
-	 split_name, which isdefined using the super().__init__ constructor from childclasses, Rent, Bill, Project
-	all_votes, which is a dictionary containing each member as a key, with the value pairs set to nested dictionaries, each with a ‘towards_member’ as a key, and a vote as the value pair
-	id_name, which is unique to that split (as validated by a check of all previous id_names stored in the Datafiles) permits easy saving and loading of splits, based upon their id.

<img width="319" alt="image" src="https://user-images.githubusercontent.com/74537403/126962029-68c05c39-6d41-4421-8aaf-23bafdacbb31.png">
<img width="276" alt="image" src="https://user-images.githubusercontent.com/74537403/126962033-363bc1a6-af75-4773-840b-6076ee424f9c.png">
<img width="333" alt="image" src="https://user-images.githubusercontent.com/74537403/126962045-98e24824-cd5f-4956-ab91-0df5859c7021.png">
Bill and Project and Rental objects are similar in construction - all three consist of a name. Additionally, they inherit group members from its parent class Group, as well as inheriting all votes from parent class Split.

<img width="197" alt="image" src="https://user-images.githubusercontent.com/74537403/126962098-a80e86f1-8057-46ea-bfdf-abe0a85fa4d8.png">

All Rent, Bill and Project objects all have the custom method __str__ which returns a neat, save-friendly format of the Split information – allowing efficient loading and saving of information. 

<img width="207" alt="image" src="https://user-images.githubusercontent.com/74537403/126962136-674495fb-eeab-4250-a446-128c4aa30727.png">

As previously mentioned, the DataFile object is implied in the handling of information stored in its instance variable, datafile, which is set to open, and take data from various text files - users_file.txt, bills_file.txt, projects_file.txt, and rentals_file.txt

Datafile is more complex in its design than the other objects - having methods involved in the searching of multiple pieces of information per line of text in each file (for example, 
when checking an entered username and password match at login) 

<img width="264" alt="image" src="https://user-images.githubusercontent.com/74537403/126962190-4298c44d-0434-4bf7-8846-8a4edb9ca329.png">

Datafile also contains a custom __contains__ method, which allows the use of the “in” operator at various points of code relating to the datafiles. 
For example: 
if id_name in bills_file:


