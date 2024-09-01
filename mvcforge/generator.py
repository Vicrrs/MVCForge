import os
import argparse
from os.path import exists

class MVCProjectGenerator:
    def __init__(self, project_name) -> None:
        self.project_name = project_name
        self.base_path = os.path.join(os.getcwd(), self.project_name)

    def create_directories(self):
        directories = [
            'models', 'views', 'controllers', 'templates',
            'static', 'static/css', 'static/js', 'static/images'
        ]

        for directory in directories:
            dir_path = os.path.join(self.base_path, directory)
            os.makedirs(dir_path, exist_ok=True)
            print(f"Created directory: {dir_path}")

    def create_files(self):
        files = {
            '__init__.py': ['models', 'views', 'controllers'],
            'base_model.py': ['models'],
            'base_view.py': ['views'],
            'base_controller.py': ['controllers'],
            'base_template.html': ['templates'],
            'main.py': [],
            'config.py': []
        }
        
        # Template content using project name
        template_content = {
            'main.py': f"""
# Main entry point for the {self.project_name} project.
# This is where the application starts. You can define routes and
# initialize your application here.

if __name__ == "__main__":
    print("Welcome to the {self.project_name}!")
    # Here you can add your code to initialize the app, for example:
    # app = create_app()
    # app.run()
            """,
            'config.py': f"""
# Configuration file for the {self.project_name} project.
# Use this file to define configuration settings like database URIs,
# secret keys, and other application-specific settings.

# Example:
# DATABASE_URI = 'sqlite:///mydatabase.db'
            """,
            'base_model.py': """
# Base model class for defining the data models.
# All your data models should inherit from this base class.
# This is a good place to define common attributes and methods for all models.

class BaseModel:
    # Define common model methods and properties here
    pass
            """,
            'base_view.py': """
# Base view class for defining the views.
# This is where you define how the data will be presented to the user.
# Views handle user input and return appropriate responses.

class BaseView:
    # Define common view methods and properties here
    pass
            """,
            'base_controller.py': """
# Base controller class for defining the controllers.
# Controllers are used to handle the logic of the application.
# They interact with the models and views to process user requests.

class BaseController:
    # Define common controller methods and properties here
    pass
            """,
            'base_template.html': """
<!DOCTYPE html>
<html>
<head>
    <title>{self.project_name} - Base Template</title>
</head>
<body>
    <h1>Welcome to {self.project_name}!</h1>
    <!-- This is the base HTML template. Use it to create the structure for your web pages. -->
    <!-- You can include headers, footers, and other common elements here. -->
</body>
</html>
            """
        }
        
        for file_name, dirs in files.items():
            if dirs:
                for directory in dirs:
                    file_path = os.path.join(self.base_path, directory, file_name)
                    with open(file_path, 'w') as f:
                        content = template_content.get(file_name, f"# {file_name.split('.')[0].capitalize()} file\n")
                        f.write(content)
                    print(f"Created file: {file_path}")
                    
    def generate_project(self):
        os.makedirs(self.base_path, exist_ok=True)
        print(f"Created base project directory: {self.base_path}")
        self.create_directories()
        self.create_files()
        
def main():
    parser = argparse.ArgumentParser(description="Generate a basic MVC project structure.")
    parser.add_argument("project_name", help="The name of the project to create.")
    args = parser.parse_args()

    project_name = args.project_name
    generator = MVCProjectGenerator(project_name)
    generator.generate_project()

if __name__ == "__main__":
    main()

