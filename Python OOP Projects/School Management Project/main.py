from Registrar import Registrar
from Data.DataManager import DataManager


def main():
    registrar = Registrar()

    """
    Run the function to create the student, teacher, and course csv files
    """
    if DataManager.create_student_csv() is True:
        registrar.register_student()


if __name__ == "__main__":
    main()
