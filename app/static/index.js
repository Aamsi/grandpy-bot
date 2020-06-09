function ConvChat (selector) {
    that = this;
    this.component = $(selector);
    this.msgBlock = "";
    this.msgInput = $(".msg-input");
    this.msgContent = "";
    this.author = "user";

    this.getMsg = function () {
        that.msgContent = that.msgInput.val();
        if (that.msgContent) {
            that.sendMsg();
            $.post('/process_msg', {
                msg_content: that.msgContent
            }, function (res) {
                that.msgContent = res.msg;
                that.author = "bot"
            })
            .done(function() {
                that.sendMsg();
            });
        };
    };

    this.sendMsg = function () {
        if (that.author == 'user') {
            that.msgBlock = `<div class='col-md-3 ml-2 mb-3 msg-left'><p>${that.msgContent}</p></div>`
        } else {
            that.msgBlock = `<div class='col-md-3 ml-2 mb-3 msg-right'><p>${that.msgContent}</p></div>`
        };
        that.component.prepend(that.msgBlock);
    };

    this.update = function () {
        that.author = 'user';
        that.getMsg();
        that.msgInput.val('');
    };
};


var convChat = new ConvChat(".msg-thread");

$(".btn").click(function(e) {
    e.preventDefault();
    convChat.update();
});
