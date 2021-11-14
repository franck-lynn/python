import numbers


class Group:
    # 支持切片操作
    def __init__(self, name, company_name, staffs):
        self.name = name
        self.company_name = company_name
        self.staffs = staffs
    # 实现一个不可变的 sequence, 要实现这些魔法函数

    def __reversed__(self):
        self.staffs.reverse()

    #! 实现切片的关键, 要实现

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(name=self.name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(name=self.name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

    def __str__(self) -> str:
        return str(self.staffs)


staffs = ['bobby1', 'imooc', 'bobby3', 'bobby4']
group = Group(name="imooc", company_name="imooc",  staffs=staffs)

sub_group = group[:2]
print(sub_group)
sub_group = group[0]
print(sub_group)
print(len(group))

reversed(group)
print(group)