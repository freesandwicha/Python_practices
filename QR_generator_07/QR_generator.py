# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 17/8/2023 8:12 pm

import qrcode

class FirstQR:
    def __init__(self, size: int, padding: int ):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, fg: str, bg: str):
        user_input:str = input('Enter the text:')

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            print(f'Successfully created {file_name}! ')
        except Exception as e :
            print(f'Error: {e}')


def main():
    myqr = FirstQR(23,2)
    myqr.create_qr('sample.png', 'black','yellow')

if __name__ == '__main__':
    main()

