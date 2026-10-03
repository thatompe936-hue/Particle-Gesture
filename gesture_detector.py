import cv2
import mediapipe as mp
import math


class GestureDetector:

    def __init__(self):

        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

    # ==================================================
    # MAIN DETECTION
    # ==================================================

    def detect(self, frame):

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = self.hands.process(
            rgb_frame
        )

        gesture = "Unknown"

        if results.multi_hand_landmarks:

            hand = results.multi_hand_landmarks[0]

            self.mp_drawing.draw_landmarks(
                frame,
                hand,
                self.mp_hands.HAND_CONNECTIONS
            )

            gesture = self.recognize_gesture(hand)

        return frame, gesture

    # ==================================================
    # DISTANCE BETWEEN TWO LANDMARKS
    # ==================================================

    def distance(self, a, b):

        return math.sqrt(
            (a.x - b.x) ** 2 +
            (a.y - b.y) ** 2
        )

    # ==================================================
    # FINGER STATES
    # ==================================================

    def get_finger_states(self, hand):

        lm = hand.landmark

        index_up = (
            lm[8].y < lm[6].y
        )

        middle_up = (
            lm[12].y < lm[10].y
        )

        ring_up = (
            lm[16].y < lm[14].y
        )

        pinky_up = (
            lm[20].y < lm[18].y
        )

        thumb_extended = (
            abs(lm[4].x - lm[2].x) > 0.08
        )

        return (
            thumb_extended,
            index_up,
            middle_up,
            ring_up,
            pinky_up
        )

    # ==================================================
    # GESTURE RECOGNITION
    # ==================================================

    def recognize_gesture(self, hand):

        lm = hand.landmark

        (
            thumb,
            index,
            middle,
            ring,
            pinky
        ) = self.get_finger_states(hand)

        # ==================================================
        # MEASUREMENTS
        # ==================================================

        thumb_index_distance = self.distance(
            lm[4],
            lm[8]
        )

        # ==================================================
        # I SWAR
        # ==================================================

        if (
            index
            and middle
            and not ring
            and not pinky
        ):

            index_tip_x = lm[8].x
            middle_tip_x = lm[12].x

            index_pip_x = lm[6].x
            middle_pip_x = lm[10].x

            crossed = (
                (index_tip_x - middle_tip_x)
                *
                (index_pip_x - middle_pip_x)
                < 0
            )

            if crossed:
                return "I SWAR"

            return "PEACE"

        # ==================================================
        # LOVE
        #
        # Thumb and index touching.
        # Other three fingers extended.
        # ==================================================

        if (
            thumb_index_distance < 0.07
            and middle
            and ring
            and pinky
        ):
            return "LOVE"

        # ==================================================
        # CLOCK IT
        #
        # Thumb and index pinching.
        # Other fingers folded.
        # ==================================================

        if (
            thumb_index_distance < 0.09
            and not middle
            and not ring
            and not pinky
        ):
            return "CLOCK IT"

        # ==================================================
        # CHILL
        #
        # Thumb + index + pinky.
        # ==================================================

        if (
            thumb
            and index
            and not middle
            and not ring
            and pinky
        ):
            return "CHILL"

        # ==================================================
        # ROCK ON
        #
        # Index + pinky.
        # ==================================================

        if (
            index
            and not middle
            and not ring
            and pinky
        ):
            return "ROCK ON"

        # ==================================================
        # WASSUP
        #
        # Thumb + pinky.
        # ==================================================

        if (
            thumb
            and not index
            and not middle
            and not ring
            and pinky
        ):
            return "WASSUP"

        # ==================================================
        # HELLO
        #
        # All five fingers extended.
        # ==================================================

        if (
            thumb
            and index
            and middle
            and ring
            and pinky
        ):
            return "HELLO"

        # ==================================================
        # COOL / LAME
        #
        # Thumb only.
        # ==================================================

        if (
            thumb
            and not index
            and not middle
            and not ring
            and not pinky
        ):

            if lm[4].y < lm[3].y:
                return "COOL"

            if lm[4].y > lm[3].y:
                return "LAME"

        # ==================================================
        # FUCK YOU
        #
        # Middle finger only.
        # ==================================================

        if (
            not thumb
            and not index
            and middle
            and not ring
            and not pinky
        ):
            return "FUCK YOU"

        # ==================================================
        # INDEX GESTURES
        #
        # ONE LOVE / YOU SUCK
        # ==================================================

        if (
            not thumb
            and index
            and not middle
            and not ring
            and not pinky
        ):

            depth_difference = abs(
                lm[8].z - lm[5].z
            )

            if depth_difference > 0.12:
                return "YOU SUCK"

            return "ONE LOVE"

        # ==================================================
        # BRO
        #
        # Closed fist.
        # ==================================================

        if (
            not thumb
            and not index
            and not middle
            and not ring
            and not pinky
        ):
            return "BRO"

        # ==================================================
        # UNKNOWN
        # ==================================================

        return "Unknown"

    # ==================================================
    # CLOSE
    # ==================================================

    def close(self):

        self.hands.close()