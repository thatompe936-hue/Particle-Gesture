import math
import numpy as np
import pygame


class ShapeFactory:

    # ==================================================
    # MAIN GETTER
    # ==================================================

    @staticmethod
    def get(name, count, width, height):

        if name == "PEACE":
            return ShapeFactory.text(
                "PEACE",
                count,
                width,
                height
            )

        if name == "BRO":
            return ShapeFactory.text(
                "BRO",
                count,
                width,
                height
            )

        if name == "ROCK ON":
            return ShapeFactory.text(
                "ROCK ON",
                count,
                width,
                height
            )

        if name == "CHILL":
            return ShapeFactory.text(
                "CHILL",
                count,
                width,
                height
            )

        if name == "COOL":
            return ShapeFactory.text(
                "COOL",
                count,
                width,
                height
            )

        if name == "HELLO":
            return ShapeFactory.text(
                "HELLO",
                count,
                width,
                height
            )

        if name == "FUCK YOU":
            return ShapeFactory.text(
                "FUCK YOU",
                count,
                width,
                height
            )

        if name == "ONE LOVE":
            return ShapeFactory.text(
                "ONE LOVE",
                count,
                width,
                height
            )

        if name == "GAY":
            return ShapeFactory.text(
                "GAY",
                count,
                width,
                height
            )

        if name == "CLOCK IT":
            return ShapeFactory.text(
                "CLOCK IT",
                count,
                width,
                height
            )

        if name == "I SWAR":
            return ShapeFactory.text(
                "I SWAR",
                count,
                width,
                height
            )

        if name == "LAME":
            return ShapeFactory.text(
                "LAME",
                count,
                width,
                height
            )

        if name == "YOU SUCK":
            return ShapeFactory.text(
                "YOU SUCK",
                count,
                width,
                height
            )

        if name == "WASSUP":
            return ShapeFactory.text(
                "WASSUP",
                count,
                width,
                height
            )

        # Extra shapes
        if name == "HEART":
            return ShapeFactory.heart(
                count,
                width,
                height
            )

        if name == "STAR":
            return ShapeFactory.star(
                count,
                width,
                height
            )

        if name == "TRIANGLE":
            return ShapeFactory.triangle(
                count,
                width,
                height
            )

        if name == "RING":
            return ShapeFactory.ring(
                count,
                width,
                height
            )

        return ShapeFactory.circle(
            count,
            width,
            height
        )

    # ==================================================
    # TEXT
    # ==================================================

    @staticmethod
    def text(
        text,
        count,
        width,
        height
    ):

        font_size = 220

        font = pygame.font.SysFont(
            "arial",
            font_size,
            bold=True
        )

        # ------------------------------------------
        # Fit text to screen
        # ------------------------------------------

        while (
            font.size(text)[0] > width * 0.72
            and font_size > 40
        ):

            font_size -= 5

            font = pygame.font.SysFont(
                "arial",
                font_size,
                bold=True
            )

        surface = font.render(
            text,
            True,
            (255, 255, 255)
        )

        # ------------------------------------------
        # Get alpha
        # ------------------------------------------

        alpha = pygame.surfarray.array_alpha(
            surface
        )

        # IMPORTANT:
        # array_alpha uses X,Y ordering.
        # Keep coordinates in this order.

        xs, ys = np.where(
            alpha > 80
        )

        if len(xs) == 0:

            return ShapeFactory.circle(
                count,
                width,
                height
            )

        points = np.column_stack(
            (xs, ys)
        ).astype(float)

        # ------------------------------------------
        # Center
        # ------------------------------------------

        points[:, 0] -= (
            surface.get_width() / 2
        )

        points[:, 1] -= (
            surface.get_height() / 2
        )

        # ------------------------------------------
        # Scale
        # ------------------------------------------

        scale_x = (
            width * 0.72
        ) / surface.get_width()

        scale_y = (
            height * 0.55
        ) / surface.get_height()

        scale = min(
            scale_x,
            scale_y
        )

        points *= scale

        # ------------------------------------------
        # Select particles
        # ------------------------------------------

        if len(points) >= count:

            indices = np.random.choice(
                len(points),
                count,
                replace=False
            )

        else:

            indices = np.random.choice(
                len(points),
                count,
                replace=True
            )

        return points[indices]

    # ==================================================
    # CIRCLE
    # ==================================================

    @staticmethod
    def circle(
        count,
        width,
        height
    ):

        radius = min(
            width,
            height
        ) * 0.25

        angles = np.random.uniform(
            0,
            math.pi * 2,
            count
        )

        radii = np.sqrt(
            np.random.uniform(
                0,
                1,
                count
            )
        ) * radius

        x = np.cos(angles) * radii
        y = np.sin(angles) * radii

        return np.column_stack(
            (x, y)
        )

    # ==================================================
    # RING
    # ==================================================

    @staticmethod
    def ring(
        count,
        width,
        height
    ):

        radius = min(
            width,
            height
        ) * 0.32

        angles = np.random.uniform(
            0,
            math.pi * 2,
            count
        )

        radius_variation = np.random.normal(
            0,
            4,
            count
        )

        radii = (
            radius
            + radius_variation
        )

        x = np.cos(angles) * radii
        y = np.sin(angles) * radii

        return np.column_stack(
            (x, y)
        )

    # ==================================================
    # HEART
    # ==================================================

    @staticmethod
    def heart(
        count,
        width,
        height
    ):

        t = np.random.uniform(
            0,
            math.pi * 2,
            count
        )

        scale = min(
            width,
            height
        ) * 0.025

        x = (
            16 * np.sin(t) ** 3
        )

        y = (
            13 * np.cos(t)
            - 5 * np.cos(2 * t)
            - 2 * np.cos(3 * t)
            - np.cos(4 * t)
        )

        # Add slight thickness
        thickness = np.random.normal(
            0,
            2,
            count
        )

        x += thickness
        y += thickness

        x *= scale
        y *= -scale

        return np.column_stack(
            (x, y)
        )

    # ==================================================
    # STAR
    # ==================================================

    @staticmethod
    def star(
        count,
        width,
        height
    ):

        points = []

        outer_radius = min(
            width,
            height
        ) * 0.32

        inner_radius = (
            outer_radius * 0.42
        )

        for i in range(10):

            angle = (
                -math.pi / 2
                + i * math.pi / 5
            )

            radius = (
                outer_radius
                if i % 2 == 0
                else inner_radius
            )

            points.append(
                (
                    math.cos(angle) * radius,
                    math.sin(angle) * radius
                )
            )

        points = np.array(
            points,
            dtype=float
        )

        # Randomly select line segments
        result = []

        for _ in range(count):

            segment = np.random.randint(
                0,
                len(points)
            )

            a = points[segment]

            b = points[
                (segment + 1)
                % len(points)
            ]

            t = np.random.random()

            point = (
                a
                + (b - a) * t
            )

            # Slight particle spread
            point += np.random.normal(
                0,
                2,
                2
            )

            result.append(point)

        return np.array(
            result
        )

    # ==================================================
    # TRIANGLE
    # ==================================================

    @staticmethod
    def triangle(
        count,
        width,
        height
    ):

        radius = min(
            width,
            height
        ) * 0.30

        vertices = np.array(
            [
                [
                    0,
                    -radius
                ],
                [
                    -radius,
                    radius
                ],
                [
                    radius,
                    radius
                ]
            ],
            dtype=float
        )

        result = []

        for _ in range(count):

            edge = np.random.randint(
                0,
                3
            )

            a = vertices[edge]

            b = vertices[
                (edge + 1) % 3
            ]

            t = np.random.random()

            point = (
                a
                + (b - a) * t
            )

            point += np.random.normal(
                0,
                2,
                2
            )

            result.append(point)

        return np.array(
            result
        )