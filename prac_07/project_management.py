"""
estimate time: 30 minutes
actual time: 20 minutes
"""
from prac_07.project import Project
import datetime
from operator import itemgetter

def main():
    projects = load_projects()

    while True:
        menu()
        choice = input(">>> ").upper()
        if choice == "L":
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_statistics(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid menu choice")


def menu():
    """display menu"""
    print("Menu:")
    print("L - Load projects")
    print("S - Save projects")
    print("D - Display statistics")
    print("F - Filter projects by date")
    print("A - Add new project")
    print("U - Update project")
    print("Q - Quit")


def load_projects(filename="projects.txt"):
    projects = []
    try:
        with open(filename, "r") as in_file:
            title = in_file.readline()  # Read and ignore the title line
            for line in in_file:
                parts = line.strip().split("\t")
                parts[1] = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
                parts[2] = int(parts[2])
                parts[3] = float(parts[3])
                parts[4] = int(parts[4])
                projects.append(Project(*parts))
            print("{} projects loaded from {}".format(len(projects), filename))
    except FileNotFoundError:
        print("File '{}' not found.".format(filename))
    return projects


def display_statistics(projects):
    """Display two groups: incomplete projects; completed projects, both sorted by priority"""
    completed_projects = []
    incomplete_projects = []
    for project in projects:
        if project.completed == 100:
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
    print("Incomplete projects:")
    incomplete_projects.sort()
    for i, project in enumerate(incomplete_projects):
        print("{}. {}".format(i + 1, project))
    print("Completed projects:")
    completed_projects.sort()
    for i, project in enumerate(completed_projects):
        print("{}. {}".format(i + 1, project))


def get_valid_filename():
    """Get a valid filename from the user"""
    while True:
        filename = input("Filename: ")
        if filename == "":
            print("Invalid filename")
        else:
            break
    return filename


def save_projects(projects):
    """Prompt the user for a filename to save projects to and save them"""
    filename = get_valid_filename()
    # open file for writing
    out_file = open(filename, "w")
    # write title
    out_file.write("Name\tStart date\tPriority\tCost Estimate\tCompletion Percentage\n")
    # write project data
    for project in projects:
        out_file.write("{}\t{}\t{}\t{}\t{}\n".format(project.name, project.start_date,
                                                      project.cost, project.priority, project.completed))
    out_file.close()
    print("{} projects saved to {}".format(len(projects), filename))


def filter_projects_by_date(projects):
    """Ask the user for a date and display only projects that start after that date, sorted by date"""
    while True:  # get valid date
        try:
            date = datetime.datetime.strptime(input("Start date: "), "%d/%m/%Y").date()
            break
        except ValueError:
            print("Invalid date")
    filtered_projects = []  # filter projects
    for project in projects:
        if project.start_date > date:
            filtered_projects.append(project)
    #sort projects by itemgetter 
    sorted_projects = sorted(filtered_projects, key=Project.start_date)
        
    print("Filtered projects:")
    for i, project in enumerate(filtered_projects):
        print("{}. {}".format(i + 1, project))



main()
# display_statistics(projects)
