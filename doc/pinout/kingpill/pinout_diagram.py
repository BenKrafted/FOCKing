from pinout.core import Group, Image
from pinout.components.layout import Diagram_2Rows
from pinout.components.pinlabel import PinLabelGroup
from pinout.components.text import TextBlock
from pinout.components.legend import Legend
from pinout.components import leaderline as lline

# Import pin label data
import data

# Create a new diagram
diagram = Diagram_2Rows(1024, 1200, 1000, "diagram")
diagram.add_stylesheet("styles.css", embed=True)

# Diagram group
graphic = diagram.panel_01.add(Group(400, 42))

# Hardware image
hardware = graphic.add(Image("kingpill.png", embed=True))

# Add key coordinates (measured manually or using pixel tools)
hardware.add_coord("left_header", 26, 57)       # top left pin
hardware.add_coord("right_header", 218, 57)     # top right pin
hardware.add_coord("swd_header", 57, 534)       # SWD header
# Other (x,y) pairs can also be stored here
hardware.add_coord("pin_pitch_v", 0, 32)
hardware.add_coord("pin_pitch_h", 32, 0)

# Add LEFT pin labels
graphic.add(
    PinLabelGroup(
        x=hardware.coord("left_header").x,
        y=hardware.coord("left_header").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(60, 0),
        label_pitch=(0, 32),
        scale=(-1, 1),
        labels=data.left_header,
    )
)

# Add RIGHT pin labels
graphic.add(
    PinLabelGroup(
        x=hardware.coord("right_header").x,
        y=hardware.coord("right_header").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(60, 0),
        label_pitch=(0, 32),
        scale=(1, 1),
        labels=data.right_header,
    )
)

# Create pinlabels on SWD header
graphic.add(
    PinLabelGroup(
        x=hardware.coord("swd_header").x,
        y=hardware.coord("swd_header").y,
        scale=(-1, 1),
        pin_pitch=hardware.coord("pin_pitch_h", raw=True),
        label_start=(100, 200),
        label_pitch=(0, 32),
        labels=data.swd_header,
        leaderline=lline.Curved(direction="vh"),
    )
)

# Title and description
title_block = diagram.panel_02.add(
    TextBlock(
        data.title,
        x=20,
        y=30,
        line_height=18,
        tag="panel title_block",
    )
)

diagram.panel_02.add(
    TextBlock(
        data.description.split("\n"),
        x=20,
        y=60,
        width=title_block.width,
        height=diagram.panel_02.height - title_block.height,
        line_height=18,
        tag="panel text_block",
    )
)

# Legend
legend = diagram.panel_02.add(
    Legend(
        data.legend,
        x=340,
        y=8,
        max_height=132,
    )
)
