SELECT name
FROM tenants
WHERE tenants.yearOfOccup >= 2001
AND tenants.name LIKE "B%";


SELECT AVG(price)
FROM suites
WHERE suites.type = "bachelor"
AND suites.aID IN 
    (SELECT aID FROM apartments 
    WHERE NOT apartments.address = 'Whyte Ave');


SELECT apartments.address, suites.unitNumber, count(tID) as [number of tenants]
FROM apartments, suites, tenants
WHERE tenants.sID = suites.sID AND suites.aID = apartments.aID
GROUP BY apartments.aID, suites.unitNumber
ORDER BY [number of tenants];