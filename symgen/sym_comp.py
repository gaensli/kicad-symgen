
from collections import OrderedDict

from sym_drawing import *

ls_center = "center"
ls_floating = "floating"

ha_left = "L"
ha_center = "C"
ha_right = "R"

va_top = "T"
va_bottom = "B"

class StyleAttributes:

    pensize = 10
    fill = NoFill

    offset = 0
    show_pin_number = True
    show_pin_name = True

    font_size = 50
    angle = "H"
    visible = False    
    horiz_alignment = "C"
    vert_alignment = "C"
    italic = False
    bold = False

    pin_length = 100
    orientation = "L"   # direction
    sizenum = 50
    sizename = 50

    def __init__(self):
        pass

class SgItem:

    def __init__(self):
        pass

class SgFile:

    items = []
    def __init__(self):
        pass

class SgDoc:
    description = ""
    keywords = ""
    datasheet = ""

    def __init__(self):
        pass

class SgRawline (SgItem):

    value = ""
    def __init__(self):
        pass
            
class SgSettings:
    def __init__(self):
        self.pin_length = 200
        self.box_width = 600
        self.box_pen = 10
        self.box_fill = Background
        self.logic_fill = NoFill
        self.label_style = ls_floating
        self.pin_stacking = False

        # name_offset
        # extra_offset       
        self.pin_names_inside = False

        self.label_horiz_align = ha_right


class SgComponent (SgItem):
    name = "name"
    ref = "ref"

    def __init__(self):
        self.fplist = []
        self.units = []
        self.doc_fields = {}
        self.user_fields = []

        self.default_footprint = ""
        self.is_template = False
        self.settings = SgSettings()

class ComponentDef:
    name = "name"
    ref = "ref"

    offset = 0
    show_pin_number = True
    show_pin_name = True
    num_units = 0
    locked = "F"
    power_sym = False

    def __init__(self):
        pass


class ComponentField:
    number=0
    value="~"
    pos=Point()
    font_size=50
    angle="H"
    visible=False    
    horiz_alignment = "C"
    vert_alignment = "C"
    italic = False
    bold = False

    def __init__(self):
        pass


class LogicDesc:
    id=""
    gates=0
    description = ""
    input_type = ""
    output_type = ""
    technologies = OrderedDict ()
    packages = ""

    def __init__(self, tokens):
        self.id=tokens[0].strip()
        if tokens[1]!="":
            self.gates=int(tokens[1])
        self.description=tokens[2].strip()

        self.input_type=""
        self.output_type=""
        self.technologies = OrderedDict ()

        if len(tokens) > 3:
            self.input_type=tokens[3]
            self.output_type=tokens[4]

            if len(tokens) > 5:
                j = 5
                while j < len(tokens):
                    if tokens[j] != "None":
                        if len(tokens)-j >= 2:
                            self.technologies [tokens[j].strip()] = tokens[j+1].strip()
                            j += 1
                        else:
                            self.packages = tokens[j].strip()
                    j += 1

    def get_datasheet (self, family):
        if family in self.technologies:
            return self.technologies[family]
        else:
            for key in self.technologies:
                if key.contains (family):
                    return self.technologies[key]

            if 'Standard' in self.technologies:
                return self.technologies['Standard']
            else:
                return None
