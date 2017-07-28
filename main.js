// inicializamos con jquery cuando el documento este cargado completamente :)
$(document).on('ready',function(){
    console.log("el documento esta listo");
    jQuery.support.cors = true;
    $.ajax({
	  url: "http://34.209.24.195/facturas",
	  crossDomain: true,
	  type: 'post',
	  dataType: 'jsonp',
		headers: {
        "X-Content-Type-Options": "nosniff"
    	},
	  contentType: "application/json; charset=utf-8",
	  xhrFields: {
	        withCredentials: true
	    },
	  data: {
	    id: '9a936864-3c10-49a9-b8bd-94bfe26b2163',
	    start:'2017-01-01',
	    finish:'2017-01-11'
	  },
	  success: function( result ) {
	    $( "#mensaje" ).html( "<strong>" + result + "</strong> degrees" );
	  }
	});
});


 id = '9a936864-3c10-49a9-b8bd-94bfe26b2163';
start = '2017-01-01';
 finish = '2017-01-11';
 url = "http://34.209.24.195/facturas?id="+id+"&start="+start+"&finish="+finish+"    ";

$.ajax({
  dataType: "jsonp",
  url: url ,
  }).done(function ( data ) {
  // do my stuff
  console.log(data);
});


// $.ajax({
// 	  url: url,
// 	  crossDomain: true,
// 	  type: 'GET',
// 	  dataType: 'json',
// 	  headers: {
//         "X-Content-Type-Options": "nosniff",
//         "content-Type":"application/json",
//         "Accept":"application/json",
//         "Access-Control-Allow-Credentials": "true",
//         "Access-Control-Allow-Headers":"*"
//       },
// 	  contentType: "application/json; charset=utf-8",
// 	  withCredentials: true,
// 	  xhrFields: {
// 	        withCredentials: true
// 	    },
// 	  success: function( result ) {
// 	  	alert(result);
// 	    $( "#mensaje" ).html( "<strong>" + result + "</strong> degrees" );
// 	  }
// 	});