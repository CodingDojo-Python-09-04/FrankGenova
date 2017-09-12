/* eslint-env jquery*/

$(document).ready(function(){
    $( function() {
        console.log("in listener");
        "use strict";
        window.addEventListener("load", function() {
            var form = document.getElementById("needs-validation");
            form.addEventListener("submit", function(event) {
                if (form.checkValidity() == false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add("was-validated");
            }, false);
        }, false);
    });
});

// validity is not working