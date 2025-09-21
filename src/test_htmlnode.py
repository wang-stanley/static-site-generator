import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode()
        node.to_html
        self.assertRaises(NotImplementedError)
        
    def test_props_to_html1(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        
        node = HTMLNode(self, "p", "blah", props=props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        
    def test_props_to_html2(self):
        props = {
            "href": "https://www.google.com",
        }
        
        node = HTMLNode(self, "p", "blah", props=props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
        
    def test_props_to_html3(self):
        node = HTMLNode(self, "p", "blah")
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()