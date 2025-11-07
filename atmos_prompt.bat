python watermark_wizard.py .\input_images\dopy_w__atmos_w .\temp_white_images --logo dopyw.png --position top-right --opacity 250 --size 10 --offset 1,1 && ^
python watermark_wizard.py .\input_images\dopy_w__atmos_b .\temp_white_images --logo dopyw.png --position top-right --opacity 250 --size 10 --offset 1,1 && ^
python watermark_wizard.py .\input_images\dopy_b__atmos_w .\temp_black_images --logo dopyb.png --position top-right --opacity 250 --size 10 --offset 1,1 && ^
python watermark_wizard.py .\input_images\dopy_b__atmos_b .\temp_black_images --logo dopyb.png --position top-right --opacity 250 --size 10 --offset 1,1 && ^
python watermark_wizard.py .\temp_white_images .\output_images --logo atmosw.png --position top-left --opacity 250 --size 10 --offset 1,1 && ^
python watermark_wizard.py .\temp_black_images .\output_images --logo atmosb.png --position top-left --opacity 250 --size 10 --offset 1,1 && ^
rmdir /s /q .\temp_white_images && ^
rmdir /s /q .\temp_black_images
