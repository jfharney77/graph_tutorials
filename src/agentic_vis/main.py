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



def personal_main2(
        pptx_output_file_path: str = "C:\\Users\\jfhar\\OneDrive\\Desktop\\github\\graph_tutorials\\agentic_plan.pptx",
        xlsx_input_file_path: str = "C:\\Users\\jfhar\\OneDrive\\Desktop\\github\\graph_tutorials\\hierarchy.xlsx"
    ) -> None:
    l12a_pairs = parse_excel_l12a(xlsx_input_file_path)
    print ('l12a_pairs:')
    print (l12a_pairs)
    a2t_pairs = parse_excel_a2t(xlsx_input_file_path)
    print ('a2t_pairs:')
    print (a2t_pairs)
    components_response = parse_excel_components(xlsx_input_file_path)
    
    print ('components_response:')
    print (components_response)
    items = components_response[0]
    sizes = components_response[1]
    print (items)
    print (sizes)
    
    prs = Presentation()
    slide = create_drawing_slide(prs, items, sizes)
    

    
    items = components_response[0]
    sizes = components_response[1]
    print (items)
    print (sizes)
    center_l1_nodes(slide)
    center_tool_nodes(slide)

    resolve_circle_overlaps(slide)

    write_surround_circles(slide, "Personalization", ["A1","A2","A3","A4","A5"])
    write_surround_circles(slide, "Knowledge", ["A6","A7","A8","A9","A10"])

    prs.save(pptx_output_file_path)
    print (f"saved {pptx_output_file_path}")


def main() -> None:
    """Entry point for agentic_vis."""
    
    
    pptx_output_file_path = "C:\\Users\\jfhar\\OneDrive\\Desktop\\github\\graph_tutorials\\agentic_plan.pptx"
    xlsx_input_file_path: str = "C:\\Users\\jfhar\\OneDrive\\Desktop\\github\\graph_tutorials\\hierarchy.xlsx"
    
    personal_main2(
        pptx_output_file_path,
        xlsx_input_file_path,
    )
    

    #full_control_open_pptx(pptx_output_file_path, False)

    # do something here to create a new slide deck

    #full_control_open_pptx(pptx_output_file_path)

if __name__ == "__main__":
    main()



