$(document).ready(function() {
    $( "#autocomplete" ).autocomplete({
      minLength: 4,
      source: function( request, response ) {
        var matcher = new RegExp( "^" + $.ui.autocomplete.escapeRegex( request.term ), "i" );
        response( $.grep( places, function( item ){
            return matcher.test( item );
        }).slice(0, 10) );
      }
    });
});