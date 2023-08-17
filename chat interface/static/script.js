$(document).ready(function() {
    $('#send-button').click(function() {
        var userInput = $('#user-input').val();
        if (userInput) {
            $('#chat-box').append('<div class="user-bubble">' + userInput + '</div>');
            $('#user-input').val('');
            
            var postData = {
                "user_input": userInput
            };

            $.ajax({
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify(postData),
                url: "/classify",
                success: function(response) {
                    $('#chat-box').append('<div class="bot-bubble">' + response.predicted_function + '</div>');
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }
    });
});
