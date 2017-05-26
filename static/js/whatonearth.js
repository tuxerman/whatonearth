var WhatOnEarth = (function() {

    var settings = {
        baseGetTermURL: '/term/',
        autocompleteURL: '/term/autocomplete',
    };

    var uiElements = {
        searchBox: null,
        definitionDiv: null,
    };

    var populateDivWithDefinition = function(div, definedTerm) {
        div.append('<h3>' + definedTerm.term + '</h3>');
        div.append('<p>' + definedTerm.definition + '</p>');

        div.append('<h4>Who</h4>');
        div.append('<p>' + definedTerm.who + '<p>');

        div.append('<h4>More</h4>');
        moreLinks = $('<ul>');
        $.each(definedTerm.more, function(index, linkInfo) {
            moreLinks.append('<li><a href="' + linkInfo.url + '">' + linkInfo.title + '</a></li>')
        });
        div.append(moreLinks);
    };

    var refreshDefinitionDiv = function(term) {
        $.getJSON(settings.baseGetTermURL + term, function(definedTerm) {
            uiElements.definitionDiv.empty();
            populateDivWithDefinition(uiElements.definitionDiv, definedTerm);
        });
    };

    var bindElements = function() {
        uiElements.searchBox = $('#search-box');
        uiElements.definitionDiv = $('#definition-div');
    };

    var init = function() {
        bindElements();

        // Set enter key behaviour
        uiElements.searchBox.keypress(function(e) {
            if (e.which == 13) {
                refreshDefinitionDiv(uiElements.searchBox.val());
                return false;
            }
        });

        // Autocompleter
        new autoComplete({
            selector: '#search-box',
            source: function(term, response) {
                $.getJSON(settings.autocompleteURL, {
                    query: term
                }, function(data) {
                    response(data);
                });
            },
            onSelect: function(event, term, item) {
                uiElements.searchBox.val(term);
                refreshDefinitionDiv(uiElements.searchBox.val());
            }
        });
    }

    return {
        init: init,
    };

})();
