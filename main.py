import cv2
import pygame
import time

from gesture_detector import GestureDetector
from particle_engine import ParticleEngine



WIDTH = 1280
HEIGHT = 720

PARTICLE_COUNT = 3500

CAMERA_WIDTH = 300
CAMERA_HEIGHT = 220

CAMERA_X = 25
CAMERA_Y = 25



GESTURE_TO_TEXT = {
    "PEACE": "PEACE",
    "BRO": "BRO",
    "ROCK ON": "ROCK ON",
    "CHILL": "CHILL",
    "COOL": "COOL",
    "HELLO": "HELLO",
    "FUCK YOU": "FUCK YOU",
    "ONE LOVE": "ONE LOVE",
    "LOVE": "LOVE",
    "CLOCK IT": "CLOCK IT",
    "I SWAR": "I SWAR",
    "LAME": "LAME",
    "YOU SUCK": "YOU SUCK",
    "WASSUP": "WASSUP",
}



def camera_to_surface(frame, width, height):

    frame = cv2.resize(
        frame,
        (width, height)
    )

    frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    frame = frame.swapaxes(
        0,
        1
    )

    return pygame.surfarray.make_surface(
        frame
    )



def draw_camera_hud(
    screen,
    x,
    y,
    width,
    height,
    detected_gesture,
    hand_detected
):

    pygame.draw.rect(
        screen,
        (20, 25, 45),
        (
            x - 4,
            y - 4,
            width + 8,
            height + 8
        ),
        2,
        border_radius=10
    )

    bracket_color = (
        80,
        190,
        255
    )

    length = 22
    thickness = 3

    # Top-left
    pygame.draw.line(
        screen,
        bracket_color,
        (x, y),
        (x + length, y),
        thickness
    )

    pygame.draw.line(
        screen,
        bracket_color,
        (x, y),
        (x, y + length),
        thickness
    )

    pygame.draw.line(
        screen,
        bracket_color,
        (x + width, y),
        (x + width - length, y),
        thickness
    )

    pygame.draw.line(
        screen,
        bracket_color,
        (x + width, y),
        (x + width, y + length),
        thickness
    )

    # Bottom-left
    pygame.draw.line(
        screen,
        bracket_color,
        (x, y + height),
        (x + length, y + height),
        thickness
    )

    pygame.draw.line(
        screen,
        bracket_color,
        (x, y + height),
        (x, y + height - length),
        thickness
    )

    # Bottom-right
    pygame.draw.line(
        screen,
        bracket_color,
        (x + width, y + height),
        (x + width - length, y + height),
        thickness
    )

    pygame.draw.line(
        screen,
        bracket_color,
        (x + width, y + height),
        (x + width, y + height - length),
        thickness
    )

    # Header
    font = pygame.font.SysFont(
        "arial",
        13,
        bold=True
    )

    label = font.render(
        "HAND TRACKING",
        True,
        (220, 230, 245)
    )

    screen.blit(
        label,
        (
            x + 12,
            y + 10
        )
    )

    # Tracking status
    if hand_detected:

        indicator_color = (
            80,
            255,
            150
        )

        status = "TRACKING"

    else:

        indicator_color = (
            255,
            100,
            100
        )

        status = "SEARCHING"

    pygame.draw.circle(
        screen,
        indicator_color,
        (
            x + width - 72,
            y + 16
        ),
        5
    )

    status_surface = font.render(
        status,
        True,
        indicator_color
    )

    screen.blit(
        status_surface,
        (
            x + width - 62,
            y + 9
        )
    )

    gesture_font = pygame.font.SysFont(
        "arial",
        16,
        bold=True
    )

    if hand_detected:

        gesture_text = detected_gesture.upper()

    else:

        gesture_text = "NO HAND"

    gesture_surface = gesture_font.render(
        gesture_text,
        True,
        (255, 255, 255)
    )

    gesture_rect = gesture_surface.get_rect(
        center=(
            x + width // 2,
            y + height - 18
        )
    )

    screen.blit(
        gesture_surface,
        gesture_rect
    )



def configure_gesture_effect(
    particles,
    gesture
):

    if gesture == "PEACE":

        particles.set_shape("PEACE")
        particles.set_effect("wave")
        particles.set_color(
            (100, 210, 255)
        )

    elif gesture == "BRO":

        particles.set_shape("STAR")
        particles.set_effect("normal")
        particles.set_color(
            (255, 100, 100)
        )

    elif gesture == "ROCK ON":

        particles.set_shape("SPIRAL")
        particles.set_effect("orbit")
        particles.set_color(
            (255, 210, 80)
        )

    elif gesture == "CHILL":

        particles.set_shape("HEART")
        particles.set_effect("floating")
        particles.set_color(
            (120, 190, 255)
        )

    elif gesture == "COOL":

        particles.set_shape("CIRCLE")
        particles.set_effect("bounce")
        particles.set_color(
            (100, 220, 255)
        )

    elif gesture == "HELLO":

        particles.set_shape("HELLO")
        particles.set_effect("wave")
        particles.set_color(
            (180, 150, 255)
        )

    elif gesture == "FUCK YOU":

        particles.set_shape("TRIANGLE")
        particles.set_effect("normal")
        particles.set_color(
            (255, 80, 100)
        )

        particles.explode(
            strength=2.0
        )

    elif gesture == "ONE LOVE":

        particles.set_shape("HEART")
        particles.set_effect("floating")
        particles.set_color(
            (255, 100, 150)
        )

    elif gesture == "LOVE":

        particles.set_shape("DOUBLE HEART")
        particles.set_effect("floating")
        particles.set_color(
            (255, 100, 200)
        )

    elif gesture == "CLOCK IT":

        particles.set_shape("CIRCLE")
        particles.set_effect("orbit")
        particles.set_color(
            (100, 255, 220)
        )

    elif gesture == "I SWAR":

        particles.set_shape("INFINITY")
        particles.set_effect("orbit")
        particles.set_color(
            (170, 120, 255)
        )

    elif gesture == "LAME":

        particles.set_shape("LAME")
        particles.set_effect("falling")
        particles.set_color(
            (150, 150, 170)
        )

    elif gesture == "YOU SUCK":

        particles.set_shape("YOU SUCK")
        particles.set_effect("wave")
        particles.set_color(
            (255, 120, 100)
        )

    elif gesture == "WASSUP":

        particles.set_shape("WAVE")
        particles.set_effect("bounce")
        particles.set_color(
            (100, 220, 180)
        )



def main():

    pygame.init()

    screen = pygame.display.set_mode(
        (WIDTH, HEIGHT)
    )

    pygame.display.set_caption(
        "ParticleGesture"
    )

    clock = pygame.time.Clock()

  

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():

        print("Could not open camera.")

        pygame.quit()

        return

    

    detector = GestureDetector()


    particles = ParticleEngine(
        WIDTH,
        HEIGHT,
        PARTICLE_COUNT
    )


    current_text = "PEACE"

    last_gesture = None

    gesture_candidate = None

    gesture_start_time = 0

    running = True


    while running:


        success, frame = camera.read()

        detected_gesture = "Unknown"

        camera_surface = None

        hand_position = None

        if success:

            frame = cv2.flip(
                frame,
                1
            )

            detection_result = detector.detect(
                frame.copy()
            )

            if len(detection_result) == 3:

                (
                    processed_frame,
                    detected_gesture,
                    hand_position
                ) = detection_result

            else:

                (
                    processed_frame,
                    detected_gesture
                ) = detection_result

            camera_surface = camera_to_surface(
                processed_frame,
                CAMERA_WIDTH,
                CAMERA_HEIGHT
            )


        if hand_position is not None:

            hand_x = (
                hand_position[0]
                * WIDTH
            )

            hand_y = (
                hand_position[1]
                * HEIGHT
            )

            distance_from_center = (
                (
                    hand_x - WIDTH / 2
                ) ** 2
                +
                (
                    hand_y - HEIGHT / 2
                ) ** 2
            ) ** 0.5

            strength = min(
                1.0,
                distance_from_center
                / (WIDTH * 0.45)
            )

            particles.set_hand_position(
                hand_x,
                hand_y,
                strength
            )

        else:

            particles.clear_hand()


        if detected_gesture in GESTURE_TO_TEXT:

            if detected_gesture != gesture_candidate:

                gesture_candidate = detected_gesture

                gesture_start_time = time.time()

            else:

                elapsed = (
                    time.time()
                    - gesture_start_time
                )

                if elapsed >= 0.30:

                    if detected_gesture != last_gesture:

                        new_text = GESTURE_TO_TEXT[
                            detected_gesture
                        ]

                        particles.set_shape(
                            new_text
                        )

                        particles.explode(
                            strength=1.2
                        )

                        configure_gesture_effect(
                            particles,
                            detected_gesture
                        )

                        current_text = new_text

                        last_gesture = detected_gesture

        else:

            gesture_candidate = None

            gesture_start_time = 0


        particles.update()


        screen.fill(
            (2, 4, 12)
        )


        particles.draw(
            screen
        )


        if camera_surface is not None:

            screen.blit(
                camera_surface,
                (
                    CAMERA_X,
                    CAMERA_Y
                )
            )

            draw_camera_hud(
                screen,
                CAMERA_X,
                CAMERA_Y,
                CAMERA_WIDTH,
                CAMERA_HEIGHT,
                detected_gesture,
                hand_position is not None
            )


        status_font = pygame.font.SysFont(
            "arial",
            14,
            bold=True
        )

        if hand_position is not None:

            status_text = "GESTURE DETECTED"

            status_color = (
                100,
                255,
                180
            )

        else:

            status_text = "SHOW YOUR HAND"

            status_color = (
                100,
                120,
                150
            )

        status_surface = status_font.render(
            status_text,
            True,
            status_color
        )

        status_rect = status_surface.get_rect(
            center=(
                WIDTH // 2,
                35
            )
        )

        screen.blit(
            status_surface,
            status_rect
        )


        gesture_font = pygame.font.SysFont(
            "arial",
            18,
            bold=True
        )

        gesture_surface = gesture_font.render(
            f"GESTURE: {detected_gesture}",
            True,
            (170, 180, 200)
        )

        screen.blit(
            gesture_surface,
            (
                CAMERA_X,
                CAMERA_Y + CAMERA_HEIGHT + 12
            )
        )


        title_font = pygame.font.SysFont(
            "arial",
            26,
            bold=True
        )

        title_surface = title_font.render(
            current_text,
            True,
            (220, 230, 255)
        )

        title_rect = title_surface.get_rect(
            center=(
                WIDTH // 2,
                HEIGHT - 55
            )
        )

        screen.blit(
            title_surface,
            title_rect
        )


        fps_font = pygame.font.SysFont(
            "arial",
            13
        )

        fps_surface = fps_font.render(
            f"{int(clock.get_fps())} FPS",
            True,
            (90, 105, 130)
        )

        screen.blit(
            fps_surface,
            (
                WIDTH - 75,
                15
            )
        )


        info_font = pygame.font.SysFont(
            "arial",
            14
        )

        info_surface = info_font.render(
            "Move your hand and change the gesture   •   ESC to exit",
            True,
            (100, 110, 130)
        )

        info_rect = info_surface.get_rect(
            center=(
                WIDTH // 2,
                HEIGHT - 25
            )
        )

        screen.blit(
            info_surface,
            info_rect
        )


        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    running = False


        pygame.display.flip()

        clock.tick(60)


    detector.close()

    camera.release()

    pygame.quit()



if __name__ == "__main__":

    main()