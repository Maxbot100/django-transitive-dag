from django.db import models


def EdgeModel(node_model):
    class AbstractEdgeModel(models.Model):
        src = models.ForeignKey(node_model, on_delete=models.CASCADE, related_name="child_edges")
        dst = models.ForeignKey(node_model, on_delete=models.CASCADE, related_name="parent_edges")

        class Meta:
            abstract = True
            auto_created = True
    return AbstractEdgeModel


def NodeModel(edge_model):
    class AbstractNodeModel(models.Model):
        children = models.ManyToManyField(
            "self",
            through=edge_model,
            through_fields=("src", "dst"),
            related_name="parents",
            symmetrical=False
        )

        class Meta:
            abstract = True
    return AbstractNodeModel
