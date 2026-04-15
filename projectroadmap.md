# Project Roadmap

## Sprint 1: Project Initiation
- [x] Create GitHub repository in `ksu-is` organization
- [x] Initialize README.md with project description
- [X] Search for related Python repositories for evaluation
- [X] Clone and attempt to run an existing codebase: https://github.com/kasmya/Inventory-Management-System 
- [X] Document findings from evaluated code: I first cloned the Kasmya repository, when I ran it in Visual Studio Code, it gave me 16 errors. Most of these were related to missing libraries ( mysql-connector ) and indention errors. After reading through the issues, I realized the code requires a pre-configured MySQL schema to run. I then tried to run code to download the needed libraries.
- [X] Document findings from Kasmya: I also realized that the code would not run properly because it was looking for a specific username and password which is accociated with the creator of this system / repository. 
      
## Sprint 2: Core Development
- [ ]Database Schema Design: Write the SQL script to create the collections table for specific fields. 
- [ ] Database Connection: Create a database.py file to establish connection between Python and MySQL.
- [ ] Basic GUI Shell: Set up the main Tkinter window with placeholder labels for "Specimen Name" and "Category."
- [ ] Input Functionality: Program the "Submit" button to print the input field data to the console (Terminal).
- [ ] Data Insertion: Write the Python logic to INSERT the user-inputted nature findings into the MySQL database.
- [ ] Search/View Feature: Implement a basic search function to query the database by specific categories.
- [ ] https://github.com/jonathandavidpollock/InventoryManagementSystem ( New inventory Management System Class )
- [ ] https://github.com/ibukun53/insect-documentation ( Specimen Documntation System )
