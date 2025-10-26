python watermark_wizard.py .\input_images\white_watermark .\temp_images --logo dopyw.png --position top-right --opacity 250 --size 9 --offset 1,1 && ^
python watermark_wizard.py .\input_images\black_watermark .\temp_images --logo dopyb.png --position top-right --opacity 250 --size 9 --offset 1,1 && ^
python watermark_wizard.py .\temp_images .\output_images --logo intbits.png --position top-left --opacity 250 --size 10 --offset 0,1 && ^
rmdir /s /q .\temp_images
