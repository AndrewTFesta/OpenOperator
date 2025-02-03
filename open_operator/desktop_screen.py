"""
@title

@description

"""
import threading
import time

import cv2
import numpy as np
import pyautogui

from open_operator import data_dir
from open_operator.general_utils import time_tag
from open_operator.storage_utils import save_data


class DesktopScreen:

    def __init__(self):
        # https://pyautogui.readthedocs.io/en/latest/
        self.live_thread = threading.Thread(target=self._run)
        self.running = True

        self.fps = 30
        self.window_title = 'Live Screen Capture'
        self.display_capture = False

        self.save_format = 'avi'
        self.base_save_dir = data_dir / 'desktop_screen' / f'{time_tag()}'
        self.video_save_path = self.base_save_dir / f'output_frames.{self.save_format}'
        self.meta_save_path = self.base_save_dir / f'meta.json'
        self.video_codex = 'XVID'

        self.frame_history = []
        return

    def save_history(self):
        save_records = []
        for each_entry in self.frame_history:
            _ = each_entry.pop('frame', None)
            save_records.append(each_entry)
        archive = {
            'frame_path': str(self.video_save_path),
            'records': save_records,
        }
        save_data(archive, self.meta_save_path, human_readable=True)
        return

    def add_frame(self, frame, mouse_coords, on_screen):
        frame_entry = {
            'idx': len(self.frame_history),
            'title': self.window_title,
            'timestamp': time.time(),
            'frame': frame,
            'mouse_coords': mouse_coords,
            'on_screen': on_screen,
        }
        self.frame_history.append(frame_entry)
        return

    def _run(self):
        self.running = True
        frame_delay = int(1000.0 / self.fps)
        pyautogui.PAUSE = 0.01
        screen_size = pyautogui.size()
        if not self.base_save_dir.exists():
            self.base_save_dir.mkdir(parents=True, exist_ok=True)

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        color = (255, 255, 255)
        thickness = 2

        mouse_coords_loc = (50, 50)
        mouse_onscreen_loc = (50, 80)

        # noinspection PyUnresolvedReferences
        fourcc = cv2.VideoWriter_fourcc(*self.video_codex)
        out = cv2.VideoWriter(self.video_save_path, fourcc, 20.0, screen_size)
        while self.running:
            img = pyautogui.screenshot()
            mouse_x, mouse_y = pyautogui.position()
            on_screen = pyautogui.onScreen((mouse_x, mouse_y))

            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            self.add_frame(frame, (mouse_x, mouse_y), on_screen)
            out.write(frame)

            if self.display_capture:
                mouse_str = f'x: {mouse_x}, y: {mouse_y}'
                annot_frame = cv2.putText(
                    frame, mouse_str, mouse_coords_loc, font, font_scale, color, thickness, cv2.LINE_AA
                )
                annot_frame = cv2.putText(
                    annot_frame, f'{on_screen=}', mouse_onscreen_loc, font, font_scale, color, thickness, cv2.LINE_AA
                )
                cv2.imshow(self.window_title, annot_frame)
            cv2.waitKey(frame_delay)

        print(f'Exiting live desktop screen playback')
        out.release()
        cv2.destroyAllWindows()

        self.save_history()
        return

    def start(self, display: bool=None):
        if display is not None:
            self.display_capture = display
        self.live_thread.start()
        return

    def stop(self):
        self.running = False
        self.live_thread.join()
        return
