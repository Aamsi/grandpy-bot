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
                    that.lat = res.lat;
                    that.long = res.long;
                    that.token = res.token;
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
                if (key == 'map') {
                    that.msgBlock = `<div class='col-md-3 ml-2 mb-3 msg-right'><div id='mapid'>${value}</div></div>`;
                    that.component.prepend(that.msgBlock);
                    that.createMap(that.lat, that.long, that.token);
                } else {
                    that.msgBlock = `<div class='col-md-3 ml-2 mb-3 msg-right'><p>${value}</p></div>`
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
