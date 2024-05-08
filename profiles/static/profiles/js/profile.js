let countrySelected = $('#id_default_country').val();
if (countrySelected == 'default') {
    $('#id_default_county').css('color', '#aab7c4');
}
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if (countrySelected == 'default') {
        $('#id_default_country').css('color', '#aab7c4');
    } else {
        $('#id_default_country').css('color', '#000');
    }
});