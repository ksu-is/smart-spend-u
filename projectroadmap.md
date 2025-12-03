# Project Roadmap

### Sprint 2 Updates
- Begin building the Smart Spend U homepage.
- Add navbar and hero section.
- Document progress in GitHub.
# Smart Spend U — Project Roadmap

This roadmap outlines the development phases, milestones, and tasks completed during the creation of Smart Spend U for the IS Application Development course. The goal was to design a functional Python application that demonstrates object oriented design, data persistence, and user centered functionality.

---

## 🟨 Phase 1: Planning and Requirements Gathering

### Goals:
- Identify the core problem: students struggle with tracking spending.
- Define the minimum viable features:
  - Add transactions  
  - View transactions  
  - Budget summary  
  - Delete entries  
  - Persistent storage

### Decisions:
- Use **CSV** instead of SQL to simplify deployment.
- Use a **console based interface** similar to the structure of SmartSoccerTracker.
- Create a `Transaction` class to organize data logically.

---

## 🟩 Phase 2: Application Design

### System Structure:
- Main program loop with menu options.
- Separate functions for:
  - Adding income
  - Adding expenses
  - Listing all transactions
  - Filtering by category
  - Saving and loading data
  - Deleting transactions
  - Displaying summary calculations

### Data Model:
Each transaction contains:
- ID  
- Date  
- Type  
- Category  
- Description  
- Amount  

---

## 🟦 Phase 3: Development

### Tasks Completed:
- Built `Transaction` class with helper methods.
- Implemented CSV read and write functionality.
- Created input validation for dates, amounts, and categories.
- Developed summary calculations.
- Added menu system with clear numbered options.
- Implemented deletion functionality with confirmation.
- Added sorting by date and ID.
- Tested with sample data to ensure accuracy.

---

## 🟫 Phase 4: Testing and Refinement

### Testing Areas:
- Invalid user input (letters instead of numbers, wrong date format)
- Empty dataset behavior
- Correct sorting of transactions
- Correct balance and totals for income vs expenses
- CSV persistence when application is restarted

### Fixes:
- Improved error handling for corrupted CSV rows
- Standardized formatting of currency output
- Added confirmation before deletion
- Increased readability of table output

-



