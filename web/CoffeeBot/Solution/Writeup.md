## CoffeeBot

A rather simple Challenge. It is just a Basic SQLi

There is one search field where you can search for different drinks a cooperation provides for employees.

However the Boss has one secret entry called Boss-Coffee (its actually Beer).


This part is the vulnerability: 
```
rows, err := db.Query(fmt.Sprintf("SELECT name, description FROM CoffeeBot WHERE name = '%s' AND status = 'public';", search))
```

The Solution is to search for `' OR 1=1 --` and then you bypass the public where clause to also find hidden Drinks.
