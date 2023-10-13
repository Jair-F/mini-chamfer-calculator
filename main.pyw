import json
import os
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QGridLayout, QComboBox, QWidget, QSizePolicy, QLineEdit
import PyQt5.QtCore
from PyQt5.QtGui import QDoubleValidator

config_file_name = "./config.json"
tool_list = None

def tool_in_tool_list(diameter:str):
    try:
        tool_list["tools"][diameter]
    except KeyError:
        return False
    
    return True
    
class Application():
    def __init__(self):
        self.selected_tool = None

        self.app = QApplication([])

        self.main_window = QMainWindow()
        self.main_window.setWindowFlags(PyQt5.QtCore.Qt.WindowStaysOnTopHint) # always on top
        self.main_window.setWindowTitle("mini chamfer calculator")
        #self.main_window.setMinimumSize(550,300)
        #self.main_window.setMaximumSize(800,800)
        self.main_window.setFixedSize(370, 140)
        #self.main_window.show()

        self.window_layout = QGridLayout()
        self.window_layout.setSpacing(0)
        #self.window_layout.setContentsMargins(3,5,5,3)
        #self.size_policy = QSizePolicy()
        #self.size_policy.setHorizontalPolicy(QSizePolicy.Policy.Expanding)
        #self.size_policy.setVerticalPolicy(QSizePolicy.Policy.Expanding)

        self.layout_widgt = QWidget(self.main_window)
        self.layout_widgt.setFixedSize(self.main_window.frameSize())
        #self.layout_widgt.setContentsMargins(0,0,0,0)
        #self.layout_widgt.setSizePolicy(self.size_policy)

        self.tool_label = QLabel("Text", self.layout_widgt)
        #self.tool_label.show()

        self.tool_combo_box = QComboBox(self.layout_widgt)
        for tool in tool_list["tools"].items():
            self.tool_combo_box.addItem(tool[1]["description"], userData=tool[0])
        self.tool_combo_box.setMinimumSize(280, 15)
        self.tool_combo_box.currentTextChanged.connect(self._handle_tool_changed)
        #self.tool_combo_box.show()

        self.chamf_label = QLabel("chamfer size", self.layout_widgt)

        self.chamf_size = QLineEdit("0.2", self.layout_widgt)
        self.chamf_size.setMaximumWidth(80)
        self.validator = QDoubleValidator(self.chamf_size, decimals=2)
        self.validator.setLocale(PyQt5.QtCore.QLocale("en_US")) # for .1 numbers
        self.chamf_size.setValidator(self.validator)
        self.chamf_size.textChanged.connect(self._calc_update_data)

        self.z_lvl_label = QLabel("Z-Level", self.layout_widgt)
        self.z_lvl = QLineEdit(self.layout_widgt)
        self.z_lvl.setMaximumWidth(80)
        self.z_lvl.setReadOnly(True)

        self.geom_offs_label = QLabel("geom. offset", self.layout_widgt)
        self.geom_offs = QLineEdit(self.layout_widgt)
        self.geom_offs.setMaximumWidth(80)
        self.geom_offs.setReadOnly(True)

        #self.cut_dia_label = QLabel("cut. dia", self.layout_widgt)
        #self.cut_dia = QLineEdit(self.layout_widgt)
        #self.cut_dia.setMaximumWidth(80)
        #self.cut_dia.setReadOnly(True)
        #self.cut_dia.setDisabled(True)

        self.window_layout.addWidget(self.tool_label, 0, 0)
        self.window_layout.addWidget(self.tool_combo_box, 0, 1)
        self.window_layout.addWidget(self.chamf_label, 1, 0)
        self.window_layout.addWidget(self.chamf_size, 1, 1)
        self.window_layout.addWidget(self.z_lvl_label, 2, 0)
        self.window_layout.addWidget(self.z_lvl, 2, 1)
        self.window_layout.addWidget(self.geom_offs_label, 3, 0)
        self.window_layout.addWidget(self.geom_offs, 3, 1)
        #self.window_layout.addWidget(self.cut_dia_label, 4, 0)
        #self.window_layout.addWidget(self.cut_dia, 4, 1)

        self.layout_widgt.setLayout(self.window_layout)
        self.layout_widgt.show()
        self.main_window.show()

        self._handle_tool_changed(self.tool_combo_box.currentText())

    def _handle_tool_changed(self, tool_descr):
        for tool in tool_list["tools"].items():
            if tool[1]["description"] == tool_descr:
                self.selected_tool = tool[1]
        self._calc_update_data(self.chamf_size.text())

    def _calc_update_data(self, _chamf_size:str):
        # checking if _chamf_size is valid input
        try:
            float(_chamf_size)
        except ValueError:
            self.z_lvl.setText("")
            #self.cut_dia.setText("")
            self.geom_offs.setText("")
            return
        
        #print(self.selected_tool)

        d = round((self.selected_tool["top_diameter"] - self.selected_tool["bottom_diameter"])/2, ndigits=3)
        z_lvl = round(-(d + self.selected_tool["cl"] + tool_list["safety"]), ndigits=3)
        g_offset = round((d - self.selected_tool["cl"] - float(_chamf_size)), ndigits=3)
        
        if float(_chamf_size) >= self.selected_tool["height"]: # chamfer not to big
            self.z_lvl.setText("")
            #self.cut_dia.setText("")
            self.geom_offs.setText("")
            return

        #self.cut_dia.setText(str(self.selected_tool["bottom_diameter"]))
        self.z_lvl.setText(str(z_lvl))
        self.geom_offs.setText(str(g_offset))

    def run(self):
        self.app.exec_()
    


if __name__ == "__main__":

    config_file_str = ""
    file_size = os.path.getsize(filename=config_file_name)
    with open(config_file_name, 'r') as file:
        config_file_str = file.read(file_size)
        tool_list = json.loads(config_file_str)
    
    app_window = Application()
    app_window.run()
    