import random
import logging

#from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

#REPO_URL = 'https://github.com/krwrobel/superlist.git'
logging.basicConfig(level=logging.DEBUG)
run.echo = True

def hello():
    print("Hello")
    run('whoami')
    run('cat ~/.ssh/authorized_keys')

def deploy():
    site_folder =f'/home/{env.user}/sites/{env.host}'
#    run(f'mkdir -p {site_folder}')
#    with cd(site_folder):
#        _get_latest_source()
#        _update_virtualenv()
#        _create_or_update_dotenv()
#        _update_Static_files()
#        _update_database()