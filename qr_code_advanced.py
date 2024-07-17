import segno

# Define the URL to encode
url = "https://www.youtube.com/watch?v=tcxDCRSm-0A"

# Create the QR code object
dengos_qrcode = segno.make_qr(url)

# Download Elias Dengo's website content (optional)
# This might not be necessary depending on your artistic goal

# elias_dengo_url = urlopen("http://eliasdengo.github.io/")  # Commented out

# Create artistic QR code with a white background (optional)
# This avoids downloading external content, which can be unreliable
white_background = (255, 255, 255)  # RGB values for white
dengos_qrcode.artistic(background_color=white_background)

# Save the QR code as a GIF image
dengos_qrcode.save("elias_dengo.gif", scale=5)

