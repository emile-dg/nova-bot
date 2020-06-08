(function(){
    // app class
    class NovaClient {
        // configurations
        name = "BECCA"
        version = "1.0.0"
        base_host = "http://127.0.0.1:5000/"

        // the dom elements
        wrapper = null
        header = null
        content = null
        footer = null
        close_button = null
        open_button = null
        send_btn = null
        input = null


        toggle_wrapper() {
            bot.wrapper.classList.toggle("closed")
        }

        init_dom() {
            // create and add appropriate classNames to the elements
            // the parent wrapper
            this.wrapper = document.createElement("div")
            this.wrapper.classList.add("nova-chat-wrapper")
            this.wrapper.classList.add("closed")

            // the close button
            this.open_button = document.createElement("div")
            this.open_button.classList.add("closed-icon")
            this.open_button.setAttribute("id", "openNova")
            let icon = document.createElement("i")
            icon.classList.add("fa")
            icon.classList.add("fa-comments")
            this.open_button.appendChild(icon)
            this.open_button.onclick = this.toggle_wrapper

            // the header
            this.header = document.createElement("div")
            this.header.classList.add("header")

            this.close_button = document.createElement("button")
            this.close_button.classList.add("close")
            let icon_2 = document.createElement("i")
            icon_2.classList.add("fa")
            icon_2.classList.add("fa-times")

            this.close_button.appendChild(icon_2)
            this.close_button.onclick = this.toggle_wrapper
            this.header.appendChild(this.close_button)
            
            // the body
            this.content = document.createElement("div")
            this.content.classList.add("body-content")

            // the footer
            this.footer = document.createElement("div")
            this.footer.classList.add("foot")

            let input_wrapper = document.createElement("div")
            input_wrapper.classList.add("input-control-wrapper")
            this.input = document.createElement("input")
            this.input.setAttribute("type", "text")

            this.send_btn = document.createElement("button")
            let icon_3 = document.createElement("i")
            icon_3.classList.add("fa")
            icon_3.classList.add("fa-paper-plane")
            this.send_btn.appendChild(icon_3)
            this.send_btn.onclick = () => { this.send_message() }

            input_wrapper.appendChild(this.input)
            input_wrapper.appendChild(this.send_btn)
            this.footer.appendChild(input_wrapper)

        }

        appendDom() {
            this.wrapper.appendChild(this.open_button)
            this.wrapper.appendChild(this.header)
            this.wrapper.appendChild(this.content)
            this.wrapper.appendChild(this.footer)
            document.body.appendChild(this.wrapper)
        }

        create_ui() {
            this.init_dom()
            this.appendDom()
        }

        init_app() {
            console.log(this.name+" is initializing")
            this.create_ui()
        }

        start() {
            console.log(this.name+" is starting")
            this.init_app()
        }

        add_msg_bubble(text, person) {
            let bubble, p
            bubble = document.createElement("div")
            p = document.createElement("p")
            p.innerText = text
            bubble.appendChild(p)
            bubble.classList.add("message-box")
            bubble.classList.add(person)
            this.content.appendChild(bubble)
            this.input.value = ""
            this.content.scrolllTop = this.content.scrolllHeight
        }

        send_message() {
            let msg = this.input.value
            if (msg != "") {
                this.ajax_call(msg)
                this.add_msg_bubble(msg ,"user")
            }
        }

        ajax_call(text) {
            let xhttp = new XMLHttpRequest ();
            bot = this
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    let result = JSON.parse(xhttp.responseText)
                    bot.add_msg_bubble(result.message, "bot")
                }
            }
            xhttp.open ("GET", this.base_host+"reply?m="+text);
            xhttp.setRequestHeader ("Content-type", "application/json");
            xhttp.send();
        }
    }

    bot = new NovaClient();
    bot.start()

})();