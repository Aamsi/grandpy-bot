function ConvChat (selector) {
    that = this;
    this.component = $(selector);
    this.msgBlock = "";
    this.msgInput = $(".msg-input");
    this.msgReceived = "";
    this.author = "user";
    this.address = null;
    this.summary = null; 
    this.botMsg = {
        firstMsg: "",
        sndMsg: "",
        errorMsg: ""
    }

    this.getMsg = function () {
        that.msgReceived = that.msgInput.val();
        if (that.msgReceived) {
            that.sendMsg();
            $.post('/process_msg', {
                msg_content: that.msgReceived
            }, function (res) {
                if (res.response == "success") {
                    that.address = res.address;
                    that.summary = res.summary;
                    that.botMsg.firstMsg = `Bien sûr mon poussin ! La voici: ${that.address}.`;
                    that.botMsg.sndMsg = `Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? ${that.summary}`;
                    delete that.botMsg.errorMsg;
                } else {
                    that.botMsg.errorMsg = "Desole, je n'ai pas compris";
                };
                that.msgReceived = "";
            })
            .done(function() {
                that.sendMsg();
            });
        };
    };

    this.sendMsg = function () {
        if (that.msgReceived) {
            that.msgBlock = `<div class='col-md-3 ml-2 mb-3 msg-left'><p>${that.msgReceived}</p></div>`
            that.component.prepend(that.msgBlock);
        } else {
            if (that.botMsg.errorMsg) {
                that.msgBlock = `<div class='col-md-3 ml-2 mb-3 msg-right'><p>${that.botMsg.errorMsg}</p></div>`
                that.component.prepend(that.msgBlock);
                delete that.botMsg.errorMsg;
                return;
            }
            for (const [key, value] of Object.entries(that.botMsg)) {
                that.msgBlock = `<div class='col-md-3 ml-2 mb-3 msg-right'><p>${value}</p></div>`
                that.component.prepend(that.msgBlock);
            };
        };
    };

    this.update = function () {
        that.getMsg();
        that.msgInput.val('');
    };
};


var convChat = new ConvChat(".msg-thread");

$(".btn").click(function(e) {
    e.preventDefault();
    convChat.update();
});
