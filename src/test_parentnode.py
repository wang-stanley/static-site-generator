import unittest

from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_single_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("span", "child1")
        child2 = LeafNode("b", "child2")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child1</span><b>child2</b></div>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_deep_nesting(self):
        deep = LeafNode("i", "innermost")
        for _ in range(5):
            deep = ParentNode("div", [deep])
        self.assertEqual(
            deep.to_html(),
            "<div><div><div><div><div><i>innermost</i></div></div></div></div></div>",
        )

    def test_to_html_with_props(self):
        child = LeafNode("span", "hello")
        parent = ParentNode("div", [child], props={"class": "container", "id": "main"})
        self.assertEqual(
            parent.to_html(),
            '<div class="container" id="main"><span>hello</span></div>',
        )

    def test_to_html_raises_if_no_tag(self):
        child = LeafNode("span", "child")
        with self.assertRaises(ValueError):
            ParentNode("", [child]).to_html()

    def test_to_html_raises_if_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()

    def test_to_html_raises_if_children_none(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()
            
    def test_child_raises_error_bubbles_up(self):
        bad_child = LeafNode("span", None)  # this will raise in LeafNode.to_html
        parent = ParentNode("div", [bad_child])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_empty_string_tag(self):
        child = LeafNode("span", "ok")
        with self.assertRaises(ValueError):
            ParentNode("", [child]).to_html()

    def test_none_tag(self):
        child = LeafNode("span", "ok")
        with self.assertRaises(ValueError):
            ParentNode(None, [child]).to_html()

    def test_none_children_list(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_empty_children_list(self):
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()

    def test_props_with_special_characters(self):
        child = LeafNode("span", "hello")
        parent = ParentNode("div", [child], props={"data-info": "5>3 & 2<4"})
        self.assertEqual(
            parent.to_html(),
            '<div data-info="5>3 & 2<4"><span>hello</span></div>',
        )


if __name__ == "__main__":
    unittest.main()
