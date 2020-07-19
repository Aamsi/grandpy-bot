function ConvChat (selector) {
    that = this;
    this.component = $(selector);
    this.msgBlock = "";
    this.msgInput = $(".msg-input");
    this.msgReceived = "";
    this.author = "user";
    this.address = null;
    this.summary = null;
    this.lat = null;
    this.long = null;
    this.mapToken = null;
    this.map = null;
    this.botMsg = {
        firstMsg: "",
        map: "",
        sndMsg: "",
        errorMsg: "",
        smallTalkMsg: ""
    }

    this.getMsg = function () {
        that.msgReceived = that.msgInput.val();
        that.botMsg.smallTalkMsg = that.checkSmallTalk(that.msgReceived);
        if (that.msgReceived) {
            that.sendMsg();
            if (that.botMsg.smallTalkMsg) {
                $(".btn-send").hide();
                $(".btn-load").show();
                that.msgReceived = "";
                that.sendMsg();
                return;
            }
            $.post('/process_msg', {
                msg_content: that.msgReceived
            }, function (res) {
                if (res.response == "success") {
                    that.address = res.address;
                    that.summary = res.summary;
                    that.lat = res.lat;
                    that.long = res.long;
                    that.token = res.token;
                    that.botMsg.firstMsg = `Bien sûr mon poussin ! La voici: ${that.address}.`;
                    that.botMsg.sndMsg = `Tu veux des infos sur ce lieu? ${that.summary}`;
                    delete that.botMsg.errorMsg;
                    delete that.botMsg.smallTalkMsg;
                } else {
                    that.botMsg.errorMsg = "Desole, je n'ai pas compris";
                };
                that.msgReceived = "";
            })
            .done(function() {
                $(".btn-load").hide();
                $(".btn-send").show();
                that.sendMsg();
            });
        };
    };

    this.sendMsg = function () {
        if (that.msgReceived) {
            that.msgBlock = `<div class="msg-left row">
                                <div class="col-md-12">
                                    <div class="float-left"><p>${that.msgReceived}&nbsp;&nbsp;</p></div>
                                </div>
                            </div>`
            that.component.prepend(that.msgBlock);
            $(".btn-load").show();
            $(".btn-send").hide();
        } else {
            if (that.botMsg.errorMsg) {
                that.msgBlock = `<div class="msg-right row">
                                    <div class="col-md-12">
                                        <div class="float-right"><p>${that.botMsg.errorMsg}</p></div>
                                    </div>
                                </div>`;
                that.component.prepend(that.msgBlock);
                delete that.botMsg.errorMsg;
                return;
            } else if (that.botMsg.smallTalkMsg) {
                that.msgBlock = `<div class="msg-right row">
                                    <div class="col-md-12">
                                        <div class="float-right"><p>${that.botMsg.smallTalkMsg}</p></div>
                                    </div>
                                </div>`
                that.component.prepend(that.msgBlock);
                $(".btn-load").hide();
                $(".btn-send").show();
                delete that.botMsg.smallTalkMsg;
                return;
            }
            for (const [key, value] of Object.entries(that.botMsg)) {
                if (key == 'map') {
                    that.msgBlock = `<div class="msg-right row">
                                        <div class="col-md-12 mb-3">
                                            <div id="mapid" class="float-right"><p>${value}</p></div>
                                        </div>
                                    </div>`;
                    that.component.prepend(that.msgBlock);
                    that.createMap(that.lat, that.long, that.token);
                } else {
                    that.msgBlock = `<div class="msg-right row">
                                        <div class="col-md-12">
                                            <div class="float-right"><p>${value}</p></div>
                                        </div>
                                    </div>`;
                    that.component.prepend(that.msgBlock);
                }
            };
        };
    };

    this.createMap = function (lat, long, token) {
        that.botMsg.map = L.map('mapid').setView([lat, long], 10);
        L.tileLayer('https://api.mapbox.com/styles/v1/{id}/light-v10/tiles/{z}/{x}/{y}?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 25,
            id: 'mapbox',
            tileSize: 256,
            zoomOffset: 0,
            accessToken: token
        }).addTo(that.botMsg.map);
        L.marker([lat, long]).addTo(that.botMsg.map);
    };

    this.checkSmallTalk = function (msg) {
        switch (msg.toLowerCase()) {
            case "bonjour":
            case "bonjour!":
            case "salut!":
            case "hey":
            case "coucou":
                return "Coucou toi!"
            case "ca va?":
            case "ca va":
            case "comment vas-tu?":
            case "comment ca va?":
                return "Ca va bien, merci."
            case "comment tu t'appelles?":
            case "t'es qui?":
            case "t'as quel age?":
            case "tu fais quoi dans la vie?":
            case "tu t'appelles comment?":
                return "T'as pas besoin de le savoir."
        }
    }

    this.update = function () {
        that.getMsg();
        that.msgInput.val('');
    };
};


var convChat = new ConvChat(".msg-conv");

$(".btn-send").click(function(e) {
    e.preventDefault();
    convChat.update();
});

$(".btn-load").hide();
