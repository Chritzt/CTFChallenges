## The Unsafe Weddingbook

This challenge has a Simple web interface with just one inputfield and this one is vulnerable to xss.

The intended solution is to get the flag with this payload: 
```
<img src=x onerror=alert(document.cookie)>
```

Honestly the flag is found in the coockies of you browser so you can also solve the challenge in this way, however I wanted to do a very easy beginner challenge and then go further to reflected XSS and blind XSS.


