class GestureRecognizer:
    # Finger tip landmark IDs from MediaPipe
    TIP_IDS = [4, 8, 12, 16, 20]

    def count_fingers(self, landmarks):
        if not landmarks:
            return 0

        fingers = []

        # Thumb (compares x position)
        if landmarks[4][0] < landmarks[3][0]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other 4 fingers (compare y position)
        for tip in self.TIP_IDS[1:]:
            if landmarks[tip][1] < landmarks[tip - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        return sum(fingers)

    def recognize(self, landmarks):
        count = self.count_fingers(landmarks)

        if count == 0:
            return "PAUSE"
        elif count == 1:
            return "PLAY"
        elif count == 2:
            return "NEXT"
        elif count == 3:
            return "PREV"
        elif count == 4:
            return "VOL_DOWN"
        elif count == 5:
            return "VOL_UP"
        else:
            return "NONE"
