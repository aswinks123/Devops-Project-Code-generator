


#Importing Modules
import argparse
from pywebio.input import *
from pywebio.output import *
from flask import  Flask
from pywebio.session import *
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
import qrcode
from PIL import Image
import re
import time
from pywebio.session import run_js
from pywebio import start_server
import barcode
#from barcode import EAN13
from barcode import Code39

#-----------------------------------------------------------------------------------------------------------------------

#Creating  a flask appls


app=Flask(__name__)



#Main function that creates the QR code

def QR():

    put_html(r"""<h1  align="center"><strong> CODE GENERATOR</strong></h1>""")  # App Name in Main screen
    # Drop-down selection


    gift = select('Choose a Service to get started!', ['QR Code', 'Barcode'])

    if gift == 'QR Code':

        put_html(r"""<h2  align="center"><strong>QRCode Generator</strong></h2>""")  # App Name in Main screen
        img = open('logo.png', 'rb').read()  # logo
        put_image(img, width='100px')  # size of image
        foreground = ['Black', 'Red', 'Blue', 'White', 'Yellow', 'Cyan', 'Magenta']
        background = ['White', 'Red', 'Blue', 'Black', 'Yellow', 'Cyan', 'Magenta']

        def check_age(age):
            if age > 10:
                return 'Maximum supported size is 10'
            elif age < 1:
                return 'Minimum supported size is 1'







        datas= input_group('Customise the QR Code', [
            input('Text', type=TEXT, name='text', required=True,
                  help_text='Required'),

            input('Enter Border size', type=NUMBER, name='border',validate=check_age),


            select('Select Foreground color', options=foreground, name='fg'),
            select('Select Background color', options=background, name='bg'),


            actions(" ", [
                {'label': 'Generate', 'value': 'submit'},
                {'label': 'Clear', 'type': 'reset', 'color': 'danger'},

            ], name='actions'),
        ])

        if datas['fg']==datas['bg']:
            #put_error("Both FG and BG cannot be the same")
            popup('Error', [
                put_html('<h2>Both Foreground and Background colors cannot be the same</h2>'),
                put_buttons(['close'], onclick=lambda _: run_js('window.location.reload()'))

            ])
            time.sleep(20)
            run_js('window.location.reload()')

        # Adding Progress bar
        put_text(" ")
        put_processbar('bar')
        for i in range(1, 8):
            set_processbar('bar', i / 7)
            time.sleep(0.1)




        # Creating QR code using the provided data

        feature = qrcode.QRCode(version=1, box_size=40, border=datas['border'])
        feature.add_data(datas['text'])
        feature.make(fit=True)
        img = feature.make_image(fill_color=datas['fg'], back_color=datas['bg'])
        img.save("qr-image.jpg")

        # outputing the text and image
        # put_text("Your QR Code is Created.")
        put_html(r"""<h3  align="center"><strong>Your QR Code is Created</strong></h3>""")



        img = open('qr-image.jpg', 'rb').read()
        put_image(img, width='250px')

        content = open('qr-image.jpg', 'rb').read()

        put_file('qr-image.jpg', content, 'Download QR code')


        def liked():

           put_info("Thank you for your feedback!")

        # To show About section
        def clicked():
            popup('About Us', [
                put_html('<h2>Created by Team InsightIQ</h2>'),
                put_html('<h3>This project is created using Python,Azure,Jenkins,Terraform,Ansible,Nagios,Datadog</h3>'),
                'Find More @ InsightIQ',  # equal to put_text('plain html: <br/>')
                put_buttons(['close'], onclick=lambda _: close_popup())
            ])

        def btn_click(btn_val):  # To do function of the 3 buttons

            if btn_val == 'About':  # btn_val contain the text of button
                clicked()
            elif btn_val == 'Generate new Code':
                run_js('window.location.reload()')
            elif btn_val == 'Like':
                liked()
        

        put_buttons(['Generate new Code', 'About', 'Like'], onclick=btn_click)  # Buttons

    if gift=='Barcode':
        put_html(r"""<h2  align="center"><strong>Barcode Generator</strong></h2>""")  # App Name in Main screen
        img = open('barcodelogo.png', 'rb').read()  # logo
        put_image(img, width='100px')  # size of image
        put_html(r"""<h3 align="center"><strong> </strong></h3>""")

        bdatas = input_group('Enter the product number to generate Barcode ', [
            input(type=NUMBER, name='text', required=True,
                  help_text='Required'),

            actions(" ", [
                {'label': 'Generate', 'value': 'submit'},
                {'label': 'Clear', 'type': 'reset', 'color': 'danger'},

            ], name='actions'),
        ])

        put_text(" ")
        # Adding Progress bar
        put_processbar('bar')
        for i in range(1, 8):
            set_processbar('bar', i / 7)
            time.sleep(0.1)

        put_html(r"""<h3  align="center"><strong>Your Barcode Code is Created</strong></h3>""")
        tt=bdatas['text']
        tt=str(tt)



        ####

        from barcode.writer import ImageWriter
        #barcode_format = barcode.get_barcode_class('code39')


        my_barcode = Code39(tt, writer=ImageWriter(),add_checksum=False)
        #my_barcode = barcode_format(tt, writer=ImageWriter(),add_checksum=False)
        my_barcode.save("barcode")





        ####

        img = open('barcode.png', 'rb').read()
        put_image(img, width='350px')

        content = open('barcode.png', 'rb').read()
        put_file('barcode.png', content, 'Download barcode')

        # To show About sessiono
        def clicked():
            popup('About Us', [
                put_html('<h2>Created by Team InsightIQ</h2>'),
                put_html('<h3>This project is created using Python,Azure,Jenkins,Terraform,Ansible,Nagios,Datadog</h3>'),
                'Find More @ InsightIQ',  # equal to put_text('plain html: <br/>')
                put_buttons(['close'], onclick=lambda _: close_popup())
            ])

        # To register the like count(in beta stage)
        def liked():

            put_info("Thank you for your feedback!")

        def btn_click(btn_val):  # To do function of the 3 buttons

            if btn_val == 'About':  # btn_val contain the text of button
                clicked()
            elif btn_val == 'Generate new Code':
                run_js('window.location.reload()')
            elif btn_val == 'Like':
                liked()
            elif btn_val == 'Feedback':
                # Text Area
                fback = textarea('Enter your feedback', rows=3, placeholder='Some text')

        put_buttons(['Generate new Code', 'About', 'Like', 'Feedback'], onclick=btn_click)  # Buttons




# To allow reloading of web browser and mentioning the port
app.add_url_rule('/qr', 'webio_view', webio_view(QR), methods=['GET', 'POST', 'OPTIONS'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8083)
    args = parser.parse_args()

    start_server(QR, port=args.port,debug=True)
