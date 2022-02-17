from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QFontDialog, QColorDialog
from NotePadDemo import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox as qMB
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt6.QtCore import QFileInfo, Qt

class NotePadWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.actionNew.triggered.connect(self.file_new)
        self.actionSave.triggered.connect(self.save_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionPrint.triggered.connect(self.print_file)
        self.actionPrint_Preview.triggered.connect(self.preview_dialog)
        self.actionExport_PDF.triggered.connect(self.export_pdf)
        self.actionQuit.triggered.connect(self.exit_app)

        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)

        self.actionCut.triggered.connect(self.textEdit.cut)
        self.actionCopy.triggered.connect(self.textEdit.copy)
        self.actionPaste.triggered.connect(self.textEdit.paste)

        self.actionBold.triggered.connect(self.text_bold)
        self.actionItalic.triggered.connect(self.italic)
        self.actionUnderline.triggered.connect(self.underline)

        self.actionLeft.triggered.connect(self.align_left)
        self.actionRight.triggered.connect(self.align_right)
        self.actionCenter.triggered.connect(self.align_center)
        self.actionJustify.triggered.connect(self.align_justify)

        self.actionFont.triggered.connect(self.font_dialog)
        self.actionColor.triggered.connect(self.color_dialog)
        self.actionAbout_App.triggered.connect(self.about)

    def maybe_save(self):
        if not self.textEdit.document().isModified():
            return True

        ret = qMB.warning(self, "Application",
                            "The document has been modified. \nDo you want to save your document?",
                          qMB.StandardButton.Save | qMB.StandardButton.Discard | qMB.StandardButton.Cancel)
        if ret == qMB.StandardButton.Save:
            return self.save_file()
        if ret == qMB.StandardButton.Cancel:
            return False
        return True

    def save_file(self):
        filename = QFileDialog.getSaveFileName(self, "Save File")

        if filename[0]:
            f = open(filename[0], 'w')

            with f:
                text = self.textEdit.toPlainText()
                f.write(text)
                qMB.about(self, "Save File", "File has been saved")

    def file_new(self):
        if self.maybe_save():
            self.textEdit.clear()

    def open_file(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", '/home')
        print(fname[0])
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

    def print_file(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog()
        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.textEdit.print(printer)

    def preview_dialog(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.print_preview)
        previewDialog.exec()

    def print_preview(self, printer):
        self.textEdit.print(printer)

    def export_pdf(self):
        fn, _ = QFileDialog.getSaveFileName(self, 'Export PDF', "*.pdf")
        if fn != "":
            if QFileInfo(fn).suffix() == "": fn += '.pdf'
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print(printer)

    def exit_app(self):
        print("exit_app")
        self.close()

    def text_bold(self):
        font = QFont()
        font.setBold(True)
        self.textEdit.setFont(font)

    def italic(self):
        font = QFont()
        font.setItalic(True)
        self.textEdit.setFont(font)

    def underline(self):
        font = QFont()
        font.setUnderline(True)
        self.textEdit.setFont(font)

    def align_left(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def align_right(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight)

    def align_center(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def align_justify(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify)

    def font_dialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def color_dialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def about(self):
        qMB.about(self, "About App", "This is simple notepad app with PyQt6")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Note = NotePadWindow()
    sys.exit(app.exec())
