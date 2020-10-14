
import req_funcs

def main_function():
    selection=input()
    if selection == "1":
        req_funcs.get_amount_astronauts()
    elif selection == "2":
        req_funcs.get_iss_location()
    elif selection == "3":
        req_funcs.get_next_pass()
    else:
        print("You entered a non-valid value. Please run the app again.")


req_funcs.print_intro()
main_function()