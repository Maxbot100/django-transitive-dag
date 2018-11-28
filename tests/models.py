from django_transitive_dag.models import EdgeModel, NodeModel


class TestEdge(EdgeModel("TestNode")):
    pass


class TestNode(NodeModel("TestEdge")):
    pass
