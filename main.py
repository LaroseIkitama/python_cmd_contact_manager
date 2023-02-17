""""This is the main python module where we call all the function  to do something
"""
import module1
import utils


def main():
    """This is the main function we call when running the python file
    """

    utils.utils1.clear_console()

    while True:

        utils.utils1.menu()
        choice = input(utils.utils1.indent("Your choice : \t ", 40))

        if utils.utils1.is_numeric(value=choice):
            utils.utils1.clear_console()
            module1.file1.switch(int(choice))

            if int(choice) == 6:
                print(
                    "\n"
                    + utils.utils1.indent(" ********* G O O D  B Y E ********* ", 40))
                break

        else:
            utils.utils1.clear_console()
            print(
                "\n"
                + utils.utils1.indent(" ********* Error please enter a number ********* ", 33))


if __name__ == "__main__":
    main()
