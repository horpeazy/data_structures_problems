class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    for user_ in group.users:
        if user == user_:
            return True

    for sub_group in group.groups:
        if is_user_in_group(user, sub_group):
            return True
    return False

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child.add_user("Sebastain")
child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("James", parent))
# Output
# False

# Test Case 2
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child.add_user("Sebastain")
child.add_group(sub_child)
parent.add_user("Horpeazy")
print(is_user_in_group("Horpeazy", parent))

# Output
# True

# Test Case 3
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
parent.add_group(child)
child.add_group(sub_child)
sub_sub_child = Group("subchild1")
sub_sub_child.add_user(None)
sub_child.add_group(sub_sub_child)
print(is_user_in_group(None, parent))

# Output
# True