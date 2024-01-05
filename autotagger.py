import piexif
import piexif.helper

def add_comment(image_path, comment):
  # Load the Exif data from the image
  exif_dict = piexif.load(image_path)

  # Convert the comment to the correct format
  user_comment = piexif.helper.UserComment.dump(comment)

  # Add the comment to the UserComment field in the Exif data
  exif_dict['Exif'][piexif.ExifIFD.UserComment] = user_comment

  # Write the modified Exif data back to the image
  piexif.insert(piexif.dump(exif_dict), image_path)

if __name__ == "__main__":
  image_path = r"image.jpg"
  comment = "My comment"

  add_comment(image_path, comment)
