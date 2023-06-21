class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))

super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))
print(issubclass(list, object))
print(isinstance(super_list1, list))
print(isinstance(super_list1, object))
print(super_list1.__len__())
print(super_list1.__repr__())
print(super_list1.__str__())
print(super_list1.__getitem__(0))
print(super_list1.__add__([1, 2, 3]))
print(super_list1.__mul__(2))
print(super_list1.__len__())
print(super_list1.__delitem__(0))
