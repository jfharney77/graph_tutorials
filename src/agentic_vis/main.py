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


