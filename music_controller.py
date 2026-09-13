import pyautogui
import time
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

class MusicController:
    def __init__(self):
        # New way to activate volume control
        speakers = AudioUtilities.GetSpeakers()
        interface = speakers._dev.Activate(
            IAudioEndpointVolume._iid_,
            CLSCTX_ALL,
            None
        )
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))
        self.last_action_time = 0
        self.cooldown = 1.5

    def _can_act(self):
        now = time.time()
        if now - self.last_action_time > self.cooldown:
            self.last_action_time = now
            return True
        return False

    def execute(self, gesture):
        if not self._can_act():
            return

        if gesture == "PLAY":
            pyautogui.press('playpause')
            print("▶ Play")

        elif gesture == "PAUSE":
            pyautogui.press('playpause')
            print("⏸ Pause")

        elif gesture == "NEXT":
            pyautogui.press('nexttrack')
            print("⏭ Next track")

        elif gesture == "PREV":
            pyautogui.press('prevtrack')
            print("⏮ Previous track")

        elif gesture == "VOL_UP":
            current = self.volume.GetMasterVolumeLevelScalar()
            new_vol = min(1.0, current + 0.1)
            self.volume.SetMasterVolumeLevelScalar(new_vol, None)
            print(f"🔊 Volume: {int(new_vol * 100)}%")

        elif gesture == "VOL_DOWN":
            current = self.volume.GetMasterVolumeLevelScalar()
            new_vol = max(0.0, current - 0.1)
            self.volume.SetMasterVolumeLevelScalar(new_vol, None)
            print(f"🔉 Volume: {int(new_vol * 100)}%")
