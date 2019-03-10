from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication
import src.ratslap as ratslap
from src.db_helper import DBHelper, OperationalError
from src.helper_widgets import CommandEditor
from UI.ui_rattrap import Ui_Rattrap


class RattrapWindow(QtWidgets.QMainWindow, Ui_Rattrap):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(303,477)
        self.move(QtWidgets.QApplication.desktop().screen().rect().center() - self.rect().center())

        self.current_mode_name = None

        # Grouping similar items together.
        self.radio_buttons = [getattr(self, "mode" + i) for i in "123"]
        self.combo_boxes = [self.color, self.rate]
        self.unchangeable_items = [getattr(self, "dpi" + i) for i in "1234"] + [self.dpi_shift]
        self.buttons = [self.right, self.middle, self.left]
        self.buttons.extend([getattr(self, "g" + str(i)) for i in range(4, 10)])
        self.action_names = ["reset", "import", "export", "apply"]

        self.bind_functions_to_buttons()
        self.set_icons()
        self.mode1.setChecked(True)
        self.conn = DBHelper("settings.db")
        self.show()
        try:
            ratslap_path = self.conn.select("file_paths", ("path",), program_name="ratslap").fetchone()[0]
        except OperationalError:
            ratslap_path = self.get_ratslap_path()
        self.ratslap = ratslap.Ratslap(ratslap_path)
        for widget in self.buttons + self.radio_buttons + [self.button_apply]:
            widget.setEnabled(True)
        self.set_current_mode()

    def set_icons(self):
        for name in self.action_names:
            button = getattr(self, "button_" + name)
            image_path = "./images/" + name + "_icon.png"
            icon = QIcon()
            icon.addPixmap(QPixmap(image_path))
            button.setIcon(icon)

    def bind_functions_to_buttons(self):
        for radio_btn in self.radio_buttons:
            radio_btn.clicked.connect(self.set_current_mode)
        for combo_box in self.combo_boxes:
            combo_box.currentTextChanged.connect(self.combo_box_changed)
        for button in self.buttons:
            button.clicked.connect(self.assign_shortcut)
        for name in self.action_names:
            button = getattr(self, "button_" + name)
            action = getattr(self, name + "_action")
            button.clicked.connect(action)

    def reset_action(self):
        for i in range(3, 6):
            msg_box = QtWidgets.QMessageBox
            response = msg_box.question(self, f"Reset F{i}?", f"Do you want to reset profile F{i} to its defaults?",
                                        msg_box.No | msg_box.NoToAll | msg_box.YesToAll | msg_box.Yes)
            if response == msg_box.YesToAll:
                self.ratslap.reset("all")
                self.conn.drop_table("profiles")
                self.set_current_mode()
                break
            elif response == msg_box.Yes:
                self.ratslap.reset(i)
                self.conn.delete_row("profiles", name="f" + str(i))
                self.set_current_mode()
            elif response == msg_box.NoToAll:
                break

    def import_action(self):
        print("import")

    def export_action(self):
        print("export")

    def apply_action(self):
        for mode in ["f3", "f4", "f5"]:
            data = self.conn.select("profiles", "*", name=mode).fetchone()
            if data:
                cols = self.conn.get_column_names("profiles")
                changes = dict(zip(cols, data))
                self.ratslap.modify(mode, **changes)

    def assign_shortcut(self):
        button = self.sender()
        widget = CommandEditor(button, self)
        x, y = self.pos().x(), self.pos().y()
        widget.move(x + 30, y + 125)

    def get_ratslap_path(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select the path to the 'ratslap' program...")
        if path:
            self.conn.create_table("file_paths", ["program_name", "path"])
            self.conn.insert_values("file_paths", **{"program_name": "ratslap", "path": path})
            return path

    def set_current_mode(self):
        self.current_mode_name = "f" + str([i.isChecked() for i in self.radio_buttons].index(True) + 3)  # f3, f4 or f5
        self.ratslap.select_mode(self.current_mode_name)
        current_mode = self.get_mode(self.current_mode_name)

        for item in self.combo_boxes + self.unchangeable_items + self.buttons:
            name = item.objectName()
            try:
                item.setText(current_mode[name])
            except AttributeError:
                item.setCurrentText(current_mode[name].title())

    def combo_box_changed(self, value):
        property_name = self.sender().objectName()
        self.conn.update_value("profiles", property_name, value.lower(), name=self.current_mode_name)

    def get_mode(self, mode):
        column_names = self.conn.get_column_names("defaults")
        self.conn.create_table("profiles", column_names)
        data = self.conn.select("profiles", "*", name=mode).fetchone()
        if data:
            return dict(zip(column_names, data))
        else:
            profile = self.ratslap.parse_mode(mode)
            self.conn.insert_values("profiles", **profile)
            return self.get_mode(mode)

    def closeEvent(self, e):
        self.conn.close()
        super(RattrapWindow, self).closeEvent(e)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main_window = RattrapWindow()
    sys.exit(app.exec_())
