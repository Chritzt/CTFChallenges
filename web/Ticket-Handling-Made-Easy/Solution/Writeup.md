## Ticket-Handling-Made-Easy

This is a simple web challenge. It runs on python/flask and provides a simple web page with one input field. This input field has a SSTI attack.

`app.config['FLAG'] = os.getenv("FLAG")`

The Flag is loaded into the application config.

Later the application writes the user_input directly into the template, therefore the template engine executes commands put in the user_input.

```
    template = f'''
    <html>
        <head>
            <title>IT Support Ticket Status</title>
        </head>
        <body style="background-color: #f0f0f0; font-family: monospace; padding: 50px;">
            <h2>Automated Response System</h2>
            <hr>
            <p><strong>Status of your request: {user_input} </strong></p>
            <div style="background: white; padding: 20px; border: 1px solid #ccc;">
                {selected_response}
            </div>
            <br>
            <a href="/">Back to submission</a>
        </body>
    </html>
    '''

    return render_template_string(template)
```


The solution is to look in the application.config : 
`{{config}}`