package com.example.challenge;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class PrinterController {

    @GetMapping("/")
    public String getIndex(){
        return "index";
    }

    @PostMapping("/updateTray")
    public String updateTray(@RequestParam("trayName") String trayName, Model model) {
        model.addAttribute("userInput", trayName);

        return "preview";
    }
}
