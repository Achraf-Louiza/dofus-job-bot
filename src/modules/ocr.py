from PIL import Image
import pytesseract

PYTESSERACT_CONFIG_FUNC = lambda chars: f'--psm 6 -c tessedit_char_whitelist={chars}'

class OCR:
    """
    A class that applies character recognition on an image 
    
    """
    def __init__(self):
        pass       
        
    def recognize_text(self, image: Image, recognizable_chars: str) -> str:
        """
        Recognize the characters in the image following the config input (indicates characters to acknowledge)

        Parameters
        ----------
        image : Image
            Image where text need to be extracted
        recognizable_chars : str
            string of characters to recognize in image ocr

        Returns
        -------
        str
            Text included in the image restricted to config

        """
        config = PYTESSERACT_CONFIG_FUNC(recognizable_chars)
        text = pytesseract.image_to_string(image, config=config)
        return text
    