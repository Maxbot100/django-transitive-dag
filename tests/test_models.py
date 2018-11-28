from django.test import TestCase

from tests.models import TestNode


class NodeTestCase(TestCase):
    def test_add_direct(self):
        n1 = TestNode()
        n2 = TestNode()
        n1.save()
        n2.save()
        self.assertNotIn(n1, n2.parents.all())
        self.assertNotIn(n2, n1.children.all())
        n1.children.add(n2)
        self.assertIn(n1, n2.parents.all())
        self.assertIn(n2, n1.children.all())
