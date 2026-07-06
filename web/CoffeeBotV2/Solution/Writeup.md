## CoffeeBotv2

Again a rather simple challenge, this time a bit more advanced, with a union select.

There is one search field where you can search for different drinks a cooperation provides for employees.

However this time the boss has his secret entry in a Secret table.

There is also a small WAF like feature preventing a few attacks.
```
		if strings.Contains(searchLower, " or ") ||
			strings.Contains(searchLower, "oR ") ||
			strings.Contains(searchLower, " Or ") ||
			strings.Contains(search, "--") {

			wafTriggered = true
		}
```

This part is the vulnerability: 
```
rows, err := db.Query(fmt.Sprintf("SELECT name, description FROM CoffeeBot WHERE name = '%s';", search))
```

The Solution is to search for `' UNION SELECT name, description FROM Secret WHERE '1'='1` and therefore you can see the content of the secret table.



