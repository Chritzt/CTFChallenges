package main

import (
	"database/sql"
	"fmt"
	"html/template"
	"log"
	"net/http"
	"os"
	"strings"

	_ "github.com/mattn/go-sqlite3"
)

type Drink struct {
	Name        string
	Description string
}

var db *sql.DB

func main() {
	var err error
	db, err = sql.Open("sqlite3", "/app/coffee.db")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	envFlag := os.Getenv("FLAG")
	if envFlag != "" {
		newDesc := fmt.Sprintf("NOT AGAIN %s", envFlag)

		_, err := db.Exec("UPDATE Secret SET description = ? WHERE name = 'Boss-Coffee';", newDesc)
		if err != nil {
			fmt.Printf("[-] Error Updating Flag %v\n", err)
		} else {
			fmt.Println("[+] All Good")
		}
	}

	http.HandleFunc("/", handleIndex)

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	fmt.Printf("All Running %s\n", port)
	log.Fatal(http.ListenAndServe(":"+port, nil))
}

func handleIndex(w http.ResponseWriter, r *http.Request) {
	var result []Drink
	search := r.URL.Query().Get("search")
	wafTriggered := false

	if search != "" {
		searchLower := strings.ToLower(search)

		if strings.Contains(searchLower, " or ") ||
			strings.Contains(searchLower, "oR ") ||
			strings.Contains(searchLower, " Or ") ||
			strings.Contains(search, "--") {

			wafTriggered = true
		} else {
			rows, err := db.Query(fmt.Sprintf("SELECT name, description FROM CoffeeBot WHERE name = '%s';", search))
			if err == nil {
				defer rows.Close()
				for rows.Next() {
					var g Drink
					rows.Scan(&g.Name, &g.Description)
					result = append(result, g)
				}
			}
		}
	}

	tmpl := `
    <!DOCTYPE html>
    <html>
    <head>
       <title>CoffeeBot v2.0</title>
       <style>
          body { font-family: 'Segoe UI', sans-serif; background-color: #f4f7f6; color: #333; padding: 40px; }
          .container { max-width: 600px; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin: 0 auto; }
          h2 { color: #6f4e37; margin-top: 0; }
          .waf-alert { background-color: #f8d7da; color: #721c24; padding: 12px; border-radius: 4px; margin-bottom: 20px; border-left: 4px solid #f5c6cb; }
          input[type=text] { width: 70%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; }
          button { padding: 10px 20px; background-color: #6f4e37; color: white; border: none; border-radius: 4px; cursor: pointer; }
          button:hover { background-color: #553c29; }
          ul { list-style-type: none; padding: 0; }
          li { background: #fafafa; padding: 12px; margin-bottom: 8px; border-left: 4px solid #6f4e37; border-radius: 4px; }
          hr { border: 0; height: 1px; background: #eee; margin: 25px 0; }
       </style>
    </head>
    <body>
       <div class="container">
          <h2> CoffeeBot v2.0 (Advanced)</h2>
          <p>Welcome to our internal coffee system. Please search for a Drink:</p>
          
          {{if .Waf}}
             <div class="waf-alert">⚡ <strong>WAF Blocked:</strong> Malicious activity detected!</div>
          {{end}}

          <form method="GET" action="/">
             <input type="text" name="search" placeholder="Coffee, Tee..." autocomplete="off">
             <button type="submit">Search</button>
          </form>
          <hr>
          <h3>Searching Result:</h3>
          <ul>
          {{range .Drinks}}
             <li><strong>{{.Name}}</strong><br><span style="color:#666; font-size:13px;">{{.Description}}</span></li>
          {{else}}
             <li style="border-left-color: #ccc; color: #777;">No Drinks found</li>
          {{end}}
          </ul>
       </div>
    </body>
    </html>`

	// Wir übergeben eine anonyme Struct an das Template, um sowohl die Drinks als auch den WAF-Status zu rendern
	t, _ := template.New("webpage").Parse(tmpl)
	t.Execute(w, struct {
		Drinks []Drink
		Waf    bool
	}{result, wafTriggered})
}
