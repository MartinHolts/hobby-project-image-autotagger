import piexif

def add_title(image_path, title):
 # Load the Exif data from the image
 exif_dict = piexif.load(image_path)

 # Add the title to the ImageDescription field in the ImageIFD data
 exif_dict['0th'][piexif.ImageIFD.ImageDescription] = title.encode('utf-8')

 # Write the modified Exif data back to the image
 piexif.insert(piexif.dump(exif_dict), image_path)

if __name__ == "__main__":
 image_path = r"image.jpg"
 title = "My Image Title"

 add_title(image_path, title)
