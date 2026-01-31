"""Main module for agentic_vis.

Generates PowerPoint presentations with agent progress visualization.
"""
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pathlib import Path

<<<<<<< HEAD
from pptx import Presentation

from theme_and_title import apply_theme
from theme_and_title import use_previous_slide_deck
from theme_and_title import create_slide_from_theme
from theme_and_title import add_title_to_individual_slide
from src.agentic_vis.harvey import generate_harvey_balls
from src.agentic_vis.draw import connect_circles_batch,center_tool_nodes,center_l1_nodes,create_drawing_slide_from_slide,create_drawing_slide, connect_circles, draw_circles_center, resolve_circle_overlaps
=======
import win32com

from agentic_vis.openers import full_control_open_pptx
from src.agentic_vis.harvey import generate_harvey_balls
from src.agentic_vis.draw import center_tool_nodes,center_l1_nodes,create_drawing_slide, connect_circles, draw_circles_center, resolve_circle_overlaps, write_surround_circles
>>>>>>> fc7e2cbfc910322054719f66b1d6a2414020cd8c
from src.agentic_vis.excel_utils import attach_harvey_balls, parse_excel_l12a, parse_excel_a2t, parse_excel_components

from src.agentic_vis.excel_utils import attach_harvey_balls

PROJ_ROOT = 'C:\\Users\\John_Harney\\github\\graph_tutorials'
XLSX_FILE_PATH = "C:\\Users\\John_Harney\\github\\graph_tutorials\\hierarchy.xlsx"

AGENTIC_VIS_TITLE = "Agentic Visualization Dashboard1"
DEST_FILE_DIR = PROJ_ROOT
DEST_FILE_NAME = 'agentic_plan.pptx'
SOURCE_FILE_DIR = PROJ_ROOT + '\\private_templates\\'
SOURCE_FILE_NAME = "slide_template_blank.pptx"
SLIDE_TO_COPY = 3


# `create_drawing_slide` is implemented in src/agentic_vis/draw.py



def create_presentation(prs,filename: str = "agentic_plan.pptx"):

    items = ['a','b','c','aa','bb','cc','a']
    sizes = [1, 2, 1, 1, 1, 1,1]
    slide = create_drawing_slide(prs, items, sizes)
    harvey_ball_dict = {
        'a' : 2,
        'aa' : 2,
        'b' : 1,
        'bb' : 3,
        'c' : 4
    }
    connect_circles(slide,'a','b')
    #generate_harvey_balls(slide, 

    #    ['a', 'c']
    #)
    generate_harvey_balls(
        slide,
        harvey_ball_dict,
    )
    prs.save(filename)


from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
import math

from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
import math
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
import math

def draw_circles_around_source(slide, source: str, dest: list[str]) -> None:
    """
    Draw 6 circles of size 0.25 around the source circle.

    Args:
        slide: The slide object to draw on.
        source: The name of the source circle.
        dest: A list of destination circle names (not used in this function).

    Returns:
        None
    """
    if not hasattr(slide, 'circle_info'):
        print("Error: No circle information found on slide.")
        return

    circle_info = slide.circle_info

<<<<<<< HEAD
    if source not in circle_info:
        print(f"Error: Source circle '{source}' not found on slide.")
        return

    # Get source circle info
    left, top, size, cx, cy = circle_info[source]

    # Calculate distance from source circle center to new circle center
    distance = 200 / 72  # 200px = 200/72 inches

    # Draw 6 circles around the source circle
    for i in range(6):
        angle = i * math.pi / 3  # 60 degrees between each circle

        # Calculate new circle center coordinates
        new_cx = cx + distance * math.cos(angle)
        new_cy = cy + distance * math.sin(angle)

        # Draw new circle
        new_circle = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            int((new_cx - 0.125) * 72),  # 0.25 inch diameter, convert to pixels
            int((new_cy - 0.125) * 72),  # 0.25 inch diameter, convert to pixels
            Inches(0.25),
            Inches(0.25)
        )

        # Format new circle with default styling
        new_circle.fill.solid()
        new_circle.fill.fore_color.rgb = RGBColor(100, 149, 237)  # Cornflower blue
        new_circle.line.color.rgb = RGBColor(25, 25, 112)  # Midnight blue

def main() -> None:
    """Entry point for agentic_vis."""

    file_path = XLSX_FILE_PATH#"C:\\Users\\jfhar\\OneDrive\\Desktop\\github\\graph_tutorials\\hierarchy.xlsx"
=======
def personal_main():
    file_path = "C:\\Users\\jfhar\\OneDrive\\Desktop\\github\\graph_tutorials\\hierarchy.xlsx"
>>>>>>> fc7e2cbfc910322054719f66b1d6a2414020cd8c
    l12a_pairs = parse_excel_l12a(file_path)
    print (l12a_pairs)
    a2t_pairs = parse_excel_a2t(file_path)
    print (a2t_pairs)
    components_response = parse_excel_components(file_path)
    

    items = components_response[0]
    sizes = components_response[1]
    print (items)
    print (sizes)

    
    dest_filename = DEST_FILE_DIR + '\\' + DEST_FILE_NAME
    source_filename = SOURCE_FILE_DIR + '\\' + SOURCE_FILE_NAME
    prs = Presentation()
    prs = use_previous_slide_deck(source_filename)

    slide_to_copy = SLIDE_TO_COPY
    layout = apply_theme(prs, slide_to_copy)
    slide = create_slide_from_theme(prs, layout)
    add_title_to_individual_slide(slide, AGENTIC_VIS_TITLE)


    create_drawing_slide_from_slide(prs,slide, items, sizes)
    
    resolve_circle_overlaps(slide)
    center_l1_nodes(slide)
    center_tool_nodes(slide)

    draw_circles_around_source(slide, "Personalization", ["a", "aa", "b", "bb", "c"])

    
    #harvey_ball_dict = attach_harvey_balls(file_path)
    #print (harvey_ball_dict)
    
    #generate_harvey_balls(
    #    slide,
    #    harvey_ball_dict,
    #)


    prs.save(dest_filename)
    print (f"saved {dest_filename}")

    print (layout)
    print ('exiting...')
    import sys
    sys.exit()



    #items = []
    #sizes = []
    slide = create_drawing_slide(prs, items, sizes)
    #connect_circles_batch(slide,a2t_pairs)
    #connect_circles(slide,'A1','T1')
    #add_circle_at_coords(slide, 100, 200)
    
    #circle_num = 3
    #draw_circles_center(slide, circle_num)
    center_l1_nodes(slide)
    center_tool_nodes(slide)
    
    

    resolve_circle_overlaps(slide)

    write_surround_circles(slide, "Personalization", ["A1","A2","A3","A4","A5"])
    write_surround_circles(slide, "Knowledge", ["A6","A7","A8","A9","A10"])

    #connect_circles_batch(slide,l12a_pairs)

    prs.save(filename)
    print (f"saved {filename}")

    '''

    harvey_ball_dict = attach_harvey_balls(file_path)
    print (harvey_ball_dict)
    
    generate_harvey_balls(
        slide,
        harvey_ball_dict,
    )

<<<<<<< HEAD
    
    slide = create_drawing_slide(prs, items, sizes)
    #connect_circles_batch(slide,a2t_pairs)
    #connect_circles(slide,'A1','T1')
    #add_circle_at_coords(slide, 100, 200)
    
    #circle_num = 3
    #draw_circles_center(slide, circle_num)
    resolve_circle_overlaps(slide)
    connect_circles_batch(slide,l12a_pairs)
    center_l1_nodes(slide)
    center_tool_nodes(slide)
    

    harvey_ball_dict = attach_harvey_balls(file_path)
    print (harvey_ball_dict)
    
    generate_harvey_balls(
        slide,
        harvey_ball_dict,
    )

    add_title_to_slide(prs.slides[0], "Agentic Visualization Dashboard")

    prs.save(filename)
    print (f"saved {filename}")
    '''
=======
>>>>>>> fc7e2cbfc910322054719f66b1d6a2414020cd8c
    filename = 'agentic_plan.pptx'
    prs = Presentation()
    create_presentation(prs,filename)
    print ('created {filename}')
    '''

import win32com.client

def close_ppt(filename):
    # Connect to running PowerPoint
    try:
        app = win32com.client.GetActiveObject("PowerPoint.Application")
    except:
        # PowerPoint is not running
        return None
    
    for presentation in app.Presentations:
        if presentation.Name.lower() == filename.lower():
            presentation.Close()
            print(f"{filename} closed.")
            return
    
    # Presentation not found
    return None

def close_ppt_safe(filename):
    """Close a PowerPoint presentation if it's open, otherwise return None.
    
    Args:
        filename: The name of the PowerPoint file to close.
        
    Returns:
        None if PowerPoint is not running or the file is not open.
    """
    try:
        app = win32com.client.GetActiveObject("PowerPoint.Application")
    except:
        # PowerPoint is not running
        print ('powerpoint not running?')
        return None
    print ('closing ppt...' + filename)
    for presentation in app.Presentations:
        if presentation.Name.lower() == filename.lower():
            presentation.Close()
            print(f"{filename} closed.")
            return
    
    # Presentation not found
    return None





def main() -> None:
    """Entry point for agentic_vis."""
    
    #personal_main()
    
    #close_ppt_safe("C:\\Users\\jfhar\\OneDrive\\Desktop\\github\\graph_tutorials\\agentic_plan.pptx")
    
    #for i in range(3):
    #    print (f"Opening in {3 - i} seconds...")
    #    import time
    #     time.sleep(1)

    full_control_open_pptx("C:\\Users\\jfhar\\OneDrive\\Desktop\\github\\graph_tutorials\\agentic_plan.pptx")

if __name__ == "__main__":
    main()



<<<<<<< HEAD
=======

def flatten_names_with_depth(data: dict) -> dict:
    """Flatten all values with key 'name' into a mapping of name -> depth.

    Depth is counted from each top-level key in the provided mapping. For each
    top-level key (e.g. 'l1') the depth of its immediate children starts at 1.

    Examples (shape):
    - 'l1' (top-level key) -> its child 'l2_a' has depth 1 when we enter its
        value; a 'name' inside 'l2_a' will therefore be recorded with depth 2.

    Args:
        data: Nested mapping following the user's structure.

    Returns:
        dict: mapping of each encountered name (string) to its integer depth.
    """

    result: dict = {}

    def _walk(node, depth: int):
        # node can be dict, list, or scalar
        if isinstance(node, dict):
            # If this dict has a 'name' key, record it at current depth
            if 'name' in node and isinstance(node['name'], str):
                result[node['name']] = depth

            for k, v in node.items():
                # Skip the 'name' key itself but traverse other values
                if k == 'name':
                    continue
                # Recurse into children, incrementing depth for nested structures
                if isinstance(v, (dict, list)):
                    _walk(v, depth + 1)
                # Scalars under other keys are ignored except 'name'
        elif isinstance(node, list):
            for item in node:
                _walk(item, depth + 1)

    # Iterate top-level keys; entering each top-level value starts at depth=1
    if isinstance(data, dict):
        for key, value in data.items():
            _walk(value, 1)

    return result

>>>>>>> fc7e2cbfc910322054719f66b1d6a2414020cd8c
