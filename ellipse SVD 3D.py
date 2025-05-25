from manim import *
import numpy as np

class Ellipse3DTransform(ThreeDScene):
    def construct(self):
        # Set up axes
        axes = ThreeDAxes(x_range=[-4, 4], y_range=[-4, 4], z_range=[-4, 4])
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.add(axes)

        # Create 2D ellipse in XY plane
        ellipse = ParametricFunction(
            lambda t: np.array([
                2 * np.cos(t),  # Major axis along X
                np.sin(t),     # Minor axis along Y
                0              # Z=0 for XY plane
            ]),
            t_range = [0, TAU],
            color = BLUE
        )

        # Label for original ellipse
        label1 = Text("Original Ellipse", font_size=24).move_to(UP * 3.2 + LEFT * 2)
        self.play(Create(ellipse), Write(label1))
        self.wait(1)

        # Rotate the camera around the object
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(4)
        self.stop_ambient_camera_rotation()

        # Apply a linear transformation (e.g., stretch along X-axis)
        transform_matrix = [[1.5, 0, 0], [0, 1, 0], [0, 0, 1]]
        matrix = Matrix([
            ["1.5", "0"],
            ["0", "1"]
        ]).scale(0.6).to_corner(UR)

        label2 = Text("Elongated Ellipse", font_size=24).move_to(UP * 3.2 + RIGHT * 2)
        self.play(Write(matrix))
        self.wait(1)

        # Apply transformation using ApplyMatrix for visual effect
        self.play(ApplyMatrix(transform_matrix, ellipse), FadeOut(label1), Write(label2))
        self.wait(2)

        # Final camera rotation to show transformed shape
        self.begin_ambient_camera_rotation(rate=-0.15)
        self.wait(4)
        self.stop_ambient_camera_rotation()

        self.wait(2)
