$(document).ready(function() {
    var options = {
        'source': '.charsleft',
    }
    var calculate = function(target, maxlength) {
            var remaining = maxlength - $(target).val().length;
            $(target).parent().find('.count').html(remaining);
            /* Over 50%, change colour to orange */
            p = (100 * remaining) / maxlength;
            if (p < 25) {
                $(target).parent().find('.count').removeClass('orange')
                $(target).parent().find('.count').addClass('red');
            } else if (p < 50) {
                $(target).parent().find('.count').removeClass('red');
                $(target).parent().find('.count').addClass('orange');
            } else {
                $(target).parent().find('.count').removeClass('orange red');
            }
        };
    $(document).on('keyup', options.source, function(event) {
        var maxlength = $(event.target).attr('maxlength');
        calculate(event.target, maxlength);
    });
});