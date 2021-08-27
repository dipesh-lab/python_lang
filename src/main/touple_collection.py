elements = ("nasa", "esa", "isro", "jaxa", "boeing");

print(elements)
print("Collection size", elements.__len__())
print("First Element", elements[0])


print("Last Element", elements[elements.__len__() - 1])
print("Last Element", elements[-1])

elements.insert(3, "spacex")

print(elements)


print("Print two lists")

companies = ["lockheed martin", "boeing", "raytheon"]

print(elements + companies)

dataList = elements + companies

print("Print merged list", dataList)
print("Merged list size", dataList.__len__())


print("Get element frequency", dataList.count("boeing"))