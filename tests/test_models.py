from django.test import TestCase

from tests.models import TestNode, TestEdge


class NodeTestCase(TestCase):
    def test_add_direct_edge(self):
        n1 = TestNode()
        n2 = TestNode()
        n1.save()
        n2.save()
        self.assertNotIn(n1, n2.ancestors.all())
        self.assertNotIn(n2, n1.descendants.all())
        n1.children.add(n2)
        self.assertIn(n2, n1.descendants.all())
        self.assertIn(n2, n1.children.all())
        self.assertIn(n1, n2.ancestors.all())
        self.assertIn(n1, n2.parents.all())

    def test_remove_direct_edge(self):
        n1 = TestNode()
        n2 = TestNode()
        n1.save()
        n2.save()
        n1.children.add(n2)
        n1.children.remove(n2)
        self.assertNotIn(n1, n2.ancestors.all())
        self.assertNotIn(n2, n1.descendants.all())

    def test_remove_nonexisting_edge(self):
        n1 = TestNode()
        n2 = TestNode()
        n1.save()
        n2.save()
        n1.children.remove(n2)
        self.assertNotIn(n1, n2.ancestors.all())
        self.assertNotIn(n2, n1.descendants.all())

    def test_remove_child_node(self):
        n1 = TestNode()
        n2 = TestNode()
        n1.save()
        n2.save()
        n1.descendants.add(n2)
        n2.delete()
        self.assertEqual(n1.descendants.count(), 0)

    def test_remove_parent_node(self):
        n1 = TestNode()
        n2 = TestNode()
        n1.save()
        n2.save()
        n1.descendants.add(n2)
        n1.delete()
        self.assertEqual(n2.ancestors.count(), 0)

    # def test_add_indirect_edge(self):
    #     n1 = TestNode()
    #     n2 = TestNode()
    #     n3 = TestNode()
    #     n1.save()
    #     n2.save()
    #     n3.save()
    #     self.assertNotIn(n1, n2.ancestors.all())
    #     self.assertNotIn(n2, n1.descendants.all())
    #     n1.children.add(n2)
    #     n2.children.add(n3)
    #     self.assertIn(n3, n1.descendants.all())
    #     self.assertIn(n1, n3.ancestors.all())
    #     self.assertNotIn(n3, n1.children.all())
    #     self.assertNotIn(n1, n3.parents.all())


class EdgeTestCase(TestCase):
    def test_update_src_dst_fails(self):
        n1 = TestNode()
        n2 = TestNode()
        n1.save()
        n2.save()
        n1.children.add(n2)
        edge = TestEdge.objects.first()
        self.assertEqual(edge.src, n1)
        self.assertEqual(edge.dst, n2)
        edge.dst = n1
        edge.save()
        # Retrieve again because we're in a bad state
        edge = TestEdge.objects.first()
        self.assertEqual(edge.dst, n2)
