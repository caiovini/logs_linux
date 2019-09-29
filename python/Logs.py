
import sys

from config import servers as serv
from config import users as user
from config import passwords as passw
from config import log_path as log_path
from fabric import Connection

command = "tail -n 50 -f -s 5 "

def vivere_app():
    con = Connection(host=serv.machine4,
                     user=user.userNameTomcat,
                     connect_kwargs={'password': passw.passwordTomcat})
    con.run(command + log_path.report)

def switch(arg):
    switcher = {
        "report" : report
    }
    return switcher.get(arg, lambda: print("Invalid argument"))    


if __name__ == "__main__":
    func = switch(sys.argv[1])
    func()
