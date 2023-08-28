"""
estimate time: 30 minutes
actual time: 20 minutes
"""
from prac_07.project import Project


def main():
    projects = []

    # get project data from file
    in_file = open("project_data.csv", "r")
    # read title
    title = in_file.readline()
    # read project data

    for line in in_file:
        # split line into parts by tabs
        parts = line.strip().split("\t")
        # create project object and add to list
        projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))
    in_file.close()
    
    print(projects)

    


main()