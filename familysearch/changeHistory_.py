"""FamilySearch Change History submodule"""
# Python imports

# Magic

class ChangeHistory:
    """https://familysearch.org/developers/docs/api/resources#authorities"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#change-history"""
        pass

    def person_change_history(self, pid):
        """https://familysearch.org/developers/docs/api/tree/Person_Change_History_resource"""
        return self.base + "/platform/tree/persons/{pid}/changes".format(pid)

    def child_change_history(self, caprid):
        """https://familysearch.org/developers/docs/api/tree/Child-and-Parents_Relationship_Change_History_resource."""
        return self.tree_base + "child-and-parents-relationships/"\
              + caprid + "/changes"

    def couple_change_history(self, crid):
        """https://familysearch.org/developers/docs/api/tree/Couple_Relationship_Change_History_resource"""
        return self.tree_base + "couple-relationships/" + crid + "/changes"

    def restore_change(self, chid):
        """Obsolete."""
        return self.tree_base + "changes/" + chid + "/restore"

# FamilySearch imports

from familysearch import FamilySearch
FamilySearch.__bases__ += (ChangeHistory,)