<<<<<<< HEAD
if (window.yourlabs === undefined) window.yourlabs = {};

yourlabs.RemoteAutocompleteWidget = {
    /*
    The default deck getValue() implementation just returns the PK from the
    choice HTML. RemoteAutocompleteWidget.getValue's implementation checks for
    a url too. If a url is found, it will post to that url and expect the pk to
    be in the response.

    This is how autocomplete-light supports proposing values that are not there
    in the database until user selection.
    */
    getValue: function(choice) {
        var value = choice.data('value');
        console.log("value:",value)
        // var url = "/autocomplete/TagAutoComplete/"
        if (value==="000") {
            choice.html(this.input.val())
=======
FlyWidget = {
    getValue: function(choice) {
        var value = choice.data('value');
        console.log("creating a new choice")

        if (value == 'create') {
            choice.html(this.input.val())

>>>>>>> origin/master
            $.ajax(this.autocomplete.url, {
                async: false,
                type: 'post',
                data: {
<<<<<<< HEAD
                    'name': this.input.val()
=======
                    'name': this.input.val(),
>>>>>>> origin/master
                },
                success: function(text, jqXHR, textStatus) {
                    value = text;
                }
            });

            choice.data('value', value);
        }

        return value;
    }
}

$(document).bind('yourlabsWidgetReady', function() {
    // Instanciate decks with RemoteAutocompleteWidget as override for all widgets with
    // autocomplete 'remote'.
<<<<<<< HEAD
    $('body').on('initialize', '.autocomplete-light-widget[data-widget-bootstrap=rest_model]', function() {
        console.log("initialize flyyyyyyyy")
        $(this).yourlabsWidget(yourlabs.RemoteAutocompleteWidget);
    });
});
=======
    console.log("here")
    $('body').on('initialize', '.autocomplete-light-widget[data-widget-bootstrap=fly-widget]', function() {
        $(this).yourlabsWidget(FlyWidget);
    });
});
>>>>>>> origin/master
