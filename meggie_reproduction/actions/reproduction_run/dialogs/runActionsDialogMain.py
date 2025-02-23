"""Contains a class for logic of the run actions dialog."""

import json

from PyQt5 import QtWidgets

from meggie_reproduction.actions.reproduction_run.dialogs.runActionsDialogUi import (
    Ui_RunActionsDialog,
)

from meggie.mainwindow.dynamic import find_all_action_specs

from meggie.utilities.messaging import exc_messagebox
from meggie.utilities.messaging import messagebox
from meggie.utilities.filemanager import homepath


class RunActionsDialog(QtWidgets.QDialog):
    """Contains logic for the run actions dialog."""

    def __init__(self, parent, experiment):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_RunActionsDialog()
        self.ui.setupUi(self)

        self.experiment = experiment
        self.parent = parent

        self.action_log = None
        self.action_specs = find_all_action_specs()
        self.current_subject = None

        self.actions_available = []
        self.actions_done = []

        self.ui.labelBrowseCurrentSelectionFilename.setText("")
        self.ui.groupBoxSubject.setEnabled(False)
        self.ui.comboBoxSubject.clear()
        self.ui.listWidgetAvailable.clear()
        self.ui.listWidgetDone.clear()
        self.ui.textBrowserActionsInfo.setPlainText("")
        self.ui.groupBoxActions.setEnabled(False)

        # Add handler for subject change
        self.ui.comboBoxSubject.currentTextChanged.connect(self.on_subject_changed)

    def on_subject_changed(self, value):
        if not value:
            return

        if not self.actions:
            return

        # sanity check to not update if subject did not really change
        if self.current_subject == value:
            return
        self.current_subject = value

        # get installed actions
        installed_actions = [spec[1] for spec in self.action_specs.values()]

        # ensure all actions are available in the installation
        for action in self.action_log[value]:
            if action["id"] not in installed_actions:
                messagebox(
                    self, f"The log contains {action['id']} that is not installed."
                )

        # update available actions
        self.actions_available = []
        self.ui.listWidgetAvailable.clear()
        for action in self.action_log[value]:

            # get the action spec
            action_spec = self.action_specs.get(action["id"])
            if action_spec:
                self.actions_available.append(action["id"])
                self.ui.listWidgetAvailable.addItem(
                    f"{action_spec[2]['name']} ({action['desc']})"
                )

        self.ui.groupBoxActions.setEnabled(True)

    def on_pushButtonSourceBrowse_clicked(self, checked=None):
        if checked is None:
            return

        fname, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open Action Log", homepath(), "JSON Files (*.json);;All Files (*)"
        )
        if not fname:
            return

        try:
            with open(fname) as f:
                self.action_log = json.load(f)
        except Exception as exc:
            exc_messagebox(self, exc)

        if not self.action_log:
            messagebox(self, "The selected action log seems empty.")

        if self.action_log:
            self.ui.labelBrowseCurrentSelectionFilename.setText(str(fname))
            self.ui.groupBoxSubject.setEnabled(True)
            self.ui.comboBoxSubject.addItems(sorted(self.action_log.keys()))

    def on_pushButtonClose_clicked(self, checked=None):
        if checked is None:
            return

        self.close()

    def closeEvent(self, event):
        """Initialize the ui when the dialog is closed."""
        self.parent.initialize_ui()
        event.accept()
