# Project Roadmap

## Sprint 1: Project Initiation
- [x] Create GitHub repository in `ksu-is` organization
- [x] Initialize README.md with project description
- [X] Search for related Python repositories for evaluation
- [X] Clone and attempt to run an existing codebase: https://github.com/kasmya/Inventory-Management-System 
- [X] Document findings from evaluated code: I first cloned the Kasmya repository, when I ran it in Visual Studio Code, it gave me 16 errors. Most of these were related to missing libraries ( mysql-connector ) and indention errors. After reading through the issues, I realized the code requires a pre-configured MySQL schema to run. I then tried to run code to download the needed libraries.
- [X] Document findings from Kasmya: I also realized that the code would not run properly because it was looking for a specific username and password which is accociated with the creator of this system / repository. 
- [X] https://github.com/ibukun53/insect-documentation ( Specimen Documntation System )

      
## Sprint 2: Core Development 
- [X] Database Connection: Create a database.py file to establish connection between Python and MySQL.
- [X] Installed MySQL connector,updated, and ensured it is running.
- [X] Created aeon_registry database within MYSQL Workbench
- [X] Cloned KSU IS Aeon Registry repository onto mac to pull up to edit on VS Studio
- [X] Created test.txt file in VS Studio and saved to ensure bridge between github desktop/VS Studio. Pushed commits.
- [X] Created code within database.py and main.py
- [X] Matched password function in database.py with SQL workbench to run smoothly when promoted.
- [X] Set up initial TKinter GUI Layout and implement data insertion logic.
- [X] Ran code in new terminal, SQL window with data selection pulled up succsessfully.
- [X] Added green coloring to register finding button to make more visible.
- [X] Added another category box for specific item type.



