"""Harvey ball generation for PowerPoint presentations."""
from pptx.util import Inches
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor


def generate_harvey_balls(slide, items: list[str]) -> None:
    """Draw small indicator circles (Harvey balls) to the top-left of specified circles.

    Args:
        slide: The slide object returned from create_drawing_slide.
        items: List of circle names to add Harvey balls to.
    """
    if not hasattr(slide, 'circle_info'):
        print("Error: No circle information found on slide. Use slide from create_drawing_slide().")
        return

    circle_info = slide.circle_info
    harvey_ball_size = Inches(0.125)
    offset_pixels = 10

    for item_name in items:
        if item_name not in circle_info:
            print(f"Warning: Circle '{item_name}' not found on slide, skipping Harvey ball.")
            continue

        # Get circle info
        left, top, size, cx, cy = circle_info[item_name]
        radius = size / 2

        # Position Harvey ball to the top-left of the circle
        # 10 pixels to the left of the left edge and 10 pixels above the top edge
        harvey_left = left - harvey_ball_size - offset_pixels
        harvey_top = top - harvey_ball_size - offset_pixels

        # Create Harvey ball
        harvey_ball = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            int(harvey_left),
            int(harvey_top),
            harvey_ball_size,
            harvey_ball_size
        )

        # Format Harvey ball
        harvey_ball.fill.background()  # No fill
        harvey_ball.line.color.rgb = RGBColor(184, 134, 11)  # Dark goldenrod border
