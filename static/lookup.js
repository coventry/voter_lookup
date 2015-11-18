current_request_number = 0;
displayed_request_number = 0;

ajax = function(querystring) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
	    resp = JSON.parse(xmlhttp.responseText);
	    requestnum = parseInt(resp.reqnum)
	    if (requestnum >= displayed_request_number) {
		document.getElementById("results").innerHTML = resp.result;
		displayed_request_number = requestnum;
	    }
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
    query.push('reqnum=' + current_request_number.toString());
    current_request_number += 1;
    querystring = "/lookup?" + query.join("&");
    ajax(querystring);
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
    
