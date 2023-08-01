from PIL import Image
import qrcode

# Open the image file
img = Image.open('./oldGoogle.png')
width, height = img.size

# Get the URL to generate a QR code for
new_link = "https://facebook.com"

# Generate the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(new_link)
qr.make(fit=True)
img_new = qr.make_image(fill_color="black", back_color="white")

# Create a new blank image with the same dimensions as the original image
img_qr = Image.new('RGB', (width, height), color='white')

# Calculate the position to paste the QR code onto the blank image
x = (width - img_new.width) // 2
y = (height - img_new.height) // 2

# Paste the QR code onto the blank image
img_qr.paste(img_new, (x, y))

# Paste the blank image with the QR code onto the original image
img.paste(img_qr, (0, 0))

# Save the new image
img.save('./new.png')

# Close the original image
img.close()
