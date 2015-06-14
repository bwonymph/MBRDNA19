var ref = new Firebase("https://docs-examples.firebaseio.com/web/saving-data/fireblog/posts");
// Attach an asynchronous callback to read the data at our posts reference
ref.on("value", function(snapshot) {
  console.log(snapshot.val());
}, function (errorObject) {
  console.log("The read failed: " + errorObject.code);
});

ref.on("child_added", function(snapshot, prevChildKey) {
  var newPost = snapshot.val();
  console.log("Author: " + newPost.author);
  console.log("Title: " + newPost.title);
  console.log("Previous Post ID: " + prevChildKey);

// Get the data on a post that has changed
ref.on("child_changed", function(snapshot) {
  var changedPost = snapshot.val();
  console.log("The updated post title is " + changedPost.title);
});

<div id="areaChart" style="width: 800px; height: 200px"></div>
<script>
  $('#areaChart').epoch({
    type: 'time.area',
    data: areaChartData
  });
</script>

var areaChartData = [
  // The first layer
  {
    label: "Fuel efficiency",
    values: [{Timestamp, Fuel_Consumption}]
  }];

/*      
<div id="gaugeChart" class="epoch gauge-small"></div>
<script>
  $('#gaugeChart').epoch({
    type: 'time.gauge',
    
    value: 0.5
  });
</script>

<div id="gaugeChart2" class="epoch gauge-small"></div>
<script>
  $('#gaugeChart').epoch({
    type: 'time.gauge',
    value: 0.5
  });
</script>

<div id="gaugeChart3" class="epoch gauge-small"></div>
<script>
  $('#gaugeChart').epoch({
    type: 'time.gauge',
    value: 0.5
  });
</script>

<div id="gaugeChart4" class="epoch gauge-small"></div>
<script>
  $('#gaugeChart').epoch({
    type: 'time.gauge',
    value: 0.5
  });
</script>*/