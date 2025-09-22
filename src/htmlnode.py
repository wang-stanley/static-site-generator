class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        html_attributes = ""
        
        if not self.props:
            return html_attributes
        
        for prop in self.props:
            html_attributes += (f' {prop}="{self.props[prop]}"')
        return html_attributes
            
    def __repr__(self):
        print(f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")
    
    
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError("LeafNode value is empty")
        
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag or self.tag == "":
            raise ValueError("ParentNode tag is empty")

        if not self.children or len(self.children) == 0:
            raise ValueError("Children's list is empty")
        
        children_concat = ""
        for child in self.children:
            child_text = child.to_html()
            children_concat += child_text
            
        return f"<{self.tag}{self.props_to_html()}>{children_concat}</{self.tag}>"
    