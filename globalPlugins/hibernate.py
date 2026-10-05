import globalPluginHandler
from scriptHandler import script
import subprocess
import ui
import threading

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    @script(
        description="رفتن سیستم به حالت هایبرنت",
        gesture="kb:NVDA+alt+h"
    )
    def script_hibernateSystem(self, gesture):
        ui.message("در حال هایبرنت کردن سیستم...")
        threading.Thread(target=self._runHibernateCommand).start()

    def _runHibernateCommand(self):
        try:
            # دستور استاندارد هایبرنت در ویندوز
            subprocess.run(
                ["rundll32.exe", "powrprof.dll,SetSuspendState", "1", "1", "0"],
                creationflags=subprocess.CREATE_NO_WINDOW
            )
        except Exception as e:
            ui.message(f"خطا در هایبرنت کردن سیستم: {str(e)}")