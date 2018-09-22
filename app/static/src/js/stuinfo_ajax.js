



var csrftoken = $('meta[name=csrf-token]').attr('content')


var stu_ajax = {

    'get':function (args) {
        args['method'] = 'get';
        this.ajax(args)
    },
    'post':function (args) {
        args['method'] = 'post';
        this._ajaxSetup_Cookie();
        this.ajax(args)
    },
    'ajax':function (args) {
        $.ajax(args)
    },
    '_ajaxSetup_Cookie':function () {
        $.ajaxSetup({
         beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken)
            }
    }
});
    }
}
