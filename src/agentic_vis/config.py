"""config.py."""
from pptx.dml.color import RGBColor

# Size constants for component types

L1_SIZE = 1.0
AGENT_SIZE = 0.4
TOOL_SIZE = 0.2

L1_COLOR = RGBColor(1,1,1)
AGENT_COLOR = RGBColor(2,2,2)
TOOL_COLOR = RGBColor(3,3,3)

MARGIN_X = 0.75
MARGIN_Y = 0.75

DEFAULT_SLIDE_WIDTH_INCHES = 10
DEFAULT_SLIDE_HEIGHT_INCHES = 7.5

INCHES_FROM_SOURCE_CENTER_TO_TARGET_CENTER = 1.0

L1_2_AGENTS_TAB_NAME = 'L12A'
AGENTS_2_TOOLS_TAB_NAME = 'A2T'
COMPONENTS_TAB_NAME = 'Components'


AGENTIC_VIS_TITLE = "Agentic Visualization Dashboard1"
DEFAULT_PROJ_ROOT = 'C:\\Users\\John_Harney\\github\\graph_tutorials'
DEFAULT_XLSX_FILE_PATH = "C:\\Users\\John_Harney\\github\\graph_tutorials\\hierarchy.xlsx"

DEST_FILE_DIR = DEFAULT_PROJ_ROOT
DEST_FILE_NAME = 'agentic_plan.pptx'
SOURCE_FILE_DIR = DEFAULT_PROJ_ROOT + '\\private_templates\\'
SOURCE_FILE_NAME = "slide_template_blank.pptx"
SLIDE_TO_COPY = 3
