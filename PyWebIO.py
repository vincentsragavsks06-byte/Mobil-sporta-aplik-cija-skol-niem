from pywebio import start_server
from pywebio.input import input_group, input, PASSWORD
from pywebio.output import put_text, put_success, put_error

def main():
    info = input_group("Login", [
        input('Username', name='username', required=True, placeholder='your username'),
        input('Password', name='password', type=PASSWORD, required=True, placeholder='your password')
    ])

    username = info['username']
    password = info['password']

    # simple check
    if username == 'admin' and password == 'secret':
        put_success(f'Welcome, {username}!')
    else:
        put_error('Invalid username or password')
        put_text(f'You submitted: {info}')

if __name__ == '__main__':
    start_server(main, port=8080, debug=True)