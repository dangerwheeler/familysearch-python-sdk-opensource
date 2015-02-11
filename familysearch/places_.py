"""FamilySearch Places submodule"""
# Python imports

# Magic

class Places:
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#places"""
        self.places_base = self.base + "/platform/places/"
        from familysearch import FamilySearch
        FamilySearch.__bases__ += (Places,)

    def get_places_search(self, q):
        """Obsolete."""
        return self.get(self.places_base + "search?q=name:" + q)

    def get_place_description(self, pdid, children=None):
        """Obsolete."""
        url = self.places_base + "description/" + pdid
        if children:
            url = url + "/children"
        return self.get(url)

    def get_place_group(self, pgid):
        """Obsolete."""
        return self.get(self.places_base + "gropus/" + pgid)

    def get_place(self, pid):
        """Obsolete."""
        return self.get(self.places_base + str(pid))

    def get_place_type(self, ptid):
        """Obsolete."""
        return self.get(self.places_base + "types/" + ptid)

    def get_place_type_group(self, ptgid):
        """Obsolete."""
        return self.get(self.places_base + "type-gropus/" + ptgid)

    def get_place_types(self):
        """Obsolete."""
        return self.get(self.places_base + "types")

    def get_place_type_groups(self):
        """Obsolete."""
        return self.get(self.places_base + "type-groups")