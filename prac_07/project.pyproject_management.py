"""
Time Estimate: 10-12 hours
"""

import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.percent_complete}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def update_progress(self, percent_complete):
        self.percent_complete = percent_complete

    def update_priority(self, priority):
        self.priority = priority


class ProjectManagementSystem:
    def __init__(self):
        self.projects = []

    def load_projects(self, filename):
        with open(filename, 'r') as file:
            next(file)  # Skip header
            for line in file:
                data = line.strip().split('\t')
                name, start_date, priority, cost_estimate, percent_complete = data
                project = Project(name, start_date, int(priority), float(cost_estimate), int(percent_complete))
                self.projects.append(project)
        print(f"Loaded {len(self.projects)} projects from {filename}")

    def save_projects(self, filename):
        with open(filename, 'w') as file:
            file.write("Name\tStart Date\tPriority\tCost Estimate\tPercent Complete\n")
            for project in self.projects:
                file.write(
                    f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.percent_complete}\n")

    def display_projects(self):
        incomplete_projects = [project for project in self.projects if project.percent_complete < 100]
        completed_projects = [project for project in self.projects if project.percent_complete == 100]
        incomplete_projects.sort(key=lambda x: x.priority)
        completed_projects.sort(key=lambda x: x.priority)

        print("Incomplete projects:")
        for project in incomplete_projects:
            print(f"  {project}")
        print("Completed projects:")
        for project in completed_projects:
            print(f"  {project}")

    def filter_projects_by_date(self, date):
        filtered_projects = [project for project in self.projects if project.start_date > date]
        filtered_projects.sort(key=lambda x: datetime.datetime.strptime(x.start_date, "%d/%m/%Y"))

        print(f"Projects starting after {date}:")
        for project in filtered_projects:
            print(f"  {project}")

    def add_new_project(self):
        name = input("Name: ")
        start_date = input("Start date (dd/mm/yyyy): ")
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: $"))
        percent_complete = int(input("Percent complete: "))
        project = Project(name, start_date, priority, cost_estimate, percent_complete)
        self.projects.append(project)

    def update_project(self):
        self.display_projects()
        choice = int(input("Project choice: "))
        project = self.projects[choice]
        new_percent_complete = input("New Percentage (leave blank to retain existing value): ")
        if new_percent_complete:
            project.update_progress(int(new_percent_complete))
        new_priority = input("New Priority (leave blank to retain existing value): ")
        if new_priority:
            project.update_priority(int(new_priority))


def main():
    filename = "projects.txt"
    pm_system = ProjectManagementSystem()
    pm_system.load_projects(filename)

    print("Welcome to Pythonic Project Management")
    while True:
        print("\nMenu:")
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").strip().lower()

        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            pm_system.load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            pm_system.save_projects(filename)
        elif choice == 'd':
            pm_system.display_projects()
        elif choice == 'f':
            date = input("Show projects that start after date (dd/mm/yyyy): ")
            pm_system.filter_projects_by_date(date)
        elif choice == 'a':
            pm_system.add_new_project()
        elif choice == 'u':
            pm_system.update_project()
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? ").strip().lower()
            if save_choice.startswith('y'):
                pm_system.save_projects("projects.txt")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
