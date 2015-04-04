from bottle import route, run, get
from bottledaemon import daemon_run
import subprocess
import logging
import os

LOG_FILE = 'hook.log'
BOTTLE_LOG_FILE = 'bottle.log'
BOTTLE_PID = 'bottle.pid'

LOG_PATH = os.path.dirname(os.path.realpath(__file__)) + '/' + LOG_FILE
BOTTLE_PATH = os.path.dirname(os.path.realpath(__file__)) + '/' + BOTTLE_LOG_FILE
BOTTLE_PID_PATH = os.path.dirname(os.path.realpath(__file__)) + '/' + BOTTLE_PID

@get('/pull/<path:path>')
def pull(path):
    logging.basicConfig(filename=LOG_PATH, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    logging.info('======================')
    logging.info('Pulling for %s' % path)
    path = path if path.startswith('/') else '/' + path
    if os.path.isdir(path):
        # output = subprocess.check_output(["git", "pull"], stderr=subprocess.STDOUT, cwd=path)
        output = subprocess.check_output(["git", "status"], stderr=subprocess.STDOUT, cwd=path)
        output = "%s" % (output.decode('unicode_escape'))
        logging.info(output)
        return output

    logging.info('given path %s does not exist' % path)
    return 'Given path does not exist, dude! Give me a proper path to work with lah! :)'

# run(host='localhost', port=8989)
if __name__ == "__main__":
  daemon_run(host='localhost', port=8989, logfile=BOTTLE_PATH, pidfile=BOTTLE_PID_PATH)