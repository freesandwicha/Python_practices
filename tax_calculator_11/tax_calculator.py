# -*- coding = utf-8 -*-
# Worker : HAN XIA
# Motto : Practice makes perfect.
# Time : 22/8/2023 1:45 pm

import customtkinter as ctk

class TaxCalculator:
    def __init__(self):
        #Initialize the window
        self.window = ctk.CTk()
        self.window.title('Tax Calculator')
        self.window.geometry('300x200')
        self.window.resizable(False, False)

        self.padding: dict = {'padx': 20, 'pady': 10}

        #Income label and entry
        self.income_label = ctk.CTkLabel(self.window, text='Income:')
        self.income_label.grid(row=0, column=0, **self.padding)
        #The grid() method is used to specify where the widget should be placed in its parent window or frame.
        self.income_entry = ctk.CTkEntry(self.window)
        #An entry widget is like a text box that allows users to input text.
        self.income_entry.grid(row=0, column=1, **self.padding)

        # Tax label and entry
        self.tax_rate_label = ctk.CTkLabel(self.window, text='Percent:')
        self.tax_rate_label.grid(row=1, column=0, **self.padding)
        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)

        # Result label and entry
        self.result_label = ctk.CTkLabel(self.window, text='Tax:')
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, '0')
        self.result_entry.grid(row=2, column=1, **self.padding)

        #Calculate button
        self.calculate_button = ctk.CTkButton(self.window, text='Calculate', command=self.calculate_tax)
        #the method self.calculate_tax will be executed when the button is pressed.
        #This is a reference to the method.
        #self.calculate_tax(): This would immediately call and execute the calculate_tax method when the button is being set up, not when it's clicked
        self.calculate_button.grid(row=3, column=1, **self.padding)


    def update_result(self, text: str):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def calculate_tax(self):
        try:
            income: float = float(self.income_entry.get())
            tax_rate: float = float(self.tax_rate_entry.get())
            self.update_result(f'${income * (tax_rate / 100):,.2f}')
            # : is used to indicate the option format.
            #   ,  This is a formatting option to include a comma as a thousand separator.
            #   .2f This is another formatting option that rounds the number to 2 decimal places, making it suitable for monetary values.

        except ValueError:
            self.update_result('Invalid input')

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()




