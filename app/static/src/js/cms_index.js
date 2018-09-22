function Cms_index() {
    this.ctx = document.getElementById("myChart").getContext('2d');
    this.ctx2 = document.getElementById("myChart2").getContext('2d');
    this.ctx3 = document.getElementById("myChart3").getContext('2d');
    this.backgroundColors = [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)'
    ];
    this.borderColors = [
        'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
    ];
}

Cms_index.prototype.reuturn_data = function (labels, data, backgroundColor, borderColor) {
    var data = {
        labels: labels,
        datasets: [{
            label: labels,
            data: data,
            backgroundColor: backgroundColor,
            borderColor: borderColor,
            borderWidth: 1
        }],
    };
    return data
};


Cms_index.prototype.reuturn_options = function (text) {
    var options = {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        },
        title: {
            display: true,
            text: text
        }
    };
    return options
};


Cms_index.prototype.ShowEvent = function () {
    var self = this;
    stu_ajax.get({
        'url': '/cms/',
        'data': {'teacher': 'teacher', 'student': 'student', 'class': 'class'},
        'success': function (result) {
            self.labeles = result['data']['labels'];
            self.teach_dataes = result['data']['teacher_dataes'];
            self.text = '系部教师比';
            new Chart(self.ctx, {
                type: 'bar',
                data: self.reuturn_data(self.labeles, self.teach_dataes, self.backgroundColors, self.borderColors),
                options: self.reuturn_options(self.text),
            });
            self.student_dataes = result['data']['student_dataes'];
            self.text = '系部学生数比';
            new Chart(self.ctx2, {
                type: 'line',
                data: self.reuturn_data(self.labeles, self.student_dataes, self.backgroundColors, self.borderColors),
                options: self.reuturn_options(self.text),
            });
            self.class_dataes = result['data']['class_dataes'];
            self.text = '系部教师数比';
            new Chart(self.ctx3, {
                type: 'polarArea',
                data: self.reuturn_data(self.labeles, self.class_dataes, self.backgroundColors, self.borderColors),
                options: self.reuturn_options(self.text),
            });
        }
    });

};


$(function () {
    var cms = new Cms_index();
    cms.ShowEvent()
});


