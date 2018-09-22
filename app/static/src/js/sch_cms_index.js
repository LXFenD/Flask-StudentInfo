function Sch_Info(){
        this.btn_save = $('.btn-save');
}

Sch_Info.prototype.listenClickSaveEvent = function(){
    var self = this;
     var ue = UE.getEditor('container', {
                'serverUrl': '/cms/editor/'
            });

    self.btn_save.click(function () {
        var sch_name = $("#sch-name").val();
        var sch_address = $("#sch-address").val();
        var sch_email = $("#sch-email").val();
        var sch_phone = $("#sch-phone").val();
        var sch_time = $("#sch-time").val();
        var sch_area = $("#sch-area").val();
        var sch_content = ue.getContent();
        data = {
            'sch_name':sch_name,
            'sch_address':sch_address,
            'sch_email':sch_email,
            'sch_phone':sch_phone,
            'sch_time':sch_time,
            'sch_area':sch_area,
            'sch_content':sch_content,
        }
        stu_ajax.post({
            'url':'/cms/sch_detail/',
            'data':data,
            'success':function () {
                alert('成功');
            }
        })
    });
};





$(function() {
    var sch = new Sch_Info();
    sch.listenClickSaveEvent();
});