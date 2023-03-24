class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        return

    def __str__(self):  # 用于人性化显示，面向用户，print(object)
        return self.name + ":" + str(self.age)

    def __lt__(self, other):
        return self.name < other.name if self.name != other.name else self.age < other.age


if __name__ == "__main__":
    print("\t".join([str(item) for item in sorted([People("abc", 18),
                                                   People("abe", 19), People("abe", 12), People("abc", 17)])]))
