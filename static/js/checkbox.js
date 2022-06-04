$('.form-correct-input').on('click',function(ev) {
    ev.preventDefault();
    var $this = $(this),
        aid = $this.data('aid');
        qid = $this.data('qid');
    $.ajax('/correct/', {
        method: 'POST',
        data: {
            aid: aid,
            qid: qid
        }
    }).done(function(data) {
        console.log(data['error']);
        if (data['error'] == "") {
            if (data['value']) {
                $('.correct-' + aid).prop('correct', true);
                $('#block-ans-' + aid).load("/question/"+qid+"/ #block-ans-"+aid+" > *");
                
                
            } else {
                
                
                
                $('.correct-' + aid).prop('correct', false);
                $('#block-ans-' + aid).load("/question/"+qid+"/ #block-ans-"+aid+" > *");
            }
        } else {
            alert('Action not permitted')
        }
    });
});