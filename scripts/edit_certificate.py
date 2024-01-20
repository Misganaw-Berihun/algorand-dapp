import cv2
from datetime import datetime

def load_image(image_path):
    return cv2.imread(image_path)

def resize_logo(logo, target_width):
    _, _, channels = logo.shape
    scale_factor = target_width / logo.shape[1]
    return cv2.resize(logo, (int(target_width), int(logo.shape[0] * scale_factor)))

def add_logo(certificate, logo, position):
    certificate[position[0]:position[0] + logo.shape[0], 
                position[1]:position[1] + logo.shape[1]] = logo

def add_text(certificate, text, position, font_size, font_color, font_thickness, font=cv2.FONT_HERSHEY_SIMPLEX):
    cv2.putText(certificate, text, position, font, font_size, font_color, font_thickness)

def generate_certificate(full_name, date, output_path, certificate_id):
    certificate_bg = load_image("../images/certificate.png")
    logo = load_image("../images/logo.png")
    logo = resize_logo(logo, target_width=100)
    
    add_logo(certificate_bg, logo, position=(20, 20))

    add_text(certificate_bg, "ISSUE DATE", position=(130, 485), font_size=1, font_color=(0, 0, 0), font_thickness=2)
    add_text(certificate_bg, "Certificate ID", position=(690, 485), font_size=1, font_color=(0, 0, 0), font_thickness=2)

    add_text(certificate_bg, full_name, position=(200, 635), font_size=2, font_color=(255, 0, 0), font_thickness=4)

    date_str = date.strftime("%B %d, %Y") 
    add_text(certificate_bg, date_str, position=(200, 520), font_size=0.5, font_color=(255, 0, 0), font_thickness=2)

    add_text(certificate_bg, certificate_id, position=(700, 520), font_size=0.5, font_color=(255, 0, 0), font_thickness=2)

    cv2.imwrite(output_path, certificate_bg)

if __name__ == "__main__":
    full_name = "Misganaw Berihun"
    date = datetime.now()
    output_path = "output_certificate.jpg"
    generate_certificate(full_name, date, output_path, "CTF123494u5664098")
