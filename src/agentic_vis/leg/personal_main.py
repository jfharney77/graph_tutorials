
from pptx import Presentation
from agentic_vis.draw import center_l1_nodes, center_tool_nodes, create_drawing_slide, resolve_circle_overlaps, write_surround_circles
from agentic_vis.excel_utils import parse_excel_a2t, parse_excel_components, parse_excel_l12a


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


if __name__ == '__main__':
    personal_main()