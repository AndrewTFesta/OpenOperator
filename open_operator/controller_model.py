"""
@title

@description

"""
import threading


class ControllerModel:

    def __init__(self):
        self.controller_thread = threading.Thread(target=self._run)
        self.running = True
        return

    def _run(self):
        self.running = True



        while self.running:
            pass

        print(f'Exiting model controller')
        return

    def start(self):
        self.controller_thread.start()
        return

    def stop(self):
        self.running = False
        return