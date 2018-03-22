"""
A sample showing how to have a NAOqi service as a Python app.
"""

__version__ = "0.0.3"

__author__ = 'Zach'
__email__ = 'zach.yan@teksbotics.com'


import qi,logging

import stk.runner,stk.events,stk.services,stk.logging
from dialog_engine import DialogEngine
from teks_logger import teks_logger

DEFAULT_LOGGER_FORMATTER = logging.Formatter('%(message)s,%(levelname)s,"%(asctime)s"')
DEFAULT_LOGGER_LEVEL = logging.INFO

logger = teks_logger("teks_demo", \
                     DEFAULT_LOGGER_FORMATTER, \
                     None, \
                     DEFAULT_LOGGER_LEVEL)

class ALMyService(object):
    "NAOqi service example (set/get on a simple value)."
    APP_UUID = "dialog_display"
    APP_ID = "com.teksbotics." + APP_UUID
    PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    WEBPATH = os.path.join("http://198.18.0.1", PATH[PATH.rfind("apps"):len(PATH)])
    APP_TOPICS_RELATIVE_PATH = APP_UUID + "/dialogs/"
    APP_TOPICS_ABSOLUTE_PATH = PATH + "/dialogs/"
    def __init__(self, qiapp):
        # generic activity boilerplate
        self.qiapp = qiapp
        self.events = stk.events.EventHelper(qiapp.session)
        self.s = stk.services.ServiceCache(qiapp.session)
        self.logger = stk.logging.get_logger(qiapp.session, self.APP_ID)
        self.dialogs = ['test']
        # Internal variables
        self.dialog = DialogEngine(self.s,self.logger,self.dialogs,subscriberID = APP_ID,pkgPath = PATH)
        #startDialog and stopDialog
        #Answered = qi.Property()

        #self.events.connect("Dialog/Answered",self.Answered)
        #self.events.connect("Dialog/LastInput",self.LastInput)



    #def Answered(self,p):


    @qi.bind(returnType=qi.Void, paramsType=[])
    def stop(self):
        "Stop the service."
        self.logger.info("ALMyService stopped by user request.")
        self.qiapp.stop()

    @qi.nobind
    def on_stop(self):
        "Cleanup (add yours if needed)"
        self.logger.info("ALMyService finished.")

####################
# Setup and Run
####################

if __name__ == "__main__":
    stk.runner.run_service(ALMyService)

