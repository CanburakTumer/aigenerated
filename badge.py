from PIL import Image, ImageDraw, ImageFont
import os

# Badge specifications
width = 400
height = 40
background_color = (90, 90, 90)  # Gray background similar to the style provided
left_color = (60, 60, 60)  # Darker gray for the left section
text_color = (255, 255, 255)  # White text

# Create the badge
badge = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(badge)

# Define font (using default system font)
try:
    # Try to use Arial font
    font = ImageFont.truetype("arial.ttf", 32)  # Increased from 20 to 24
except:
    # Fallback to default font
    font = ImageFont.load_default(size=24)

# Left section (AI Icon background)
icon_section_width = 50
draw.rectangle([(0, 0), (icon_section_width, height)], fill=left_color)

# Add AI text/icon
ai_text = "AI"
text_bbox = draw.textbbox((0, 0), ai_text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
text_x = (icon_section_width - text_width) // 2
text_y = (height - text_height) // 2
draw.text((text_x, text_y), ai_text, fill=text_color, font=font)

# Center section (Message: "AI Assisted content")
message = "AI Assisted Content"
message_x = icon_section_width + 30
message_bbox = draw.textbbox((0, 0), message, font=font)
message_height = message_bbox[3] - message_bbox[1]
message_y = (height - message_height) // 2
draw.text((message_x, message_y), message, fill=text_color, font=font)

# Right section (Percentage: "100%")
percentage = "100%"
percentage_bbox = draw.textbbox((0, 0), percentage, font=font)
percentage_width = percentage_bbox[2] - percentage_bbox[0]
percentage_x = width - percentage_width - 10
draw.text((percentage_x, message_y), percentage, fill=text_color, font=font)

# Save the badge as PNG
output_path = "ai_assisted_badge.png"
badge.save(output_path)
output_path
