<script type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
<script>
(function poll() {
    $.ajax({
        url: "http://172.31.99.3/vehicle",
        type: "GET",
        success: function(data) {
            // do something here
            var jsonString = JSON.stringify(data, undefined, 4);
        },
        dataType: "json",
        crossDomain: true,
        complete: setTimeout(function() {poll()}, 1000),
        timeout: 1000
    })
})();
</script>