from enum import Enum

class TextType(Enum):
    TEXT = "text"
    ITALIC = "italic"
    BOLD = "bold"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
class TextNode():
    def __init__(self, text, type, url=None):
        self.text = text
        self.type = type
        self.url = url
        
    def __eq__(self, node):
        return(self.text == node.text and self.type == node.type and self.url == node.url)
    
    def __repr__(self):
        return (f"TextNode({self.text}, {self.type}, {self.url})")
