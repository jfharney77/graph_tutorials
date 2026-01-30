"""Main module for agentic_vis.

Generates PowerPoint presentations with agent progress visualization.
"""
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pathlib import Path

from pptx import Presentation

from theme_and_title import apply_theme
from theme_and_title import use_previous_slide_deck
from theme_and_title import create_slide_from_theme
from theme_and_title import add_title_to_individual_slide
from src.agentic_vis.harvey import generate_harvey_balls
from src.agentic_vis.draw import connect_circles_batch,center_tool_nodes,center_l1_nodes,create_drawing_slide_from_slide,create_drawing_slide, connect_circles, draw_circles_center, resolve_circle_overlaps
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
    filename = 'agentic_plan.pptx'
    prs = Presentation()
    create_presentation(prs,filename)
    print ('created {filename}')
    '''




if __name__ == "__main__":
    main()



