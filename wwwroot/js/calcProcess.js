$(document).ready(function(){
		
    $("#calcData").keypress(function(event) {
		$("#calcError").text("");
		$("#results").css("display", "none");
		if (event.which == 13) {
        	event.preventDefault();
        	$("#calcSubmit").click();
		}
        return /\d/.test(String.fromCharCode(event.keyCode));
    });
	
	$("#calcSubmit").click(function(event){
		var intRegex = /[0-9 -()+]+$/; 
		if ($("#calcData").val().length === 0  || $("#calcData").val() == "0" || !intRegex.test($("#calcData").val()))
		     { $("#calcError").text("Please enter a positive number."); }
		else {
			var calcInt = parseInt($("#calcData").val());
			var arrSeq = [];
			var arrEvens = [];
			var arrOdds = [];
			var arrMultis = [];
			var arrFibo = [0,1,1];
			var nextFibo = 2;
			var prevFibo = 1;
					
			for ( var i = 1; i <= calcInt; i++ ) {
				// Regular Sequence
                arrSeq.push(i);				
				// Odd & Evens Sequence
				if (i % 2 === 1) { arrOdds.push(i);} else { arrEvens.push(i); }				
				// Multiples (C,E,Z) Sequence
				if (i % 3 === 0  && i % 5 === 0) { arrMultis.push("Z"); }
				else if (i % 5 === 0 ) { arrMultis.push("E"); }
				else if (i % 3 === 0 ) { arrMultis.push("C"); }
				else arrMultis.push(i);				
				// Fibonacci Sequence
				if( i === nextFibo ) {
					arrFibo.push(i);
					nextFibo = prevFibo + i;
					prevFibo = i;
				}
			}
			
			$("#numsSeq").text(arrSeq.join(", "));
			$("#numsOdds").text(arrOdds.join(", "));
			$("#numsMultis").text(arrMultis.join(", "));
			$("#numsFibo").text(arrFibo.join(", "));
			if(arrEvens.length > 0) { 
				$("#numsEvens").text(arrEvens.join(", "));
			} else {
				$("#numsEvens").text("No even numbers"); 
			}
	         
			$("#results").css("display", "block");
		}
	});
});

