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
            
    