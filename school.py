class School:
    def __init__(self, name):
        self.name = name

    def roster(self, roster = {}):
        self._roster = roster
        return dict(sorted(self._roster.items()))

    def add_student(self,name,roster):
        if roster in self._roster:
            (self._roster[roster]).append(name)
        else:
            self._roster[roster] = []
            self._roster[roster].append(name)
        return dict(sorted(self._roster.items()))

    def grade(self,roster):
        return self._roster[roster]

    def sort_roster(self):
        my_dict = self.roster()
        keys = my_dict.keys()
        new = []
        for roster in keys:
            new_values = sorted(my_dict[roster])
            new.append(new_values)
        return dict(zip(keys,new))
