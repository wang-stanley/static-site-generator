import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
        
    def test_leaf_node_error(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_raw(self):
        node = LeafNode(None, "raw text", None)
        self.assertEqual(node.to_html(), "raw text")
    
    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
        
    def test_leaf_to_html_empty(self):
        node = LeafNode("p", "", None)
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_leaf_to_html_anchor_multi_props(self):
        node = LeafNode("a", "Click", {"href": "https://x.com", "target": "_blank"})
        html = node.to_html()
        self.assertTrue(html.startswith("<a "))
        self.assertIn('href="https://x.com"', html)
        self.assertIn('target="_blank"', html)
        self.assertTrue(html.endswith('>Click</a>'))
        
    def test_leaf_to_html_span_with_class(self):
        node = LeafNode("span", "hi", {"class": "badge badge-info"})
        html = node.to_html()
        self.assertTrue(html.startswith("<span "))
        self.assertIn('class="badge badge-info"', html)
        self.assertTrue(html.endswith('>hi</span>'))
        
    def test_leaf_to_html_raw_preserves_whitespace(self):
        text = "  padded text  "
        node = LeafNode(None, text)
        self.assertEqual(node.to_html(), text)        
        
if __name__ == "__main__":
    unittest.main()