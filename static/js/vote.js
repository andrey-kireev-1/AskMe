$('.js-vote').on('click', function(ev) {
    console.log("CLICK")
    ev.preventDefault();
    var $this = $(this),
        action = $this.data('action'),
        qid = $this.data('qid');
    $.ajax('/question_vote/', {
        method: 'POST',
        data: {
            action: action,
            qid: qid
        }
    }).done(function(data) {
        console.log(data['error']);
        if (data['error'] == "") {
            $('.q-' + qid).html(data['rating']);
        } else {
            alert('Action not permitted')
        }
       
        str = "#block" + qid;
        $('.js-' + qid).hide();
        $("#block"+qid).load("/question/"+qid+"/ #block"+qid+" > *");
    });
});

$('.js-vote-ans').on('click', function(ev) {
    ev.preventDefault();
    var $this = $(this),
        action = $this.data('action'),
        aid = $this.data('aid');
    $.ajax('/answer_vote/', {
        method: 'POST',
        data: {
            action: action,
            aid: aid
        }
    }).done(function(data) {
        console.log(data['error']);
        if (data['error'] == "") {
            $('.ans-' + aid).html(parseInt($('.ans-' + aid).html()) + parseInt(data['rating']));
        } else {
            alert('Action not permitted')
        }
        $('.js-ans-' + aid).hide();
    });
});