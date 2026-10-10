import globalPluginHandler
from scriptHandler import script
import subprocess
import ui
import threading

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    @script(
        description="Hibernate the system",
        gesture="kb:NVDA+shift+control+h"
    )
    def script_hibernateSystem(self, gesture):
        ui.message("Hibernating the system...")
        threading.Thread(target=self._runHibernateCommand).start()

    def _runHibernateCommand(self):
        try:
            subprocess.run(
                ["rundll32.exe", "powrprof.dll,SetSuspendState", "1", "1", "0"],
                creationflags=subprocess.CREATE_NO_WINDOW
            )
        except Exception as e:
            ui.message(f"Error hibernating the system: {str(e)}")