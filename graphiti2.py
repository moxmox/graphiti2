import sys
from PyQt5 import QtWidgets as widgets
from string import ascii_lowercase
import math
import re
import matplotlib.pyplot as plt

class Math_Function:

    def __init__(self):
        self.domain = list()
        self.range = list()
        for n in range(-100, 101):
            self.domain.append(n)

    def reset_range(self):
        self.range.clear()

    def quadratic(self, x=None, a=None, b=None, c=None):
        self.reset_range()
        plt.title('Quadratic Function')
        fig = plt.gcf()
        ax = fig.gca()
        ax.spines['left'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        if a is 0:
            a = 1
        if x is not None and x is not 0:
            y = self.__compute_quadratic__(a=a, b=b, c=c, x=x)
            label = 'f(x)=' + str(a) + '*' + str(x) + '^2+' + str(b) + '*' + str(x) + '+' + str(c)
            plt.plot(x, y, "*r", label=label)
            plt.legend(loc='upper left')
            plt.show()
        else:
            for n in self.domain:
                y = self.__compute_quadratic__(a=a, b=b, c=c, x=n)
                self.range.append(y)
            plt.plot(self.domain, self.range, '--r', label='f(x)=ax^2+bx+c')
            plt.legend(loc='upper left')
            plt.show()

    def __compute_quadratic__(self, a=1, b=0, c=0, x=1):
        return a*(math.pow(x, 2)) + b*(x) + c #quadratic equation


    def linear(self, x=None, a=None, b=None): ## range should be cleared before beginning a new function
        self.reset_range()
        plt.title('Linear Function')
        fig = plt.gcf()
        ax = fig.gca()
        ax.spines['left'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        if x is not None and x is not 0:
            y = self.__compute_linear__(x=x, a=a, b=b)
            label = 'f(x)=' + str(a) + '*' + str(x) + '+' + str(b)
            plt.plot(x, y, '*r', label=label)
            plt.legend(loc='upper left')
            plt.show()
        else:
            for n in self.domain:
                y = self.__compute_linear__(a=a, b=b, x=n)
                self.range.append(y)
            plt.plot(self.domain, self.range, '--r', label='f(x)=ax+b')
            plt.legend(loc='upper left')
            plt.show()

    def __compute_linear__(self, a=1, x=1, b=1):
        return a*x+b #linear equation

    def exponential(self, x=None, z=None, a=1):
        self.reset_range()
        plt.title('Exponential Function')
        fig = plt.gcf()
        ax = fig.gca()
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        if z is None or z is 0:
            return
        
        if x is not None and z is not None:
            plt.plot(x, (a * math.pow(x, z)), '*r', label='f(x)=ax^z')
            plt.legend(loc='upper left')
            plt.show()
            return

        if z is not None or z is not 0:
            for n in self.domain:
                self.range.append(a * math.pow(n, z))
        plt.plot(self.domain, self.range, '--r', label='f(x)=ax^z')  
        plt.legend(loc='upper left')
        plt.show()


    def square(self, x=None, a=None):
        self.reset_range()
        plt.title('Square Of a Number')
        fig = plt.gcf()
        ax = fig.gca()
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position(('axes', 0.01))
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        if x is not None:
            if a is not 0:
                label = 'f(x)' + str(a) + '*' + str(x) +'^2'
                plt.plot(x, a*(x*x), '*r', label=label)
            else:
                plt.plot(x, (x*x), '*r', label='f(x)=ax^2')
            plt.legend(loc='upper left')
            plt.show()
            return

        if a is not 0:
            for n in self.domain:
                self.range.append(a*(n*n))
        else:
            for n in self.domain:
                self.range.append(n*n)
        plt.plot(self.domain, self.range, '--r', label='f(x)=ax^2')
        plt.legend(loc='upper left')
        plt.show()
        

    def cube(self, x=None, a=None):
        self.reset_range()
        plt.title('Cube Of a Number')
        fig = plt.gcf()
        ax = fig.gca()
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        if x is not 0:
            if a is not 0 and a is not None:
                label = 'f(x)=' + str(a) + '*' + str(x) +'^3'
                plt.plot(x, a*(math.pow(x, 3)), '*r', label=label)
            else:
                plt.plot(x, math.pow(x, 3), '*r', label='f(x)=ax^3')
            plt.legend(loc='upper left')
            plt.show()
            return

        if a is not 0:
            for n in self.domain:
                self.range.append(a*(n*n*n))
        else:
            for n in self.domain:
                self.range.append(n*n*n)
        plt.plot(self.domain, self.range, '--r', label='f(x)=ax^3')
        plt.legend(loc='upper left')
        plt.show()

class Window():

    def init_ui(self):
        self.app = widgets.QApplication(sys.argv)
        self.w = widgets.QWidget()
        self.w.setGeometry(100, 100, 600, 200)

        self.btn = widgets.QPushButton("Graph Selected Function")
        self.btn.clicked.connect(self.click)
        self.domain_chkbox = widgets.QCheckBox('plot single point')
        self.domain_chkbox.stateChanged.connect(self.checked)

        self.out_layout_vbox = widgets.QVBoxLayout()
        self.out_layout_vbox.addWidget(self.btn)
        self.out_layout_vbox.addWidget(self.domain_chkbox)

        self.inner_vbox_layout = widgets.QVBoxLayout()
        self.out_layout_vbox.addLayout(self.inner_vbox_layout)
        self.out_layout_vbox.addStretch()

        self.var_row1_hbox = widgets.QHBoxLayout()
        self.var_row2_hbox = widgets.QHBoxLayout()
        self.row1_hbox = widgets.QHBoxLayout()
        self.row2_hbox = widgets.QHBoxLayout()

        self.var_labels = dict()
        self.var_edits = dict()

        self.letter_keys = list()
        self.letter_keys.append('a')
        self.letter_keys.append('b')
        self.letter_keys.append('c')
        self.letter_keys.append('x')
        self.letter_keys.append('y')
        self.letter_keys.append('z')
        for key in self.letter_keys:
            self.var_labels[key] = widgets.QLabel(key + ":")
            self.var_edits[key] = widgets.QLineEdit()
            if key == 'a' or key == 'b' or key == 'c':
                self.var_row1_hbox.addWidget(self.var_labels[key])
                self.var_row1_hbox.addWidget(self.var_edits[key])
            elif key == 'x' or key == 'y' or key == 'z':
                self.var_row2_hbox.addWidget(self.var_labels[key])
                self.var_row2_hbox.addWidget(self.var_edits[key])

        self.var_edits['y'].setEnabled(False)
        self.var_edits['x'].setEnabled(False)

        #radio buttons for graphing functions
        self.exp_func_radio = widgets.QRadioButton('ax^z')
        self.sqr_func_radio = widgets.QRadioButton('ax^2')
        self.cubic_func_radio = widgets.QRadioButton('ax^3')
        self.linear_func_radio = widgets.QRadioButton('ax+b')
        self.quadratic_func_radio = widgets.QRadioButton('ax^2+bx+c')

        #button group additons
        self.btn_group = widgets.QButtonGroup()
        self.exp_func_radio.setChecked(True)
        self.btn_group.addButton(self.exp_func_radio)
        self.btn_group.addButton(self.sqr_func_radio)
        self.btn_group.addButton(self.cubic_func_radio)
        self.btn_group.addButton(self.linear_func_radio)
        self.btn_group.addButton(self.quadratic_func_radio)

        #row 1 & 2 hboxes
        self.row1_hbox.addWidget(self.exp_func_radio)
        self.row1_hbox.addWidget(self.sqr_func_radio)
        self.row1_hbox.addWidget(self.cubic_func_radio)
        self.row2_hbox.addWidget(self.linear_func_radio)
        self.row2_hbox.addWidget(self.quadratic_func_radio)

        #vbox layouts
        self.inner_vbox_layout.addLayout(self.var_row1_hbox)
        self.inner_vbox_layout.addLayout(self.var_row2_hbox)
        self.inner_vbox_layout.addStretch()
        self.inner_vbox_layout.addLayout(self.row1_hbox)
        self.inner_vbox_layout.addStretch()
        self.inner_vbox_layout.addLayout(self.row2_hbox)

        self.w.setLayout(self.out_layout_vbox)

        self.w.setWindowTitle('Graphiti')
        self.w.show()
        sys.exit(self.app.exec_())

    def checked(self):
        if self.domain_chkbox.isChecked():
            self.var_edits['x'].setEnabled(True)
        else:
            self.var_edits['x'].setEnabled(False)

    def click(self):
        click_vars = dict()
        f = Math_Function()
        for key in self.letter_keys:
            if self.var_edits[key].isEnabled():
                tmp = self.var_edits[key].text()
                pattern = re.compile(r'[+-]?\d+')            #(r"[-][0-9]+")
                data = re.findall(pattern, tmp)
                if data:
                    click_vars[key] = int(data[0])
                else:
                    click_vars[key] = 0
            else:
                click_vars[key] = 0
        if self.btn_group.checkedButton() == self.sqr_func_radio:
            if not self.var_edits['x'].isEnabled():
                f.square(a=click_vars['a'])
            else:
                f.square(click_vars['x'], a=click_vars['a'])
        elif self.btn_group.checkedButton() == self.exp_func_radio:
            if not self.var_edits['x'].isEnabled():
                if click_vars['a'] is not 0:
                    f.exponential(a=click_vars['a'], z=click_vars['z'])
                else:
                    f.exponential(z=click_vars['z'])
            else:
                if click_vars['a'] is not 0:
                    f.exponential(x=click_vars['x'], z=click_vars['z'], a=click_vars['a'])
                else:
                    f.exponential(x=click_vars['x'], z=click_vars['z'])
        elif self.btn_group.checkedButton() == self.linear_func_radio:
            if self.var_edits['x'].isEnabled():
                f.linear(x=click_vars['x'], a=click_vars['a'], b=click_vars['b'])
            else:
                f.linear(a=click_vars['a'], b=click_vars['b'])
        elif self.btn_group.checkedButton() == self.quadratic_func_radio:
            if self.var_edits['x'].isEnabled():
                f.quadratic(a=click_vars['a'], b=click_vars['b'], c=click_vars['c'], x=click_vars['x'])
            else:
                f.quadratic(a=click_vars['a'], b=click_vars['b'], c=click_vars['c'])
        elif self.btn_group.checkedButton() == self.cubic_func_radio:
            if not self.var_edits['x'].isEnabled():
                f.cube(x=click_vars['x'], a=click_vars['a'])
            else:
                f.cube(a=click_vars['a']) #x=click_vars['x'] recently removed \note for debug\

def main():
    window = Window()
    window.init_ui()

if __name__ == "__main__":
    main()