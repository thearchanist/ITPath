import os

def create_project_structure():
    # Membuat folder project-name
    os.makedirs("backend/core")
    os.makedirs("backend/forum")
    os.makedirs("backend/media")
    os.makedirs("backend/static")
    os.makedirs("backend/templates")
    os.makedirs("frontend/public")
    os.makedirs("frontend/src/assets")
    os.makedirs("frontend/src/components")
    os.makedirs("frontend/src/router")
    os.makedirs("frontend/src/views")
    os.makedirs("db/mongodb_data")
    os.makedirs("docs")
    os.makedirs("tests")

    # Membuat file manage.py dan requirements.txt
    with open("backend/manage.py", "w") as file:
        pass
    with open("backend/requirements.txt", "w") as file:
        pass

    # Membuat file package.json
    with open("frontend/package.json", "w") as file:
        pass

    # Membuat file .gitignore
    with open(".gitignore", "w") as file:
        file.write("*.pyc\n__pycache__/\n")

if __name__ == "__main__":
    create_project_structure()
