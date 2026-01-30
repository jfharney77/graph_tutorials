"""Main module for agentic_vis.

Generates PowerPoint presentations with agent progress visualization.
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pathlib import Path

import win32com

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
    file_path = "C:\\Users\\jfhar\\OneDrive\\Desktop\\github\\graph_tutorials\\hierarchy.xlsx"
    l12a_pairs = parse_excel_l12a(file_path)
    print (l12a_pairs)
    a2t_pairs = parse_excel_a2t(file_path)
    print (a2t_pairs)
    components_response = parse_excel_components(file_path)
    

    items = components_response[0]
    sizes = components_response[1]
    print (items)
    print (sizes)

    
    filename = 'agentic_plan.pptx'
    prs = Presentation()
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

    from src.agentic_vis.excel_utils import attach_harvey_balls
    harvey_ball_dict = attach_harvey_balls(file_path)
    print (harvey_ball_dict)
    
    generate_harvey_balls(
        slide,
        harvey_ball_dict,
    )

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

def close_ppt_app(app):
    app.Quit()
    print("PowerPoint application closed.")

import os

def open_pptx(filename: str):
    os.startfile(filename)


def full_control_open_pptx(filename: str):
    import win32com.client

    app = win32com.client.Dispatch("PowerPoint.Application")
    app.Visible = True

    presentation = app.Presentations.Open(filename)

    # Do stuff here...
    input("Press Enter to close the presentation and quit PowerPoint...")

    presentation.Close()
    app.Quit()


def main() -> None:
    """Entry point for agentic_vis."""
    
    #personal_main()
    
    #close_ppt_safe("C:\\Users\\jfhar\\OneDrive\\Desktop\\github\\graph_tutorials\\agentic_plan.pptx")
    
    #for i in range(3):
    #    print (f"Opening in {3 - i} seconds...")
    #    import time
    #     time.sleep(1)

    #open_pptx("C:\\Users\\jfhar\\OneDrive\\Desktop\\github\\graph_tutorials\\agentic_plan.pptx")
    full_control_open_pptx("C:\\Users\\jfhar\\OneDrive\\Desktop\\github\\graph_tutorials\\agentic_plan.pptx")

if __name__ == "__main__":
    main()




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

"""
my_dict = {
    "l1" : {
        "name" : "",
        "types" : {
            "p" : {
                "name" : "",
                "agents" : {
                    "name: "",
                    "tools" : {
                        [ 
                            {
                                "name" : "",
                                "progress" : 2
                            }
                        ]

                    },
                    "progress : "" 
                },
        }
    }
}
}
"""

