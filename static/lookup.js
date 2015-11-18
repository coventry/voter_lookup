ajax = function(querystring) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            document.getElementById("results").innerHTML = xmlhttp.responseText;
        }
    };
    xmlhttp.open("GET", querystring, true);
    xmlhttp.send();
}

lookup = function() {
    var form = document.getElementById("signupform");
    var query = [];
    for (eidx=0; eidx < form.elements.length; eidx++) {
        element = form.elements[eidx];
        if (element.className != "exclude") {
            query.push(element.name + "=" + element.value);
        }
    }
    query.push('active_element=' + document.activeElement.name);
    querystring = "/lookup?" + query.join("&");
    ajax(querystring);
}

keypress = function(e) {
    if (event.which == 13 || event.keyCode == 13) {
         e.preventDefault();
         lookup();         
    }
    if (event.which == 32 || event.keyCode == 32) {
        lookup();
    }
    return true;
}

// Can't call this "clear".  Some kind of namespace shadowing?
clear_form = function(e) {
    var form = document.getElementById("signupform");
    for (eidx=0; eidx < form.elements.length; eidx++) {
        element = form.elements[eidx];
        if (element.className != "exclude") {
            element.value = '';
        }
    }
    document.getElementById("RESIDENTIAL_ZIP").focus()
}
    
