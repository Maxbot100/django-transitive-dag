from django_transitive_dag.models import EdgeModel, NodeModel


class TestEdge(EdgeModel("TestNode")):
    def __str__(self):
        return "TestEdge[{0.id}, {0.src.id}-{0.hops}->{0.dst.id}]".format(self)


class TestNode(NodeModel("TestEdge")):
    def __str__(self):
        return "TestNode[{0.id}]".format(self)
