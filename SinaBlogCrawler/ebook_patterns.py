class CalibrePattern:
	html_pattern = """<?xml version='1.0' encoding='utf-8'?>
	<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
	<title>$title</title>
	</head>
	<body>
	<h2>$title</h2>
	<h5>$pubtime</h5>
	<div>
		$body
	</div>
	</body>
	</html>"""

	# node navMap in toc.ncx for Calibre ebook editor
	navmap_pattern = """
	<navPoint id="num_$n" playOrder="$n">
		<navLabel>
		<text>$title</text>
		</navLabel>
		<content src="$filename"/>
	</navPoint>
	"""