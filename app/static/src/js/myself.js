function MySelf() {
    this.change = $('.change')
    this.input_change = $('#input-change')
    this.span_value = this.input_change.text();
    this.span_add = $('<span id="input-change"></span>');
    this.input_add = $('<input style="border-radius: 5px;border: 1px solid #32AAEE; padding-left: 3px"/>');
    this.is_add = true;
    this.add_value = ""
    this.img_click = $('.info-img img');
    this.input_file = $('.info-img input[name="upimg"]');
    this.btn_load = $('.btn-load');
    this.is_show = true;
    this.ueditor = $('<script id="container" name="content" type="text/plain"></script>')
}

MySelf.prototype.ListenChangeEvent = function () {
    var self = this;
    self.change.click(function () {

        if (self.is_add) {
            self.input_change.remove();
            if (self.span_add) {
                self.span_add.remove();
            }
            self.input_add.insertAfter(".famingyan");
            self.input_add.val(self.span_value);
            $(this).text('确定修改');
            self.is_add = false
        } else {

            var input_s = $(this).parent().children('input');
            if (input_s) {
                  stu_ajax.get({
                    'url':'/cms/myself/',
                    'data':{
                        'value':input_s.val()
                    },
                    'success':function (result) {
                        console.log(result['data']['value'])
                        self.add_value = result['data']['value']
                        input_s.remove()
                        self.span_add.insertAfter(".famingyan");
                        self.span_add.text(self.add_value);
                        self.is_add = true;

                    }
            });
            }
            $(this).text('更改');

        }

    });
};

MySelf.prototype.ListenClickUpoloadImageEvent = function()
{
        var self = this;
        self.img_click.click(function () {
            self.input_file.click()
        })
    self.input_file.change(function () {
        var files = this.files[0];
        var formdata = new FormData();
        formdata.append('file',files);
        stu_ajax.post({
            'url':'/cms/upload_file/',
            'data':formdata,
            'processData':false,
            'contentType':false,
            'success':function (result) {
                url_to = result['data']['url']
                self.img_click.attr('src',url_to)
            }
        })
    })

};

MySelf.prototype.ListenClickLoadSaveEvent = function()
{
    var self = this;
    var info_text = $('.info-text');
    var value = info_text.html();
    self.btn_load.click(function () {
        if(self.is_show)
        {
            info_text.text('');
            info_text.append(self.ueditor);
            self.ueditor.text(value);
            self.ue = UE.getEditor('container', {
                'serverUrl': '/cms/editor/'
            });
            self.is_show = false
        }else
        {
            info_text.children(self.ueditor).remove();
            info_text.append(self.ue.getContent());
            stu_ajax.get({
               'url':'/cms/up_detail/',
                'data':{
                   'detail':self.ue.getContent()
                },
                'success':function (result) {
                    if(result['code'] == 200)
                    {
                        window.location.reload();
                    }else {

                    }
                }
            });
            window.location.reload();
            self.is_show = true;
        }

    })

};

$(function () {
    var myself = new MySelf()
    myself.ListenChangeEvent();
    myself.ListenClickUpoloadImageEvent();
    myself.ListenClickLoadSaveEvent();

})