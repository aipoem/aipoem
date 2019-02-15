
<html>
<!--

	DIVISIONE IN SILLABE - versione Javascript
	
	ORIGINALE IN CBM BASIC 2.0 by Franco Musso, Marzo 1983:
	http://ready64.it/ccc/pagina.php?ccc=09&pag=036.jpg
	
	TRADUZIONE IN JAVASCRIPT by Francesco Sblendorio, Maggio 2013:
	http://www.sblendorio.eu/Misc/Sillabe

-->
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
<title>Divisione in sillabe</title>
<style>
.sans-serif {
	font-family: tahoma, verdana, arial, sans serif;
	font-size: 15px;
}

</style>
<script>

function isVowel(c) {
	return "AEIOUÁÉÍÓÚÀÈÌÒÙ".indexOf(c.toUpperCase()) != -1;
}

function divide(word) {
	var a = word.toUpperCase();
	var result="";
	var s=0;
	while (s < a.length) {
		if (!isVowel(a.charAt(s))) {
			result += word.charAt(s); s++;
		} else if (!isVowel(a.charAt(s+1))) {
			if (s+2 >= a.length) {
				result += word.substring(s,s+2)+"-"; s += 2;
			} else if (isVowel(a.charAt(s+2))) {
				result += word.charAt(s)+"-"; s++;
			} else if (a.charAt(s+1) == a.charAt(s+2)) {
				result += word.substring(s,s+2)+"-"; s += 2;
			} else if ("SG".indexOf(a.charAt(s+1)) != -1) {
				result += word.charAt(s)+"-"; s++;
			} else if ("RLH".indexOf(a.charAt(s+2)) != -1) {
				result += word.charAt(s)+"-"; s++;
			} else {
				result += word.substring(s,s+2)+"-"; s+=2;
			}
		} else if ("IÍÌ".indexOf(a.charAt(s+1)) != -1) {
			if (s>1 && a.substring(s-1,s+1)=="QU" && isVowel(a.charAt(s+2))) {
				result += word.substring(s,s+2); s += 2;
			} else if (isVowel(a.charAt(s+2))) {
				result += word.charAt(s)+"-"; s++;
			} else {
				result += word.charAt(s); s++;
			}
		} else if ("IÍÌUÚÙ".indexOf(a.charAt(s))!=-1) {
			result += word.charAt(s); s++;
		} else {
			result += word.charAt(s)+"-"; s++;
		}
	}
	
	if (result.charAt(result.length-1)=="-")
		result = result.substring(0,result.length-1);
	return result;
}


function divide_sentence(s) {
	if (s==null) {
		return "";
	}
	
	var result="";
	var i=0;
	while (s.length>0) {
		word = s.substr(0,s.search(/[^a-záéíóúàèìòù]|$/i));
		result += divide(word);
		s = s.substr(word.length);
		
		separator = s.substr(0,s.search(/[a-záéíóúàèìòù]|$/i));
		result += separator;
		s = s.substr(separator.length);
	}
	return result;
}

function do_divide() {
	var word = document["form0"].word.value;
	if (document.all) element = document.all["result"]; else element=document.getElementById("result");
	element.innerHTML = divide_sentence(word).replace(/\n/g,"<br/>\n");
}

</script>
	</head>

<body class="sans-serif">
<table cellpadding="5" style="background-color:cyan; border-style:solid; border-color:black; border-width:1px"><tr><td valign="top" style="width:420px">
<span style="font-weight:bold;color:navy">Inserisci qui il testo:</span>
<form id="form0" name="form0" accept-charset="UTF-8">
<textarea class="sans-serif" name="word" id="word" rows="25" cols="55" onkeyup="do_divide()"></textarea><br/>
</form>
</td><td valign="top" style="width:420px">
<span style="font-weight:bold;color:navy">Testo diviso in sillabe:</span><br />
<script>if (document.all) document.write("<br />");</script>
<span id="result" name="result"></span>
</td></tr></table>
</body>

</html>
