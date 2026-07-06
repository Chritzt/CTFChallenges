## Paper-Jam

This challenge is a simple application to change the name of a Printer Paper tray, therefore you can enter something on a webpage.

The Application uses Thymeleafe to show the webpage, as I used a old version of Thymeleafe there is a SSTI.

```

    @PostMapping("/updateTray")
    public String updateTray(@RequestParam("trayName") String trayName, Model model) {
        model.addAttribute("userInput", trayName);

        return "preview";
    }
```

This code sends the userinput straight to the template. 

```
    <div style="font-size: 24px; margin: 20px 0;">
        <span th:text="__${userInput}__">User Text</span>
    </div>
```

This code directly puts the user input into the template as a Template Expression (SpEL), which means if you have the right syntax, a command is executed.

The Flag sits in the application.properties `challenge.flag=${CTF_FLAG:FLAG{default_local_fallback_flag}}` and simulates therefore a important software configuration.

The Solution is to use this as a user input `${@environment.getProperty('challenge.flag')}`