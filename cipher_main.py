# Libraries needed
import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi

# The only window we need 
class window(QDialog):
    def __init__(self):
        super(window, self).__init__()

        # Load the .ui file
        loadUi("main.ui", self)

        # Connect graphical components to behavior functions
        self.run.clicked.connect(self.process) # run button behave with the process function
        self.encode.clicked.connect(self.coder) # encode radiobutton behave with the coder function
        self.decode.clicked.connect(self.coder) # decode radiobutton behave with the coder function
        
        # Global variable to identify which radiobutton is checked
        self.version = 0

    # Identify whether user want to encode or decode 
    def coder(self):

        if self.encode.isChecked():
            self.version = 1
        elif self.decode.isChecked():
            self.version = 2

    # Run the selected method between code or decode
    def process(self):
        text = self.text.toPlainText() # Get the written text 

        # Helpers 
        alphabet = 'abcdefghijklmnopqrstuvwxyz' # This is the latin alphabet
        alpha = {alphabet[i]:i+1 for i in range(26)} # A dictionary of each letter and their position in the alphabet
        temp, num = [], 0 

        """
        @temp wil contains the transformed letters
        @num the position to do the transformation.

        Also we make sure @num initial value is 0 to indicate we are at the beginning of a word.
        As 0 is not a letter position in @alpha, only the next values of @num will refer to a letter 
        position.
        """

        # When user hits run button with written message and selected method, start the magic
        if text and self.version:

            # My not so optimized way of Cipher encoding
            if self.version == 1:
                for t in text:
                    t = t.lower()

                    if t in alphabet: # Alpha character

                      if num == 0: # If starting the word
                        num += alpha[t]
                        temp.append(alphabet[num - 1].upper())

                      else: # Elsewhere
                        num += alpha[t]

                        # Handle exceeding 26 range
                        if num < 26:
                          temp.append(alphabet[num - 1].upper())
                        else:
                          temp.append(alphabet[num - 27].upper())

                        num = alpha[t] # Saving the position for next letter transformation

                    else: # Non Alpha character
                      temp.append(t)

                self.visualizer.setPlainText(''.join(temp)) # Render the encryption in the bottom prompt

            # My not so optimized way of Cipher decoding
            else:
                temp, num = [text[0]], alpha[text[0].lower()] # Keep the first letter and its position in the alphabet

                for t in text[1:]: # Then you can do the flip flop for the rest
                    t = t.lower()

                    if t in alphabet:
                        num = alpha[t] - num
                        temp.append(alphabet[num - 1])

                        if num < 0: # Prevent error from negative index
                            num += 26 

                    else:
                        temp.append(t)

                self.visualizer.setPlainText(''.join(temp)) # Render the encryption in the bottom prompt

        # When user hits run button without written message and selected method, put a reminder in the bottom prompt
        else:
            self.visualizer.setPlainText('Verify that you pasted a message AND selected a method.')




# Build the app from all we did previously
app = QApplication(sys.argv)
mainwindow = window()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setWindowTitle("CIPHER ENCRYPTING -- v1.0")
widget.setFixedWidth(400) # App window width
widget.setFixedHeight(500) # App window height
widget.show()
sys.exit(app.exec_())
