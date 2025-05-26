# Project Tracker Application

This is a simple web application that allows you to create projects, add tasks to them, and track your progress. All data is stored locally in your web browser.

## Features
- Create projects with a name and description.
- Add tasks with descriptions to each project.
- Mark tasks as "closed".
- View an activity diagram showing how many tasks were closed each day (similar to a GitHub contribution graph).
- Dark mode toggle for user interface preference.
- Data persistence using browser's local storage.

## How to Run
1.  Ensure you have Python 3 installed on your system.
2.  Clone or download the repository.
3.  Open a terminal and navigate to the root directory of this repository.
4.  Run the following command to start the webserver:
    ```bash
    python app.py
    ```
5.  Open your web browser and go to `http://localhost:8000` to use the application.

## How to Use
- **Creating a Project:**
  - Enter a project name and description in the respective input fields under "Create New Project".
  - Click the "Create Project" button. The new project will appear in the "Projects List".
- **Adding a Task:**
  - Once a project is created, it will show an input field for "Task description" and an "Add Task" button.
  - Type the task description and click "Add Task". The task will appear under that project.
- **Closing a Task:**
  - Each open task will have a "Close Task" button next to it.
  - Click this button to mark the task as completed. The task's status will update, and it will be recorded in the activity diagram.
- **Activity Diagram:**
  - The "Activity" section displays a visual representation of tasks closed per day.
- **Data Storage:**
  - All your projects and tasks are saved automatically in your browser's local storage. If you close the tab or browser and reopen it, your data will be reloaded.
