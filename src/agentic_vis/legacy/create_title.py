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

