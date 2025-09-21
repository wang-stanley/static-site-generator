import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_neq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        
    def test_neq_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node DIFF", TextType.TEXT)
        self.assertNotEqual(node, node2)
        
    def test_neq_url(self):
        node = TextNode("This is a text node", TextType.TEXT, url="https://test.com")
        node2 = TextNode("This is a text node", TextType.TEXT, url="https://testDIFF.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()