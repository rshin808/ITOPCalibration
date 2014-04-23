class Peter:
    def __init__(self, name, job):
        self._name = str(name)
        self.name = str(name)
        self._job = str(job)

    def __str__(self):
        return self._name

    def __len__(self):
        return len(self._name)
P = Peter("Peter Orel", "GOD of hardware")

print P.name
print len(P)


def test1(complex):
    return complex


print test1(2)
print test1(P)

a = True

if a == True:
    print "ok"

a = "hello"

if a == True:
    print "ok"
else:
    print type(a)
