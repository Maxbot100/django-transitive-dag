from django.db import models


def EdgeModel(node_model):
    class AbstractEdgeModel(models.Model):
        src = models.ForeignKey(node_model, on_delete=models.CASCADE, related_name="dsc_edges", editable=False)
        dst = models.ForeignKey(node_model, on_delete=models.CASCADE, related_name="asc_edges", editable=False)
        hops = models.PositiveIntegerField(default=0)

        def save(self, *args, **kwargs):
            # Prevent updating src & dst fields
            update_fields = kwargs.get('update_fields', None)
            if update_fields is None:
                update_fields = self._meta.get_fields()
            kwargs['update_fields'] = [f.name for f in update_fields if f.name not in ("id", "src", "dst")]
            return super().save(*args, **kwargs)

        class Meta:
            abstract = True
            auto_created = True
            unique_together = (('src', 'dst'),)

    return AbstractEdgeModel


def NodeModel(edge_model):
    class AbstractNodeModel(models.Model):
        descendants = models.ManyToManyField(
            "self",
            through=edge_model,
            through_fields=("src", "dst"),
            related_name="ancestors",
            symmetrical=False
        )

        class Meta:
            abstract = True

        _children = None
        _parents = None

        @property
        def children(self):
            if self._children is None:
                # Maybe hacky? But we get add, remove, etc. niceties from ManyRelatedManager
                class Children(self.descendants.__class__):
                    def get_queryset(self):
                        return super().get_queryset().filter(asc_edges__hops=0)
                self._children = Children(self)
            return self._children

        @property
        def parents(self):
            if self._parents is None:
                class Parents(self.ancestors.__class__):
                    def get_queryset(self):
                        return super().get_queryset().filter(dsc_edges__hops=0)
                self._parents = Parents(self)
            return self._parents

    return AbstractNodeModel
