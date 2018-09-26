function Class_index() {
        this.select_dep = $('#select_dep');
        this.pro_info = $('#pro_info');
        this.teach_info = $('#teach_info')
}

Class_index.prototype.listenChangeSelect = function(){
    var self = this;
    self.select_dep.change(function () {
        stu_ajax.get({
            "url":'/cms/class/',
            'data':{'dep_id':$(this).val()},
            'success':function (result) {
                self.pro_info.find('option').filter(':gt(0)').remove();
                data = result['data'][0];
                for (var i = 0; i <data.length ; i++) {
                    self.pro_info.append('<option value="'+data[i].id+'">'+data[i].pro_name+'</option>')
                }
            }
        })
    })
};


Class_index.prototype.listenChangeSelect2 = function(){
    var self = this;
    self.pro_info.change(function () {
        stu_ajax.get({
            "url":'/cms/class/',
            'data':{'dep_id':self.select_dep.val(),
            'pro_id':$(this).val()},
            'success':function (result) {
                self.teach_info.find('option').filter(':gt(0)').remove();
                data = result['data'][0];
                for (var i = 0; i <data.length ; i++) {
                     self.teach_info.append('<option value="'+data[i].id+'">'+data[i].teach_name+'</option>')
                }
            }
        })
    })
};


$(function () {
    var classe = new Class_index();
    classe.listenChangeSelect();
    classe.listenChangeSelect2();
});

