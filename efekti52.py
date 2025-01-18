from PIL import ImageEnhance, Image, ImageOps

# vendosim vlerat default
default_brightness_factor = 0.85
default_brilliance_factor = 1.1
default_highlights_factor = 0.68
default_shadows_factor = 0.74
default_contrast_factor = 0.7
default_black_point_factor = 0.1
default_saturation_factor = 1.1
default_vibrancy_factor = 1.08
default_warmth_factor = 1.1
default_tint_factor = 1.35
default_sharpness_factor = 1.15
default_definition_factor = 1.23

# marrim imazhin
img = Image.open("image.jpg")

# pyesim perdoruesin nese deshiron te personalizoje imazhin
customize = input("Do you want to customize the image? (y/n) ")

# nese perdoruesi deshiron të personalizoje, kerkojme vlerat
if customize == "y":
    # i ruajm vlerat ne float
    brightness_factor = float(input("Enter brightness factor (0-1): "))
    brilliance_factor = float(input("Enter brilliance factor (0-2): "))
    highlights_factor = float(input("Enter highlights factor (0-1): "))
    shadows_factor = float(input("Enter shadows factor (0-1): "))
    contrast_factor = float(input("Enter contrast factor (0-2): "))
    black_point_factor = float(input("Enter black point factor (0-1): "))
    saturation_factor = float(input("Enter saturation factor (0-2): "))
    vibrancy_factor = float(input("Enter vibrancy factor (0-2): "))
    warmth_factor = float(input("Enter warmth factor (0-2): "))
    tint_factor = float(input("Enter tint factor (0-2): "))
    sharpness_factor = float(input("Enter sharpness factor (0-2): "))
    definition_factor = float(input("Enter definition factor (0-2): "))
else:
    # perdorim vlerat default
    brightness_factor = default_brightness_factor
    brilliance_factor = default_brilliance_factor
    highlights_factor = default_highlights_factor
    shadows_factor = default_shadows_factor
    contrast_factor = default_contrast_factor
    black_point_factor = default_black_point_factor
    saturation_factor = default_saturation_factor
    vibrancy_factor = default_vibrancy_factor
    warmth_factor = default_warmth_factor
    tint_factor = default_tint_factor
    sharpness_factor = default_sharpness_factor
    definition_factor = default_definition_factor

# aplikojme permiresimet ne imazh me vlera te caktuara nga perdoruesi ose vlerat default
brightness = ImageEnhance.Brightness(img).enhance(brightness_factor)
brilliance = ImageEnhance.Color(brightness).enhance(brilliance_factor)
highlights = ImageEnhance.Brightness(brilliance).enhance(highlights_factor)
shadows = ImageEnhance.Brightness(highlights).enhance(shadows_factor)
contrast = ImageEnhance.Contrast(shadows).enhance(contrast_factor)
brightness = ImageEnhance.Brightness(img).enhance(brightness_factor)
black_point = ImageOps.autocontrast(brightness, cutoff=black_point_factor)
saturation = ImageEnhance.Color(black_point).enhance(saturation_factor)
vibrancy = ImageEnhance.Color(saturation).enhance(vibrancy_factor)
warmth = ImageEnhance.Color(vibrancy).enhance(warmth_factor)
tint = ImageEnhance.Color(warmth).enhance(tint_factor)
sharpness = ImageEnhance.Sharpness(tint).enhance(sharpness_factor)
definition = ImageEnhance.Color(sharpness).enhance(definition_factor)


# aplikojme permiresimet ne imazh
brightness = ImageEnhance.Brightness(img).enhance(brightness_factor)
brilliance = ImageEnhance.Color(brightness).enhance(brilliance_factor)
highlights = ImageEnhance.Brightness(brilliance).enhance(highlights_factor)
shadows = ImageEnhance.Brightness(highlights).enhance(shadows_factor)
contrast = ImageEnhance.Contrast(shadows).enhance(contrast_factor)
brightness = ImageEnhance.Brightness(img).enhance(brightness_factor)
black_point = ImageOps.autocontrast(brightness, cutoff=black_point_factor)
saturation = ImageEnhance.Color(black_point).enhance(saturation_factor)
vibrancy = ImageEnhance.Color(saturation).enhance(vibrancy_factor)
warmth = ImageEnhance.Color(vibrancy).enhance(warmth_factor)
tint = ImageEnhance.Color(warmth).enhance(tint_factor)
sharpness = ImageEnhance.Sharpness(tint).enhance(sharpness_factor)
definition = ImageEnhance.Sharpness(sharpness).enhance(definition_factor)

# ruajme foton e modifikuar
definition.save("output_image.jpg")

# ruani imazhin
# file_name = input("Enter file name to save image: ")
# definition.save(file_name)