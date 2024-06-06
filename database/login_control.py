import json
from ldap3 import Server, Connection, ALL, NTLM, Tls
import ssl


def login_control(username, password):
    with open("database/login_info.json") as f:
        data = json.load(f)

        chek_username = username.value
        chek_password = password.value

        for user in data["users"]:
            if user["username"] == chek_username and user["password"] == chek_password:
                # page.go('/home')
                return True
        return False


def authenticate_user(username, password, servername, domain):
    """
    Authenticates a user by connecting to an LDAP server and binding with the provided username and password.

    Parameters:
        username (str): The username of the user to authenticate.
        password (str): The password of the user to authenticate.
        servername (str): The name or IP address of the LDAP server.
        domain (str): The domain or organization unit of the LDAP server.

    Returns:
        bool: True if the user is authenticated successfully, False otherwise.
    """
    server = Server(
        servername,
        port=389,
        use_ssl=False,
        get_info=ALL,
        get_operation_progress=True,
    )
    user_dn = f"{domain}\\{username}"

    try:
        conn = Connection(
            server, user=user_dn, password=password, authentication=NTLM, auto_bind=True
        )
        return True
    except Exception as e:
        print(f"Authentication failed: {e}")
        return False
