
// center map to San Francisco
function initialize() {
  var mapProp = {
    center: new google.maps.LatLng(37.773972,-122.431297),
    zoom:5,
    mapTypeId:google.maps.MapTypeId.ROADMAP
  };
  var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
}
google.maps.event.addDomListener(window, 'load', initialize);

