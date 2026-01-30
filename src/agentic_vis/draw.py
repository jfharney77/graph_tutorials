from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
import math


def connect_circles(slide, circ1_name: str, circ2_name: str) -> None:
    """Draw a line connecting two circles by their names at their circumferences.

    Args:
        slide: The slide object returned from create_drawing_slide.
        circ1_name: The text name of the first circle.
        circ2_name: The text name of the second circle.
    """
    if not hasattr(slide, 'circle_info'):
        print("Error: No circle information found on slide. Use slide from create_drawing_slide().")
        return

    circle_info = slide.circle_info

    #print ('exiting...')
    #import sys
    #sys.exit()

    if circ1_name not in circle_info or circ2_name not in circle_info:
        print(f"Error: Circle '{circ1_name}' or '{circ2_name}' not found on slide.")
        return

    # Get center coordinates and sizes of both circles
    left1, top1, size1, cx1, cy1 = circle_info[circ1_name]
    left2, top2, size2, cx2, cy2 = circle_info[circ2_name]

    # Calculate radii (half of size)
    radius1 = size1 / 2
    radius2 = size2 / 2

    # Calculate angle from circle1 center to circle2 center
    dx = cx2 - cx1
    dy = cy2 - cy1
    distance = math.sqrt(dx**2 + dy**2)

    if distance == 0:
        print("Warning: Circles have the same center, cannot draw a line.")
        return

    # Unit vector pointing from circle1 to circle2
    unit_dx = dx / distance
    unit_dy = dy / distance

    # Start point: on circumference of circle1 in direction of circle2
    start_x = cx1 + unit_dx * radius1
    start_y = cy1 + unit_dy * radius1

    # End point: on circumference of circle2 in direction of circle1
    end_x = cx2 - unit_dx * radius2
    end_y = cy2 - unit_dy * radius2

    # Draw a straight connector from circumference to circumference
    connector = slide.shapes.add_connector(1, int(start_x), int(start_y), int(end_x), int(end_y))
    connector.line.color.rgb = RGBColor(128, 128, 128)  # Gray line
    connector.line.width = Pt(2)  # 2 point width


def create_drawing_slide(prs, items: list[str] | None = None, sizes: list[float] | None = None):
    """Create a slide with circles containing text for each item in the list.

    Args:
        prs: The Presentation object to add the slide to.
        items: Optional list of strings to display in circles. If None, creates empty slide.
        sizes: Optional list of circle sizes (in inches) matching the length of items.
               If None, defaults to 1.5 inches for all circles.

    Returns:
        The slide object with `circle_info` attribute mapping names to positions/sizes,
        or `None` if no items were provided.
    """
    blank_slide_layout = prs.slide_layouts[6]  # Blank layout
    slide = prs.slides.add_slide(blank_slide_layout)

    if not items:
        return None

    # Deduplicate items while preserving order: if an item appears multiple
    # times in the input list, only draw the first occurrence.
    seen = set()
    unique_items = []
    for it in items:
        if it not in seen:
            seen.add(it)
            unique_items.append(it)

    # Get slide dimensions
    slide_width = prs.slide_width
    slide_height = prs.slide_height

    # Set default sizes if not provided. Map sizes to the first occurrence
    # of each unique item so duplicates use the first size provided.
    if sizes is None:
        sizes = [Inches(1.5)] * len(unique_items)
    else:
        orig_sizes = [Inches(s) if isinstance(s, (int, float)) else s for s in sizes]
        sizes = []
        for it in unique_items:
            try:
                idx = items.index(it)
                sizes.append(orig_sizes[idx] if idx < len(orig_sizes) else Inches(1.5))
            except ValueError:
                sizes.append(Inches(1.5))

    num_items = len(unique_items)

    # Calculate spacing
    if num_items == 1:
        # Center single circle
        circle_size = sizes[0]
        left = (slide_width - circle_size) / 2
        top = (slide_height - circle_size) / 2
        positions = [(left, top)]
    else:
        # Arrange in a circle pattern around the center
        import math
        center_x = slide_width / 2
        center_y = slide_height / 2
        radius = Inches(2)

        positions = []
        for i in range(num_items):
            angle = (2 * math.pi * i) / num_items
            circle_size = sizes[i]
            x = center_x + radius * math.cos(angle) - circle_size / 2
            y = center_y + radius * math.sin(angle) - circle_size / 2
            positions.append((x, y))

    # Store circle info: name -> (left, top, size, center_x, center_y)
    circle_info = {}

    # Create circles with text
    for i, (item, (left, top)) in enumerate(zip(unique_items, positions)):
        circle_size = sizes[i]
        center_x = left + circle_size / 2
        center_y = top + circle_size / 2
        circle_info[item] = (left, top, circle_size, center_x, center_y)

        # Add circle shape
        circle = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            int(left),
            int(top),
            circle_size,
            circle_size
        )

        # Format circle
        circle.fill.solid()
        circle.fill.fore_color.rgb = RGBColor(100, 149, 237)  # Cornflower blue
        circle.line.color.rgb = RGBColor(25, 25, 112)  # Midnight blue

        # Add text to circle
        text_frame = circle.text_frame
        text_frame.clear()  # Clear default text
        p = text_frame.paragraphs[0]
        p.text = item
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)  # White text
        p.alignment = 1  # Center alignment

    # Store circle info on slide for later use
    slide.circle_info = circle_info
    return slide


def add_circle_at_coords(slide, x: float, y: float) -> None:
    """Add a circle of size 0.5 inches at the specified coordinates on the slide.

    Args:
        slide: The slide object to add the circle to.
        x: The x coordinate (left position) in EMUs or as a numeric value.
        y: The y coordinate (top position) in EMUs or as a numeric value.
    """
    circle_size = Inches(0.5)

    # Add circle shape
    circle = slide.shapes.add_shape(
        MSO_SHAPE.OVAL,
        int(x),
        int(y),
        circle_size,
        circle_size
    )

    # Format circle with default styling
    circle.fill.solid()
    circle.fill.fore_color.rgb = RGBColor(100, 149, 237)  # Cornflower blue
    circle.line.color.rgb = RGBColor(25, 25, 112)  # Midnight blue

