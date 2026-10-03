import pygame
import random
import math


class ParticleEngine:

    def __init__(
        self,
        width,
        height,
        particle_count
    ):

        self.width = width
        self.height = height
        self.particle_count = particle_count

        self.particles = []

        self.target_points = []

        self.color = (
            100,
            210,
            255
        )

        self.effect = "normal"

        self.shape = "PEACE"

        self.hand_x = None
        self.hand_y = None
        self.hand_strength = 0

        self.time = 0

        # ------------------------------------------
        # Create particles
        # ------------------------------------------

        for _ in range(
            self.particle_count
        ):

            self.particles.append({

                "x": random.uniform(
                    0,
                    self.width
                ),

                "y": random.uniform(
                    0,
                    self.height
                ),

                "vx": random.uniform(
                    -1,
                    1
                ),

                "vy": random.uniform(
                    -1,
                    1
                ),

                "size": random.uniform(
                    1,
                    2.5
                ),

                "alpha": random.randint(
                    120,
                    255
                ),

                "target_x": self.width / 2,

                "target_y": self.height / 2,

                "phase": random.uniform(
                    0,
                    math.pi * 2
                )
            })

        self.set_shape(
            "PEACE"
        )

    # ==================================================
    # COLOR
    # ==================================================

    def set_color(
        self,
        color
    ):

        self.color = color

    # ==================================================
    # EFFECT
    # ==================================================

    def set_effect(
        self,
        effect
    ):

        self.effect = effect

    # ==================================================
    # HAND POSITION
    # ==================================================

    def set_hand_position(
        self,
        x,
        y,
        strength
    ):

        self.hand_x = x
        self.hand_y = y

        self.hand_strength = strength

    # ==================================================
    # CLEAR HAND
    # ==================================================

    def clear_hand(self):

        self.hand_x = None
        self.hand_y = None

        self.hand_strength = 0

    # ==================================================
    # SET SHAPE
    # ==================================================

    def set_shape(
        self,
        shape
    ):

        self.shape = shape

        self.target_points = (
            self.generate_shape_points(
                shape
            )
        )

        for i, particle in enumerate(
            self.particles
        ):

            if self.target_points:

                point = self.target_points[
                    i % len(
                        self.target_points
                    )
                ]

                particle["target_x"] = point[0]
                particle["target_y"] = point[1]

    # ==================================================
    # GENERATE SHAPE
    # ==================================================

    def generate_shape_points(
        self,
        shape
    ):

        shape = shape.upper()

        if shape in (
            "PEACE",
            "BRO",
            "ROCK ON",
            "CHILL",
            "COOL",
            "HELLO",
            "FUCK YOU",
            "ONE LOVE",
            "LOVE",
            "CLOCK IT",
            "I SWAR",
            "LAME",
            "YOU SUCK",
            "WASSUP"
        ):

            return self.text_points(
                shape
            )

        if shape == "STAR":

            return self.star_points()

        if shape == "HEART":

            return self.heart_points()

        if shape == "TRIANGLE":

            return self.triangle_points()

        if shape == "CIRCLE":

            return self.circle_points()

        if shape == "SPIRAL":

            return self.spiral_points()

        if shape == "INFINITY":

            return self.infinity_points()

        if shape == "DOUBLE HEART":

            return (
                self.double_heart_points()
            )

        if shape == "WAVE":

            return self.wave_points()

        return self.circle_points()

    # ==================================================
    # TEXT POINTS
    # ==================================================

    def text_points(
        self,
        text
    ):

        font = pygame.font.SysFont(
            "arial",
            170,
            bold=True
        )

        surface = font.render(
            text,
            True,
            (255, 255, 255)
        )

        rect = surface.get_rect(
            center=(
                self.width // 2,
                self.height // 2
            )
        )

        points = []

        step = 4

        for y in range(
            0,
            surface.get_height(),
            step
        ):

            for x in range(
                0,
                surface.get_width(),
                step
            ):

                pixel = surface.get_at(
                    (
                        x,
                        y
                    )
                )

                if pixel[3] > 0:

                    points.append(
                        (
                            rect.x + x,
                            rect.y + y
                        )
                    )

        if not points:

            return self.circle_points()

        return points

    # ==================================================
    # STAR
    # ==================================================

    def star_points(
        self
    ):

        points = []

        center_x = self.width / 2
        center_y = self.height / 2

        outer_radius = 220
        inner_radius = 95

        vertices = 10

        for i in range(
            self.particle_count
        ):

            angle = (
                random.uniform(
                    0,
                    math.pi * 2
                )
            )

            sector = (
                angle
                / (
                    math.pi * 2
                )
                * vertices
            )

            distance = (
                outer_radius
                if int(sector) % 2 == 0
                else inner_radius
            )

            distance += random.uniform(
                -8,
                8
            )

            x = (
                center_x
                + math.cos(angle)
                * distance
            )

            y = (
                center_y
                + math.sin(angle)
                * distance
            )

            points.append(
                (
                    x,
                    y
                )
            )

        return points

    # ==================================================
    # HEART
    # ==================================================

    def heart_points(
        self
    ):

        points = []

        center_x = self.width / 2
        center_y = self.height / 2

        scale = 12

        for _ in range(
            self.particle_count
        ):

            t = random.uniform(
                0,
                math.pi * 2
            )

            x = (
                16
                * math.sin(t) ** 3
            )

            y = (
                13
                * math.cos(t)
                - 5
                * math.cos(2 * t)
                - 2
                * math.cos(3 * t)
                - math.cos(4 * t)
            )

            x *= scale
            y *= -scale

            # Add slight thickness

            x += random.uniform(
                -12,
                12
            )

            y += random.uniform(
                -12,
                12
            )

            points.append(
                (
                    center_x + x,
                    center_y + y
                )
            )

        return points

    # ==================================================
    # DOUBLE HEART
    # ==================================================

    def double_heart_points(
        self
    ):

        points = []

        original_x = self.width / 2

        heart_width = 190

        for i in range(
            self.particle_count
        ):

            side = (
                -1
                if i % 2 == 0
                else 1
            )

            t = random.uniform(
                0,
                math.pi * 2
            )

            x = (
                16
                * math.sin(t) ** 3
            )

            y = (
                13
                * math.cos(t)
                - 5
                * math.cos(2 * t)
                - 2
                * math.cos(3 * t)
                - math.cos(4 * t)
            )

            x *= 7
            y *= -7

            x += (
                original_x
                + side * heart_width
            )

            y += (
                self.height / 2
            )

            points.append(
                (
                    x,
                    y
                )
            )

        return points

    # ==================================================
    # TRIANGLE
    # ==================================================

    def triangle_points(
        self
    ):

        points = []

        cx = self.width / 2
        cy = self.height / 2

        radius = 250

        vertices = [

            (
                cx,
                cy - radius
            ),

            (
                cx - radius,
                cy + radius
            ),

            (
                cx + radius,
                cy + radius
            )
        ]

        for _ in range(
            self.particle_count
        ):

            a = random.uniform(
                0,
                1
            )

            b = random.uniform(
                0,
                1
            )

            if a + b > 1:

                a = 1 - a
                b = 1 - b

            c = (
                1
                - a
                - b
            )

            x = (
                a * vertices[0][0]
                + b * vertices[1][0]
                + c * vertices[2][0]
            )

            y = (
                a * vertices[0][1]
                + b * vertices[1][1]
                + c * vertices[2][1]
            )

            points.append(
                (
                    x,
                    y
                )
            )

        return points

    # ==================================================
    # CIRCLE
    # ==================================================

    def circle_points(
        self
    ):

        points = []

        cx = self.width / 2
        cy = self.height / 2

        radius = 230

        for _ in range(
            self.particle_count
        ):

            angle = random.uniform(
                0,
                math.pi * 2
            )

            r = radius + random.uniform(
                -12,
                12
            )

            points.append(
                (
                    cx
                    + math.cos(angle) * r,

                    cy
                    + math.sin(angle) * r
                )
            )

        return points

    # ==================================================
    # SPIRAL
    # ==================================================

    def spiral_points(
        self
    ):

        points = []

        cx = self.width / 2
        cy = self.height / 2

        for i in range(
            self.particle_count
        ):

            angle = (
                i
                * 0.15
            )

            radius = (
                3
                + i
                * 0.055
            )

            radius = min(
                radius,
                300
            )

            x = (
                cx
                + math.cos(angle)
                * radius
            )

            y = (
                cy
                + math.sin(angle)
                * radius
            )

            points.append(
                (
                    x,
                    y
                )
            )

        return points

    # ==================================================
    # INFINITY
    # ==================================================

    def infinity_points(
        self
    ):

        points = []

        cx = self.width / 2
        cy = self.height / 2

        scale = 260

        for i in range(
            self.particle_count
        ):

            t = (
                i
                / self.particle_count
                * math.pi
                * 2
            )

            denominator = (
                1
                + math.sin(t) ** 2
            )

            x = (
                math.cos(t)
                / denominator
            )

            y = (
                math.sin(t)
                * math.cos(t)
                / denominator
            )

            points.append(
                (
                    cx + x * scale,
                    cy + y * scale
                )
            )

        return points

    # ==================================================
    # WAVE
    # ==================================================

    def wave_points(
        self
    ):

        points = []

        spacing = (
            self.width
            / self.particle_count
        )

        for i in range(
            self.particle_count
        ):

            x = (
                i
                * spacing
            )

            y = (
                self.height / 2
                + math.sin(
                    x * 0.025
                )
                * 120
            )

            points.append(
                (
                    x,
                    y
                )
            )

        return points

    # ==================================================
    # EXPLOSION
    # ==================================================

    def explode(
        self,
        strength=1.0
    ):

        for particle in self.particles:

            angle = random.uniform(
                0,
                math.pi * 2
            )

            speed = random.uniform(
                2,
                8
            ) * strength

            particle["vx"] += (
                math.cos(angle)
                * speed
            )

            particle["vy"] += (
                math.sin(angle)
                * speed
            )

    # ==================================================
    # UPDATE
    # ==================================================

    def update(
        self
    ):

        self.time += 0.03

        for particle in self.particles:

            # ------------------------------------------
            # Target
            # ------------------------------------------

            dx = (
                particle["target_x"]
                - particle["x"]
            )

            dy = (
                particle["target_y"]
                - particle["y"]
            )

            particle["vx"] += (
                dx * 0.008
            )

            particle["vy"] += (
                dy * 0.008
            )

            # ------------------------------------------
            # Damping
            # ------------------------------------------

            particle["vx"] *= 0.88

            particle["vy"] *= 0.88

            # ------------------------------------------
            # Effect
            # ------------------------------------------

            if self.effect == "wave":

                particle["vy"] += (
                    math.sin(
                        self.time
                        + particle["phase"]
                    )
                    * 0.08
                )

            elif self.effect == "floating":

                particle["x"] += (
                    math.sin(
                        self.time
                        + particle["phase"]
                    )
                    * 0.5
                )

                particle["y"] += (
                    math.cos(
                        self.time
                        + particle["phase"]
                    )
                    * 0.5
                )

            elif self.effect == "orbit":

                cx = self.width / 2
                cy = self.height / 2

                ox = (
                    particle["x"]
                    - cx
                )

                oy = (
                    particle["y"]
                    - cy
                )

                particle["vx"] += (
                    -oy * 0.0005
                )

                particle["vy"] += (
                    ox * 0.0005
                )

            elif self.effect == "bounce":

                particle["vy"] += 0.08

                if (
                    particle["y"]
                    > self.height
                ):

                    particle["y"] = (
                        self.height
                    )

                    particle["vy"] *= -0.8

            elif self.effect == "falling":

                particle["vy"] += 0.05

                if (
                    particle["y"]
                    > self.height
                ):

                    particle["y"] = 0

            # ------------------------------------------
            # Hand interaction
            # ------------------------------------------

            if self.hand_x is not None:

                dx = (
                    particle["x"]
                    - self.hand_x
                )

                dy = (
                    particle["y"]
                    - self.hand_y
                )

                distance = math.sqrt(
                    dx * dx
                    + dy * dy
                )

                radius = 180

                if (
                    distance < radius
                    and distance > 0
                ):

                    force = (
                        1
                        - distance / radius
                    )

                    force *= (
                        self.hand_strength
                        * 3
                    )

                    particle["vx"] += (
                        dx
                        / distance
                        * force
                    )

                    particle["vy"] += (
                        dy
                        / distance
                        * force
                    )

            # ------------------------------------------
            # Move
            # ------------------------------------------

            particle["x"] += (
                particle["vx"]
            )

            particle["y"] += (
                particle["vy"]
            )

            # ------------------------------------------
            # Keep particles alive
            # ------------------------------------------

            if particle["x"] < -50:

                particle["x"] = (
                    self.width + 50
                )

            if particle["x"] > (
                self.width + 50
            ):

                particle["x"] = -50

            if particle["y"] < -50:

                particle["y"] = (
                    self.height + 50
                )

            if particle["y"] > (
                self.height + 50
            ):

                particle["y"] = -50

    # ==================================================
    # DRAW
    # ==================================================

    def draw(
        self,
        screen
    ):

        for particle in self.particles:

            x = int(
                particle["x"]
            )

            y = int(
                particle["y"]
            )

            size = max(
                1,
                int(
                    particle["size"]
                )
            )

            pygame.draw.circle(
                screen,
                self.color,
                (
                    x,
                    y
                ),
                size
            )