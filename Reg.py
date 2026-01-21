# Import following modules
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio import start_server
import argparse
import re

# For checking Email, whether Valid or not.
regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

# For checking Phone Number, whether Valid or 
# not.
Pattern = re.compile(r"(0/91)?[6-9][0-9]{9}")

# For Checking URL, whether valid or not
regex_1 = ("((http|https)://)(www.)?" + 
           "[a-zA-Z0-9@:%._\\+~#?&//=]" +
           "{2,256}\\.[a-z]" +
           "{2,6}\\b([-a-zA-Z0-9@:%" +
           "._\\+~#?&//=]*)")
Pattern_1 = re.compile(regex_1)


def check_form(data):
    """Validation function used by `input_group`.

    Returns a (field_name, message) tuple on validation failure or None on success.
    """
    # for checking Name
    if data['name'].isdigit():
        return ('name', 'Invalid name!')

    # for checking UserName
    if data['username'].isdigit():
        return ('username', 'Invalid username!')

    # for checking Age
    if data['age'] <= 0:
        return ('age', 'Invalid age!')

    # for checking Email
    if not (re.search(regex, data['email'])):
        return ('email', 'Invalid email!')

    # for checking Phone Number (ensure match and length 10)
    phone_str = str(data['phone'])
    if not (Pattern.match(phone_str) and len(phone_str) == 10):
        return ('phone', 'Invalid phone!')

    # for checking Website URL
    if not Pattern_1.search(data['website']):
        return ('website', 'Invalid URL!')

    # for matching Passwords
    if data['pass'] != data['passes']:
        return ('passes', "Please make sure your passwords match")


def run_app():
    """Run the interactive registration form (console or web when served)."""
    # Taking input from the user
    data = input_group("Fill out the form:", [
        input('Username', name='username', type=TEXT,
              required=True, PlaceHolder="@username"),

        input('Password', name='pass', type=PASSWORD,
              required=True, PlaceHolder="Password"),

        input('Confirm Password', name='passes', type=PASSWORD,
              required=True, PlaceHolder="Confirm Password"),

        input('Name', name='name', type=TEXT, required=True,
              PlaceHolder="name"),

        input('Phone', name='phone', type=NUMBER,
              required=True, PlaceHolder="12345"),

        input('Email', name='email', type=TEXT,
              required=True, PlaceHolder="user@gmail.com"),

        input('Age', name='age', type=NUMBER, required=True,
              PlaceHolder="age"),

        input('Portfolio website', name='website', type=TEXT,
              required=True, PlaceHolder="www.XYZ.com")

    ], validate=check_form, cancelable=True)

    # Create a radio button
    gender = radio("Gender", options=['Male', 'Female'], required=True)

    # Create a skills markdown
    skills = select("Tech Stack", options=[
        'C Programming', 'Python', 'Web Development', 'Android Development'],
                    required=True)

    # Create a textarea
    text = textarea("Comments/Questions", rows=3,
                    placeholder="Write something...", required=True)

    # Create a checkbox
    agree = checkbox("Agreement", options=[
        'I agree to terms and conditions'], required=True)

    # Display output using popup
    popup("Your Details",
          f"Username: @{data['username']}\nName: {data['name']}\nPhone: {str(data['phone'])}\nEmail: {data['email']}\nAge: {str(data['age'])}\nWebsite: {data['website']}\nGender: {gender}\nSkill: {skills}\nComments: {text}",
          closable=True)


def main():
    run_app()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the registration form')
    parser.add_argument('--serve', action='store_true', help='Start a local web server (open in browser)')
    parser.add_argument('--port', type=int, default=8080, help='Port to use when serving')
    args = parser.parse_args()

    if args.serve:
        print(f"Starting PyWebIO server on http://localhost:{args.port} ...")
        start_server(run_app, port=args.port)
    else:
        print("Starting Reg.py in console mode...")
        run_app()
    