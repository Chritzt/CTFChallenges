package main

import (
	"html/template"
	"log"
	"net/http"
	"os"
)

type PageData struct {
	SearchTerm string
	Search template.HTML
	Flag         string
}

var flag string

func main() {
	flag = os.Getenv("FLAG")
	if flag == "" {
		flag = "FLAG{test_reflected_xss_worked_1337}"
	}

	http.HandleFunc("/", handleIndex)

	log.Println("Server lrunning http://localhost:8080 ...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handleIndex(w http.ResponseWriter, r *http.Request) {
	searchTerm := r.URL.Query().Get("search")

    http.SetCookie(w, &http.Cookie{
        Name:     "flag",
        Value:    flag,
        HttpOnly: false, 
        Path:     "/",
    })

    data := PageData{
        SearchTerm:   searchTerm,
        Search: template.HTML(searchTerm),
    }

	tmplSource := `
	<!DOCTYPE html>
	<html lang="de">
	<head>
		<meta charset="UTF-8">
		<title>Susi & Max | Wedding Guestbook</title>
		<style>
			:root {
				--bg-color: #f4f7f5;
				--card-bg: #ffffff;
				--text-main: #2c3e35;
				--text-muted: #607266;
				--accent: #8a9a86; /* Salbeigrün */
				--accent-hover: #6b7a68;
				--border: #e2e8f0;
				--highlight-bg: #f0f4f1;
			}

			body { 
				font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
				background-color: var(--bg-color); 
				color: var(--text-main); 
				margin: 0;
				padding: 0;
				display: flex;
				justify-content: center;
				align-items: center;
				min-height: 100vh;
			}

			.container { 
				background: var(--card-bg); 
				padding: 40px; 
				border-radius: 20px; 
				box-shadow: 0 10px 30px rgba(44, 62, 53, 0.05); 
				max-width: 450px; 
				width: 100%;
				box-sizing: border-box;
				border: 1px solid rgba(138, 154, 134, 0.15);
			}

			h1 { 
				font-size: 1.8rem;
				font-weight: 600;
				color: var(--text-main);
				margin-top: 0;
				margin-bottom: 10px;
				letter-spacing: -0.5px;
			}

			p {
				color: var(--text-muted);
				font-size: 0.95rem;
				margin-bottom: 30px;
			}
			
			.form-group {
				display: flex;
				gap: 10px;
				margin-bottom: 20px;
			}

			input[type="text"] { 
				flex: 1;
				padding: 12px 16px; 
				border: 1px solid var(--border); 
				border-radius: 10px; 
				font-size: 0.95rem;
				background-color: #fafafa;
				transition: all 0.2s ease;
				outline: none;
			}

			input[type="text"]:focus {
				border-color: var(--accent);
				background-color: #fff;
				box-shadow: 0 0 0 3px rgba(138, 154, 134, 0.2);
			}

			input[type="submit"] { 
				background-color: var(--accent); 
				color: white; 
				border: none; 
				padding: 12px 24px; 
				border-radius: 10px; 
				cursor: pointer; 
				font-weight: 600; 
				font-size: 0.95rem;
				transition: background-color 0.2s ease, transform 0.1s ease;
			}

			input[type="submit"]:hover { 
				background-color: var(--accent-hover); 
			}

			input[type="submit"]:active { 
				transform: scale(0.98); 
			}

			.result { 
				margin-top: 25px; 
				padding: 20px; 
				background-color: var(--highlight-bg); 
				border-radius: 12px; 
				border-left: 4px solid var(--accent);
				text-align: left;
			}

			.result strong {
				color: var(--text-main);
				word-break: break-all;
			}

			.no-entries {
				margin: 8px 0 0 0;
				font-size: 0.85rem;
				color: var(--text-muted);
			}
		</style>
	</head>
	<body>
		<div class="container">
			<h1>Susi & Max</h1>
			<p>Digital Guestbook</p>
			
			<form method="GET" action="/">
				<div class="form-group">
					<input type="text" name="search" placeholder="Search for guests..." value="{{.SearchTerm}}">
					<input type="submit" value="Suchen">
				</div>
			</form>

			{{if .SearchTerm}}
				<div class="result">
					Status for: <strong>{{.Search}}</strong>
					<p class="no-entries">No entries by now.</p>
				</div>
			{{end}}
		</div>
	</body>
	</html>
	`

	tmpl, err := template.New("webpage").Parse(tmplSource)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	tmpl.Execute(w, data)
}
