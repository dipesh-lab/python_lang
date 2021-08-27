elements = ["nasa", "esa", "isro", "jaxa", "boeing"];

print(elements)
print("Collection size", len(elements))
print("First Element", elements[0])


print("Last Element", elements[len(elements) - 1])
print("Last Element", elements[-1])

elements.insert(3, "spacex")

print(elements)


print("Print two lists")

companies = ["lockheed martin", "boeing", "raytheon"]

print(elements + companies)

dataList = elements + companies

print("Print merged list", dataList)
print("Merged list size", len(dataList))


print("Get element frequency", dataList.count("boeing"))

