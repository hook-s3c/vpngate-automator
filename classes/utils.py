import os
import pynotify


class Utils:
    """Utility library where we abstract code"""

    @staticmethod
    def create_directory_path(filepath):
        """inspects a file path and creates the directories if needed"""
 
	if not os.path.exists(os.path.dirname(filepath)):
	    try:
		os.makedirs(os.path.dirname(filepath))
	    except OSError as exc: # Guard against race condition
		if exc.errno != errno.EEXIST:
		    raise
        return

    @staticmethod
    def send_message(title, message):
	"""sends a message to the OS, to pop up as a notification"""

        pynotify.init("Test")
        notice = pynotify.Notification(title, message)
        notice.show()
        return
