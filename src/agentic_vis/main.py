"""Main module for agentic_vis.

Generates PowerPoint presentations with agent progress visualization.
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pathlib import Path

import win32com

from agentic_vis.openers import full_control_open_pptx
from src.agentic_vis.harvey import generate_harvey_balls
from src.agentic_vis.draw import center_tool_nodes,center_l1_nodes,create_drawing_slide, connect_circles, draw_circles_center, resolve_circle_overlaps, write_surround_circles
from src.agentic_vis.excel_utils import attach_harvey_balls, parse_excel_l12a, parse_excel_a2t, parse_excel_components


def create_title(prs: Presentation, powerpoint_title: str) -> None:
    """Create a title slide with the given title.

    Args:
        prs: The Presentation object to add the title slide to.
        powerpoint_title: The title text for the slide.
    """
    title_slide_layout = prs.slide_layouts[0]  # 0 is typically title slide layout
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]

    title.text = powerpoint_title
    subtitle.text = "Agentic Visualization Dashboard"


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


def connect_circles_batch(slide, pairs: list[tuple]) -> None:
    """Connect multiple pairs of circles in batch.

    For each tuple pair in the list, calls connect_circles with the pair's
    first element as circ1_name and second element as circ2_name.

    Args:
        slide: The slide object (typically returned from create_drawing_slide).
        pairs: A list of tuples where each tuple is (circ1_name, circ2_name).
    """
    for pair in pairs:
        if len(pair) >= 2:
            print ('connecting ' + str(pair[0] + ' ' + str(pair[1])))
            connect_circles(slide, pair[0], pair[1])



def personal_main():
    pass



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



